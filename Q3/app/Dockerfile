# Base image for the container, I used python:3.8-slim-buster as it used in docker docs tutorial.
# https://docs.docker.com/language/python/build-images/
FROM python:3.8-slim-buster

# Set the LABEL as it is a good practice.
LABEL image.authors="st123010@ait.asia"

# Set default location for all subsequent commands.
WORKDIR /app

# Copy working directory to the image.
COPY . /app

# Upgrade pip.
RUN python -m pip install --upgrade pip

# Install requirements files, use no cache as we want to keep docker image as small as possible.
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080, "main" module use 8000.
EXPOSE 8080

# CMD command to start uvicorn server.
# Main module named "main" and the FastAPI instance named "app".
# This images listening on port 8080 and accept connection from any ip addresses.
# Use --reload as this work run on the local machine.

CMD ["uvicorn", "convert_string:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]