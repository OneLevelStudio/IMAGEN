# docker build -t forge-server .
# docker run -p 1234:1234 forge-server

FROM python:3.10.10-slim-bullseye
RUN apt-get update && apt-get install -y git

WORKDIR /WORKDIR

RUN git clone https://github.com/OneLevelStudio/FORGE .
RUN printf 'export COMMANDLINE_ARGS="--api --listen --port 1234"' >> webui-user.sh
EXPOSE 1234
CMD ["bash", "-c", "source webui.sh -f"]