FROM python:alpine

RUN mkdir -p /app
COPY convert-qodana-to-codeclimate.py /app/
RUN chmod +x /app/convert-qodana-to-codeclimate.py

CMD ["python","/app/convert-qodana-to-codeclimate.py"]