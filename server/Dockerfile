FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04
RUN apt-get update && apt-get install -y git wget python3 python3-pip python3-venv ffmpeg libsm6 libxext6 && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN ln -sf /usr/bin/python3 /usr/bin/python

WORKDIR /WORKDIR

RUN git clone https://github.com/OneLevelStudio/FORGE .
RUN printf 'export COMMANDLINE_ARGS="--api --listen --port 1234"' >> webui-user.sh
RUN wget -P models/Stable-diffusion https://huggingface.co/onelevelstudio/diffusion/resolve/main/573152/LVSTIFY_V5.0.safetensors
RUN wget -P models/Lora https://huggingface.co/onelevelstudio/diffusion/resolve/main/375993/LORA_GHOST.safetensors

EXPOSE 1234
CMD ["bash", "-c", "source webui.sh -f"]