FROM python:3
WORKDIR /usr/src/flask-app
COPY . .
# --no cache-dir: reduces image size
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]