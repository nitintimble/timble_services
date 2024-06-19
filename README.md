# Timble Services

Timble Services is a Django project that includes asynchronous and synchronous tasks using Celery and Redis.

## Prerequisites

- Python 3.6+
- Django
- Redis
- Celery

## Setup Instructions, Ubuntu

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/timble_services.git
cd timble_services
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Redis

```bash
sudo apt-get update
sudo apt-get install redis-server
```

### 5. Start Redis Server

```bash
sudo service redis-server start
```

### 6. Run Django Server

```bash
python manage.py runserver
```

### 7. Start Celery Worker

Open another terminal, navigate to the project directory, and run:

```bash
source venv/bin/activate
celery -A timble_services worker -l info
```

## Setup Instructions, Windows

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/timble_services.git
cd timble_services
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Redis

- Download Redis for Windows from [Redis for Windows releases](https://github.com/microsoftarchive/redis/releases).
- Extract the zip file to a directory (e.g., `C:\Redis`).

### 5. Start Redis Server

Open Command Prompt as administrator, navigate to the Redis directory, and run:

```bash
cd C:\Redis
redis-server.exe redis.windows.conf
```

### 6. Run Django Server

Open another Command Prompt, activate the virtual environment, and run:

```bash
venv\Scripts\activate
python manage.py runserver
```

### 7. Start Celery Worker

Open another Command Prompt, navigate to the project directory, activate the virtual environment, and run:

```bash
cd path\to\your\project
venv\Scripts\activate
celery -A timble_services worker -l info
```

## Testing Endpoints with Postman

### Synchronous Addition

- **URL:** `http://localhost:8000/msme/add_sync/`
- **Method:** GET
- **Parameters:** `x=4`, `y=5`

### Asynchronous Addition

- **URL:** `http://localhost:8000/msme/add_async/`
- **Method:** GET
- **Parameters:** `x=4`, `y=5`

### Synchronous Multiplication

- **URL:** `http://localhost:8000/gst_analytics/multiply_sync/`
- **Method:** GET
- **Parameters:** `x=4`, `y=5`

### Asynchronous Multiplication

- **URL:** `http://localhost:8000/gst_analytics/multiply_async/`
- **Method:** GET
- **Parameters:** `x=4`, `y=5`

### Verifying Asynchronous Task Completion

- **URL:** `http://localhost:8000/msme/task_result/`
- **Method:** GET
- **Parameters:** `task_id=<task_id_received_from_async_call>`

## Notes

- Ensure Redis is running before starting Celery workers.
- Ensure the virtual environment is activated when running Django server and Celery worker.