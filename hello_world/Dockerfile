FROM ghcr.io/home-assistant/base:3.24

RUN apk add --no-cache python3

COPY server.py /server.py
COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
