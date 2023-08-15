FROM alpine:latest

RUN apk add py3-pip && pip3 install pygithub

COPY ./check_denylist.py /scripts/check_denylist.py

#Use volume to place /scripts/hotspots.txt
WORKDIR /scripts/

ENV PYTHONUNBUFFERED=true

CMD python3 /scripts/check_denylist.py
