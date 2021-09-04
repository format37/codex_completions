FROM python:latest
WORKDIR /codex
COPY requirements.txt /codex
RUN pip3 install -r requirements.txt --no-cache-dir
COPY server.py /codex
ENTRYPOINT ["python3"]
CMD ["server.py"]

