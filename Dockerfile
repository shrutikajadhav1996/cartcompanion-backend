# Use the official Python image from the Docker Hub
FROM python:3.9-slim

COPY . /app

# Set the working directory
WORKDIR /app

RUN apt-get update
RUN apt-get install -y default-libmysqlclient-dev build-essential
RUN apt-get install python3-distutils

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE $PORT

# Command to run the application
CMD gunicorn worker=4 0.0.0.0:$PORT app:app
