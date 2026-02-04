FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port for Flask
EXPOSE 5000

# Command to run the application (assuming app.py has a run block or using flask run)
CMD ["python", "src/app.py"]
