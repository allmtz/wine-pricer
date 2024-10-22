FROM python:3-slim

WORKDIR /api

# Copy the db dir
COPY . .

# Install dependencies
RUN pip install --no-cache-dir flask flask-cors

# Setup an app user so the container doesn't run as root
RUN useradd -m app
USER app

# Start the api
CMD [ "python", "/api/api.py" ]

