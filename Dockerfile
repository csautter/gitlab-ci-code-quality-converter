FROM python:3.13.0rc1-alpine3.20

RUN mkdir -p /app
COPY convert-qodana-to-codeclimate.py /app/
RUN chmod +x /app/convert-qodana-to-codeclimate.py

WORKDIR /data

CMD ["python","/app/convert-qodana-to-codeclimate.py"]