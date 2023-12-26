# Use Python 3.11.5 (based on Alpine 3.18)
FROM python:3.11.5-alpine3.18

# Set a working directory
WORKDIR /app

# Copy the requirements.txt and install
COPY requirements.txt .

# Install all the dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the rest of the stuff
COPY . .
