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

<h3>4. Error Handling:</h3>

<li>Error conditions, such as missing records or invalid data, are appropriately handled, and corresponding HTTP status codes are returned to the client.</li>
<li>Error messages are logged for debugging purposes.</li>

<h3>5. Serialization:</h3>

<li>Reminder data is serialized using the ReminderDataSerializer class to convert between Django model instances and JSON representations.</li>

These features collectively enable clients to interact with the RemindMeLater API to manage reminders efficiently.

<h2>Technologies Used<h2>
<li>Django: Backend web framework for building the API logic and handling HTTP requests.</li>
<li>Django REST Framework (DRF): Extension of Django for building RESTful APIs.</li>
<li>Docker: Containerization platform for packaging the API and its dependencies.</li>