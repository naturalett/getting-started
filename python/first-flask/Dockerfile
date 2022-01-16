FROM python:3.8.10-slim
WORKDIR /app
COPY requirements.txt expose.py ./
RUN pip install -r requirements.txt
CMD ["python", "expose.py"]