# Use the official Python image from Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir streamlit

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "calculator.py", "--server.port=8501", "--server.address=0.0.0.0"]
