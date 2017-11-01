FROM alpine:latest
MAINTAINER 7265626F6F74
ENV name SwankyBot
ENV token null
RUN apk --update add python py-pip wget ca-certificates \
 && pip install --upgrade pip \
 && pip install python-telegram-bot \
 && wget -O /tmp/master.zip https://github.com/7265626F6F74/${name}/archive/master.zip \
 && mkdir -p /bot \
 && unzip -d /bot /tmp/master.zip \
 && rm /tmp/master.zip
ENTRYPOINT sh -c "python /bot/${name}-master/bot.py ${token}"
