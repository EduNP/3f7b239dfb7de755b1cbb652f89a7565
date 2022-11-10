FROM python:3

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ERP.py .
EXPOSE 6000
CMD [ "python", "ERP.py" ]