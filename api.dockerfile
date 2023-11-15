FROM python:3.10.2-bullseye

RUN useradd -ms /bin/bash dev

USER dev

WORKDIR /home/dev

EXPOSE 8000