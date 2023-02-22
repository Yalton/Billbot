#Bertbot (Dockerfile)
FROM python:3

WORKDIR #(pwd):/usr/src/app

RUN pip install -U discord.py

CMD [ "python", "./bot.py" ]
