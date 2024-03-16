<h1>REMIND-ME-LATER PROJECT</h1>

RemindMeLater API is a Django-based RESTful API that allows clients to store, retrieve and update the data.

<h2>Features</h2>

<h3>1. Reminder CRUD Operations:</h3>

<dl>
<dt>Create Reminder:</dt> <dd>Clients can create new reminders by sending a POST request to the API endpoint.</dd>
<dt>Read Reminder(s):</dt> <dd>Clients can retrieve either a single reminder by its ID or all reminders by sending a GET request to the API endpoint.</dd>
<dt>Update Reminder:</dt> <dd>Clients can update an existing reminder by sending a PUT request with the updated data to the API endpoint.</dd>
<dt>Delete Reminder:</dt> <dd>Clients can delete an existing reminder by sending a DELETE request with the ID of the reminder to the API endpoint.</dd>
</dl>

<h3>2. Logging:</h3>

<ul>
<li>API requests and their outcomes are logged using the Python logging module.</li>
<li>Log messages include timestamps, log levels, thread names, module names, line numbers, and custom message content.</li>
</ul>

<h3>3. Request Handling:</h3>

<ul>
<li>The API view function reminder handles requests with methods GET, POST, PUT, and DELETE.</li>
<li>GET requests retrieve reminder data, POST requests create new reminders, PUT requests update existing reminders, and DELETE requests delete reminders.</li>
<li>The view function responds with appropriate HTTP status codes for different scenarios, such as success, failure, or invalid requests.</li>
</ul>

<h3>4. Error Handling:</h3>

<ul>
<li>Error conditions, such as missing records or invalid data, are appropriately handled, and corresponding HTTP status codes are returned to the client.</li>
<li>Error messages are logged for debugging purposes.</li>
</ul>

<h3>5. Serialization:</h3>
<ul>
<li>Reminder data is serialized using the ReminderDataSerializer class to convert between Django model instances and JSON representations.</li>
</ul>
These features collectively enable clients to interact with the RemindMeLater API to manage reminders efficiently.

<h2>Technologies Used</h2>
<li>Django: Backend web framework for building the API logic and handling HTTP requests.</li>
<li>Django REST Framework (DRF): Extension of Django for building RESTful APIs.</li>
<li>Docker: Containerization platform for packaging the API and its dependencies.</li>

<h2>Trying it Out</h2>
<ul>
<li>POST /api/reminder	Create a new user</li>
<li>GET /api/reminder	Get reminders details</li>
<li>GET /api/reminder/{id}	Get a single reminder details</li>
<li>PUT /api/reminder/{id}	Update a reminder details</li>
<li>DELETE /api/reminder/{id}	Delete a reminder</li>
</ul>

<h2>Getting Started</h2>

To run this API locally, follow these steps:

Clone the repository:

```
git clone https://github.com/Bhargavakkeni/Remind-Me-Later.git
```

Navigate to the project directory:

```
cd Remind-Me-Later
```

Run these commands one by one from root directory

```python
pip install -r requirements.txt
python manage.py migrate
python manage.py makemigrations
python manage.py runserver
```

<h3>Else</h3>

You can create a Docker image from the Dockerfile in the root directory.

Run this Docker command from root directory:
```
docker build -t remind-me-later .
```

Then create a container for this image by running this command:

```
docker run -p 8000:8000 remind-me-later
```


<h3>Adding PostgreSQL database:</h3>

You can add PostgreSQL database by adding this DATABASES settings to remind_me_later.settings file

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your_db_name',
        'USER' : 'your_user_name',
        'PASSWORD' : 'your_password',
        'HOST' : 'localhost'
    }
}
```
