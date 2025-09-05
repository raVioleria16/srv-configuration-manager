ARG PORT
# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .

# Install git to clone repositories if needed
RUN apt-get update && apt-get install -y git
# Install any needed packages specified in requirements.txt
RUN pip install --force-reinstall --no-cache-dir -r requirements.txt

# Copy the rest of the application's code to the working directory
COPY app/* ./

CMD uvicorn app:app --host 0.0.0.0 --port ${PORT}