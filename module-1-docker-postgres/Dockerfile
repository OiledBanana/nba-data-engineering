#BASE IMAGE
FROM python:3.13

#WORKDIR
WORKDIR /app

#COPY REQUIRMENTS.TXT
COPY requirements.txt .

#INSTALL DEPENDENCIES
RUN pip install --no-cache-dir -r requirements.txt

#COPY THE PROJECT
COPY . .

#ENTRY POINT
CMD ["python", "ingest.py"]




