FROM python:slim-buster

RUN pip install --no-cache-dir pandas fsspec

RUN mkdir -p /app
COPY convert-qodana-to-codeclimate.py /app/
RUN chmod +x /app/convert-qodana-to-codeclimate.py

CMD ["/app/convert-qodana-to-codeclimate.py"]