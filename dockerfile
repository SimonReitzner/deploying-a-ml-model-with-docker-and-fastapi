# Use/extend python3.9-slim-buster image
FROM python:3.9-slim-buster

# Copy requirements.txt, main.py and the example_model.pkl
COPY ./requirements.txt .
COPY ./main.py .
COPY ./example_model.pkl .

# Install python dependencies
RUN pip install -r requirements.txt

# Start app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]