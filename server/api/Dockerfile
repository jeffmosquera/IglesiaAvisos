FROM python:3.7

RUN pip install fastapi uvicorn pymongo pytz

EXPOSE 5000
WORKDIR /app
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]