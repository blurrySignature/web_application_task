FROM python:3.10-slim

ENV AUTHOR=blurrySignature

EXPOSE 8000

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

ENTRYPOINT ["python3", "web_application.py"]
