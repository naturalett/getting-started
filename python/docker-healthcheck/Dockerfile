FROM python:3.7-slim
WORKDIR /app
COPY expose.py requirements.txt ./
RUN pip install -r requirements.txt
CMD ["python","expose.py"]
