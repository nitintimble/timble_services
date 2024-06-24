import io
import json
from contextlib import redirect_stdout

class CompanyScorecard:
    def __init__(self, company_info, directors_info, financial_health, financial_charges, employee_info):
        self.company_info = company_info
        self.directors_info = directors_info
        self.financial_health = financial_health
        self.financial_charges = financial_charges
        self.employee_info = employee_info
        self.weights = {
            'company_info': 0.10,
            'directors_info': 0.20,
            'financial_health': 0.40,
            'financial_charges': 0.20,
            'employee_info': 0.10
        }

    def normalize(self, value, min_value, max_value):
        normalized_value = (value - min_value) / (max_value - min_value) * 10
        print(f"Normalizing value: {value} (Min: {min_value}, Max: {max_value}) -> Normalized: {normalized_value:.2f}")
        return normalized_value

    def calculate_weighted_score(self, score, weight):
        weighted_score = score * weight
        print(f"Calculating weighted score: {score:.2f} * {weight} = {weighted_score:.2f}")
        return weighted_score

    def calculate_total_score(self):
        total_score = 0
        messages = io.StringIO()

        with redirect_stdout(messages):
            # Company Information
            company_info_score = self.normalize(self.company_info['paid_up_capital'], 0, 100000000)
            company_info_weighted = self.calculate_weighted_score(company_info_score, self.weights['company_info'])
            print(f"Company Information Score: {company_info_score:.2f} (Weighted: {company_info_weighted:.2f})")
            total_score += company_info_weighted

            # Directors Information
            directors_avg_score = sum(self.directors_info.values()) / len(self.directors_info)
            directors_weighted_score = self.calculate_weighted_score(directors_avg_score, self.weights['directors_info'])
            print(f"Directors Information:")
            for director, score in self.directors_info.items():
                print(f"  - {director}: {score:.2f}")
            print(f"Directors Average Score: {directors_avg_score:.2f} (Weighted: {directors_weighted_score:.2f})")
            total_score += directors_weighted_score

            # Financial Health
            normalized_financial_health = {
                'net_worth_growth': self.normalize(self.financial_health['net_worth_growth'], 0, 100000000),
                'profit_after_tax': self.normalize(self.financial_health['profit_after_tax'], 0, 100000000),
                'income_vs_expense': self.normalize(self.financial_health['income_vs_expense'], 0, 10)
            }

            financial_health_avg_score = sum(normalized_financial_health.values()) / len(normalized_financial_health)
            financial_health_weighted_score = self.calculate_weighted_score(financial_health_avg_score, self.weights['financial_health'])
            print(f"Financial Health:")
            for metric, score in normalized_financial_health.items():
                print(f"  - {metric}: {score:.2f}")
            print(f"Financial Health Average Score: {financial_health_avg_score:.2f} (Weighted: {financial_health_weighted_score:.2f})")
            total_score += financial_health_weighted_score

            # Financial Charges
            financial_charges_avg_score = sum(self.financial_charges.values()) / len(self.financial_charges)
            financial_charges_weighted_score = self.calculate_weighted_score(financial_charges_avg_score, self.weights['financial_charges'])
            print(f"Financial Charges:")
            for metric, score in self.financial_charges.items():
                print(f"  - {metric}: {score:.2f}")
            print(f"Financial Charges Average Score: {financial_charges_avg_score:.2f} (Weighted: {financial_charges_weighted_score:.2f})")
            total_score += financial_charges_weighted_score

            # Employee Information
            employee_info_score = self.normalize(self.employee_info['epf_employee_count'], 0, 1000)
            employee_info_weighted = self.calculate_weighted_score(employee_info_score, self.weights['employee_info'])
            print(f"Employee Information Score: {employee_info_score:.2f} (Weighted: {employee_info_weighted:.2f})")
            total_score += employee_info_weighted

            print(f"\nTotal Creditworthiness Score: {total_score:.2f} out of 10")

        return messages.getvalue(), total_score

def parse_json(json_data):
    print("Parsing JSON data...")

    company_info = {
        'paid_up_capital': int(json_data['CompanyMasterSummary']['CompanyPaidUpCapital'])
    }
    print(f"Company Information: {company_info}")

    directors_info = {}
    directors = json_data['DirectorSignatoryMasterSummary']['DirectorPastMasterSummary']['Director']
    for director in directors:
        experience_directorship = int(director['DirectorCurrentDirectorshipCount'])
        din_status = 10 if director['DINStatus'] == 'Approved' else 0
        directors_info[director['DirectorName']] = (experience_directorship + din_status) / 2
    print(f"Directors Information: {directors_info}")

    financial_health = {}
    financials = json_data['FinancialsSummary']['FinancialsYearWise']
    net_worth_growth = [float(year['NetWorth']) for year in financials]
    profit_after_tax = [float(year['ProfitAfterTax']) for year in financials]
    income_vs_expense = [float(year['TotalIncome']) / float(year['TotalExpense']) for year in financials]

    financial_health['net_worth_growth'] = max(net_worth_growth)
    financial_health['profit_after_tax'] = max(profit_after_tax)
    financial_health['income_vs_expense'] = max(income_vs_expense)
    print(f"Financial Health: {financial_health}")

    financial_charges = {
        'debt_repayment_history': 8,
        'outstanding_debts': 6
    }
    print(f"Financial Charges: {financial_charges}")

    employee_info = {
        'epf_employee_count': 7
    }
    print(f"Employee Information: {employee_info}")

    return company_info, directors_info, financial_health, financial_charges, employee_info

def calculate_company_score(json_file_path):
    with open(json_file_path, 'r') as file:
        json_data = json.load(file)

    company_info, directors_info, financial_health, financial_charges, employee_info = parse_json(json_data)
    scorecard = CompanyScorecard(company_info, directors_info, financial_health, financial_charges, employee_info)
    messages, total_score = scorecard.calculate_total_score()
    return {"messages": messages, "total_score": total_score}
