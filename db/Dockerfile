FROM python:3-slim

WORKDIR /api

# Copy the db dir
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Setup an app user so the container doesn't run as root
RUN useradd -m app
USER app

# Start the api and expose the port where the api is running
CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "api:app" ]


