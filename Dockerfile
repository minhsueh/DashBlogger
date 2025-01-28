# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that the Dash app runs on
EXPOSE 8050

# Command to run the application
# CMD ["python", "-m", "dash_blogger.app"]

# Command to run Gunicorn and serve the app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8050", "dash_blogger.app:server"]