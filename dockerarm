FROM resin/rpi-raspbian:stretch
LABEL maintainer=uberentwickelt
ENV name SwankyBot
ENV token null
RUN [ "cross-build-start" ]
RUN apt update \
 && apt install python3 python3-setuptools git \
 && git clone https://github.com/python-telegram-bot/python-telegram-bot --recursive \
 && cd python-telegram-bot \
 && python3 setup.py install \
 && rm -rf python-telegram-bot \
 && mkdir -p /bot \
 && git clone https://github.com/uberentwickelt/${name} /bot \
 && rm /bot/*.md /bot/docker*
RUN [ "cross-build-end" ]
ENTRYPOINT sh -c "python3 /bot/bot.py ${token}"
