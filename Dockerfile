FROM ubuntu:latest
LABEL authors="Snake"

ENTRYPOINT ["top", "-b"]