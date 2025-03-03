FROM python:3.12
COPY src/* ./src/
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python","./src/main.py"]
