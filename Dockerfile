FROM python:3.10

# Set the working directory
WORKDIR /wordle

COPY requirments.txt .
RUN pip install -r requirments.txt

# Copy your script to the container
COPY . .

# # Make the script executable
# RUN chmod +x /wordle.py

EXPOSE 8050
# Define the command to run when starting the container (optional)
CMD ["python3", "-m", "front"]

