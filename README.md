# EventHub

## About
EventHub is a comprehensive event management platform built with Django. It allows users to create and list events, enabling participants to register easily. The platform also features a queue system for managing event registrations efficiently.

## Features
- **Event Creation and Listing:** Users can create events with detailed descriptions, times, and dates. These events are listed for all users to explore.
- **Participant Registration:** Users can register for events, with the system managing registrations and participant limits seamlessly.
- **Queue System:** A queue system is in place for events with a limited number of spots, ensuring fairness and efficiency in registration.

## Getting Started
To get EventHub up and running on your local development machine, follow these steps:

### Prerequisites
- Python (3.8 or newer)
- pip (Python package manager)
- Virtual environment (virtualenv)

### Setup Instructions

1. **Clone the Repository**
   
   Start by cloning the EventHub repository to your local machine.

   ```
   git clone https://github.com/yourusername/EventHub.git
   cd EventHub
   ```

2. **Set Up Python Virtual Environment**
   
   Create a Python virtual environment and activate it. This ensures that the project dependencies do not interfere with your global Python setup.

   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   
   With your virtual environment activated, install the project dependencies using pip.

   ```
   pip install -r requirements.txt
   ```

4. **Create a .env File**

   For security and configuration purposes, EventHub uses a `.env` file. Create this file in the root directory of your project and add the following content:

   ```
   SECRET_KEY=XXXX
   DEBUG=True
   ```

   Replace `XXXX` with a secure secret key.

5. **Generating a Django Secret Key**

   To generate a new Django secret key, you can use the following command in your terminal:

   ```
   python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
   ```
   Copy the generated key and replace `XXXX` in your `.env` file with this key.

6. **Run Migrations**
   
   Apply the database migrations to set up your database schema.

   ```
   python manage.py migrate
   ```

7. **Start the Development Server**

   Finally, you can start the Django development server to see EventHub in action.

   ```
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000` in your web browser to view the application.
