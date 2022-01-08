FROM python:3.7-slim
WORKDIR /app
COPY expose.py requirements.txt ./
RUN pip install -r requirements.txt
CMD ["python","expose.py"]

# docker build -t docker-healthcheck .
# docker run -d -p 5000:5000 --name docker-healthcheck docker-healthcheck:latest