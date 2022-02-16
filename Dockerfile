FROM python:3.11.0a5-alpine3.15

RUN mkdir -p /app
COPY convert-qodana-to-codeclimate.py /app/
RUN chmod +x /app/convert-qodana-to-codeclimate.py

WORKDIR /data

CMD ["python","/app/convert-qodana-to-codeclimate.py"]