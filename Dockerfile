# Use official Python image as base
FROM python:3.10-slim

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY danhtinhhoc/requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir gunicorn

# Copy source code
COPY danhtinhhoc/ ./danhtinhhoc/

# Set PYTHONPATH to include the danhtinhhoc directory
ENV PYTHONPATH=/app/danhtinhhoc

# Expose Flask port
EXPOSE 5000

# Run Flask app with gunicorn for production
# Change working directory to danhtinhhoc and run from there
WORKDIR /app/danhtinhhoc
CMD ["gunicorn", "-b", "0.0.0.0:5000", "-w", "4", "--timeout", "120", "gift:app"]