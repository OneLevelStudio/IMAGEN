FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04
RUN apt-get update && apt-get install -y git python3 python3-pip python3-venv ffmpeg libsm6 libxext6
RUN ln -sf /usr/bin/python3 /usr/bin/python

WORKDIR /WORKDIR

RUN git clone https://github.com/OneLevelStudio/FORGE .
RUN printf 'export COMMANDLINE_ARGS="--api --listen --port 1234"' >> webui-user.sh
EXPOSE 1234
# RUN bash -c "source webui.sh -f"
CMD ["bash", "-c", "source webui.sh -f"]