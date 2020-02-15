FROM python:3.8.1
MAINTAINER mallycrip "migsking@naver.com"

ENV SECRET_KEY_BASE $SECRET_KEY_BASE
ENV SCARFS_PASSWORD $SCARFS_PASSWORD

COPY . .
WORKDIR .

RUN pip install -r requirements
ENTRYPOINT ["python", "production.py"]

EXPOSE 5000