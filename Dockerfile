FROM thealifhaker1/userbot_docker:latest

ENV PATH="/app/bin:$PATH"
WORKDIR /app

RUN git clone https://github.com/THEALIFHAKER1/AE1-USERBOT.git -b master /app

COPY ./userbot.session ./config.env* ./client_secrets.json* ./secret.json* /app/

CMD ["bash","init/start.sh"]
