# Text To Image Generate App

**Django Project Name**: `text_to_image`

This project uses Python Django to develop an API that generates images from text using [Stability.ai](https://platform.stability.ai/). The app is designed to handle requests asynchronously, utilizing Celery and Redis for task queue management.

## Run using docker
```bash
docker-compose up --build
```

## System Requirements

- **Development Environment**: macOS (all commands provided are for macOS)
- **Python Version**: Python 3.12

Ensure your Python version is up to date, as the latest versions of Django require Python 3.12 or higher.

## Create a Virtual Environment

To create and activate a virtual environment:

```bash
python3 -m venv <env_name>
source <env_name>/bin/activate
```

## Upgrade Python and Pip:
```bash
# Upgrade pip
pip install --upgrade pip
```

## Installation
### Install Redis
Install Redis via Homebrew:
```bash
brew install redis
```
#### Verify the installation:
```bash
redis-server --version
```

### Install Node.js 
Download and install Node.js from [official website](https://nodejs.org/en)

#### Verify the installation:
```bash
node --version
```

### Install Python Libraries
Navigate to the Backend folder and install the required Python libraries using the requirements.txt file:
```bash
cd Backend
pip3 install -r requirements.txt
```

### Start the Project - How to Use
Ensure you are in the text_to_image directory where the manage.py file is located.

#### Start Redis Server
Start the Redis server for the queue service:
```bash
cd text_to_image
redis-server
```

### Start Celery Worker
Make sure you are in the text_to_image directory before starting the Celery worker:
```bash
cd Backend/text_to_image
celery -A text_to_image worker --loglevel=info
```

### Start Django Server
Start the Django development server:
```bash
cd Backend/text_to_image
python3 manage.py runserver
```
At this point, your backend should be live.

## Start the Frontend
Open a terminal in the Frontend folder and install dependencies:
```bash
npm i
```

Then, start the frontend server:
```bash
npm run dev
```

Access the application at the URL provided by the npm server, typically:
```bash
http://localhost:5173/
```

## Using the Application
Once the project is running, enter a text prompt and click “Generate Image.” The generated images are stored in the database.

## Debugging
### CORS Issues
If you encounter CORS-related issues, check the Django terminal logs and add the required address to CORS_ALLOWED_ORIGINS in settings.py:
```bash
CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    # Add other origins here as needed
]
```

## How the Project Was Built
1.	Create Django Project:
Navigate to your desired directory and start a new Django project:
```bash
django-admin startproject text_to_image
```

2.	Create Django App:
Create an app called apis within the project:
```bash
python3 text_to_image/manage.py startapp apis
```

3.	Setup Celery:
    •	Add broker and backend queue URLs in settings.py.
    •  	Initialize the Celery app in the project’s __init__.py file.
    •	Define shared tasks in tasks.py.

4.	Django Development:
•	Write Django views, URLs, and models according to the project requirements.

