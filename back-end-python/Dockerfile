FROM python:latest
RUN pip3 install websockets
COPY . /app
WORKDIR /app
EXPOSE 4000
CMD ["python3", "app.py"]