FROM python:3.8-slim-buster

LABEL maintainer="Anil Pandey <anil.pande82@gmail.com>"

COPY requirements.txt ./app/

RUN apt-get -y update && apt-get reinstall openssl
RUN pip3 install -r /app/requirements.txt

COPY container/llm /app/llm

WORKDIR /app

ENTRYPOINT ["python3", "-u", "-m", ""]