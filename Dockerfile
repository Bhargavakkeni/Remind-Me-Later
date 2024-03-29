# Use an official Python runtime as a parent image
FROM python

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /code
COPY . /code/

# Run migrations
RUN python manage.py migrate


# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
