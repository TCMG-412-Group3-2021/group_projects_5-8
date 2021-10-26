 # Use an official Python runtime as a parent image
 FROM python:3.8-slim

 # Set the working directory to /app
 WORKDIR /app

 # Copy the current directory contents into the container at /app
 COPY . /app

 # Install any needed packages specified in requirements.txt
 RUN pip install --trusted-host pypi.python.org -r requirements.txt

 # Make port 80 available to the world outside this container
 EXPOSE 80

 # Define environment variable
 ENV NAME World
 ENV SLACK_BOT_TOKEN=xoxb-73266387591-2613282402611-TF0Mum0pEaqyEq9VA63r343A

 # Run app.py when the container launches  
 CMD ["python", "app.py"]
