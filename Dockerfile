# This file tells Docker dependencies and configuration
# settings for the Python application.

# From the official Python image, version 3.12, slim variant...
FROM python:3.12-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

# Define default Flask environment variables.
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV PYTHONBUFFERED=1