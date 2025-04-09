# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the entire repository into the container
COPY . .

# Expose port 8000 so the container can serve the FastAPI app
EXPOSE 8000

# Command to run the FastAPI application.
# Since your main file is located in the src/ folder,
# we use "src.main:app" to point to the FastAPI instance in main.py.
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]