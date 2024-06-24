# Timble Services

Timble Services is a Django project that includes asynchronous and synchronous tasks using Celery and Redis.

## Contents

1. [Prerequisites](#prerequisites)
2. [Setup Instructions, Ubuntu](#setup-instructions-ubuntu)
3. [Setup Instructions, Windows](#setup-instructions-windows)
4. [Testing Endpoints with Postman](#testing-endpoints-with-postman)
5. [Adding a New App and Sample Method](#adding-a-new-app-and-sample-method)
6. [Fetching Results of Asynchronous Tasks](#fetching-results-of-asynchronous-tasks)
7. [Notes](#notes)

## Prerequisites

- Python 3.6+
- Django
- Redis
- Celery

## Cloning the Repository and Working with Branches

1. **Clone the Main Branch:**
   ```sh
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Create and Checkout a New Branch:**
   ```sh
   git checkout -b <new_branch_name>
   ```

3. **Make Changes:**
   - Make the necessary changes to your files.

4. **Add and Commit Changes:**
   ```sh
   git add .
   git commit -m "Describe your changes"
   ```

5. **Push the New Branch to the Remote Repository:**
   ```sh
   git push origin <new_branch_name>
   ```

6. **Merge the New Branch into the Main Branch:**
   - Switch back to the main branch:
     ```sh
     git checkout main
     ```
   - Pull the latest changes from the remote main branch:
     ```sh
     git pull origin main
     ```
   - Merge the new branch into the main branch:
     ```sh
     git merge <new_branch_name>
     ```
   - Push the updated main branch to the remote repository:
     ```sh
     git push origin main
     ```


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
- **Parameters:** 

  In Postman, click on the "Params" tab and add the following key-value pairs:

  - **Key:** `x`, **Value:** `4`
  - **Key:** `y`, **Value:** `5`

  Example:

  ```
  Key         | Value
  ----------------------
  x           | 4
  y           | 5
  ```

### Asynchronous Addition

- **URL:** `http://localhost:8000/msme/add_async/`
- **Method:** GET
- **Parameters:** 

  In Postman, click on the "Params" tab and add the following key-value pairs:

  - **Key:** `x`, **Value:** `4`
  - **Key:** `y`, **Value:** `5`

  Example:

  ```
  Key         | Value
  ----------------------
  x           | 4
  y           | 5
  ```

### Synchronous Multiplication

- **URL:** `http://localhost:8000/gst_analytics/multiply_sync/`
- **Method:** GET
- **Parameters:** 

  In Postman, click on the "Params" tab and add the following key-value pairs:

  - **Key:** `x`, **Value:** `4`
  - **Key:** `y`, **Value:** `5`

  Example:

  ```
  Key         | Value
  ----------------------
  x           | 4
  y           | 5
  ```

### Asynchronous Multiplication

- **URL:** `http://localhost:8000/gst_analytics/multiply_async/`
- **Method:** GET
- **Parameters:** 

  In Postman, click on the "Params" tab and add the following key-value pairs:

  - **Key:** `x`, **Value:** `4`
  - **Key:** `y`, **Value:** `5`

  Example:

  ```
  Key         | Value
  ----------------------
  x           | 4
  y           | 5
  ```

## Adding a New App and Sample Method

### 1. Create a New App

Run the following command to create a new app:

```bash
python manage.py startapp newapp
```

### 2. Register the New App

Add the new app to `INSTALLED_APPS` in `timble_services/settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'msme',
    'gst_analytics',
    'newapp',  # Add this line
]
```

### 3. Create a Synchronous and Asynchronous Task

#### `newapp/tasks.py`

```python
from celery import shared_task
import logging

logger = logging.getLogger(__name__)

@shared_task
def add(x, y):
    logger.debug(f"Adding {x} + {y}")
    return x + y
```

### 4. Create Views for the New Task

#### `newapp/views.py`

```python
from django.http import JsonResponse
from .tasks import add
import logging

logger = logging.getLogger(__name__)

# Asynchronous view using Celery
def add_numbers_async(request):
    try:
        x = int(request.GET.get('x', 0))
        y = int(request.GET.get('y', 0))
        result = add.delay(x, y)  # Asynchronous task
        return JsonResponse({'task_id': result.id})
    except Exception as e:
        logger.error(f"Error in add_numbers_async: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)

# Synchronous view
def add_numbers_sync(request):
    try:
        x = int(request.GET.get('x', 0))
        y = int(request.GET.get('y', 0))
        result = add(x, y)  # Synchronous task
        return JsonResponse({'result': result})
    except Exception as e:
        logger.error(f"Error in add_numbers_sync: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)
```

### 5. Define URLs for the New App

#### `newapp/urls.py`

```python
from django.urls import path
from .views import add_numbers_async, add_numbers_sync

urlpatterns = [
    path('add_async/', add_numbers_async, name='add_numbers_async'),
    path('add_sync/', add_numbers_sync, name='add_numbers_sync'),
]
```

### 6. Include the New App URLs in the Project URLs

#### `timble_services/urls.py`

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('msme/', include('msme.urls')),
    path('gst_analytics/', include('gst_analytics.urls')),
    path('newapp/', include('newapp.urls')),  # Add this line
]
```

### Testing the New App with Postman

#### Synchronous Addition

- **URL:** `http://localhost:8000/newapp/add_sync/`
- **Method:** GET
- **Parameters:** `x=10`, `y=2`
- **Response:**
    ```json
    {
        "result": 12
    }
    ```

#### Asynchronous Addition

- **URL:** `http://localhost:8000/newapp/add_async/`
- **Method:** GET
- **Parameters:** `x=10`, `y=2`
- **Response:**
    ```json
    {
        "task_id": "some-task-id"
    }
    ```

### Verifying Asynchronous Task Completion for New App

- **URL:** `http://localhost:8000/msme/task_result/<task_id>/`
- **Method:** GET
- **Parameters:** `task_id=<task_id_received_from_async_call>`
- **Response:**
    ```json
    {
        "status": "SUCCESS",
        "result": 12
    }
    ```

## Fetching Results of Asynchronous Tasks

To fetch the result of any asynchronous task, use the following steps:

### For `msme` App

- **URL:** `http://localhost:8000/msme/task_result/<task_id>/`
- **Method:** GET

### For `gst_analytics` App

-

 **URL:** `http://localhost:8000/gst_analytics/task_result/<task_id>/`
- **Method:** GET

Replace `<task_id>` with the actual task ID you received (e.g., `f7337263-8ee9-414b-898a-931b681988c0`).

Example Response:

```json
{
    "task_id": "f7337263-8ee9-414b-898a-931b681988c0",
    "status": "SUCCESS",
    "result": 9
}
```

## Notes

- make sure Redis is running before starting Celery workers.
- activate virtual environment before running Django server & Celery worker.