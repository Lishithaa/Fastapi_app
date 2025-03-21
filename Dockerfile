FROM python

WORKDIR /main

# Copy the current directory contents into the container
COPY . /main

# Install dependencies 
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port 
EXPOSE 8000

# Start the application with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
