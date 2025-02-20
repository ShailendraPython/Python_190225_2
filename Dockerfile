# Use the official Python 3.11 base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the source code into the container
COPY src/ .

COPY requirements.txt .

# Install dependencies if there's a requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

# Command to run the application (modify as needed)
CMD ["python", "app.py"]
