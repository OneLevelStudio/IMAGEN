# FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04
# RUN apt-get update && apt-get install -y git wget python3 python3-pip python3-venv ffmpeg libsm6 libxext6 && apt-get clean && rm -rf /var/lib/apt/lists/*
# RUN ln -sf /usr/bin/python3 /usr/bin/python

# WORKDIR /WORKDIR

# RUN git clone https://github.com/OneLevelStudio/FORGE .
# # RUN printf 'export COMMANDLINE_ARGS="--api --listen --port 1234"' >> webui-user.sh

# RUN python3 -m venv venv
# RUN bash venv/bin/activate && pip install -U pip && pip install torch==2.3.1 torchvision==0.18.1 --extra-index-url https://download.pytorch.org/whl/cu121 && pip install -r requirements_versions.txt
# RUN wget -P models/Lora https://huggingface.co/onelevelstudio/diffusion/resolve/main/375993/LORA_GHOST.safetensors
# RUN wget -P models/Stable-diffusion https://huggingface.co/onelevelstudio/diffusion/resolve/main/573152/LVSTIFY_V5.0.safetensors

# EXPOSE 1234
# CMD ["bash", "-c", "source webui.sh -f"]




FROM pytorch/pytorch:2.3.1-cuda12.1-cudnn8-runtime
RUN apt-get update && apt-get install -y --no-install-recommends git wget libgl1 libglib2.0-0 && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /WORKDIR

RUN git clone https://github.com/OneLevelStudio/FORGE .
RUN printf 'venv_dir="-"' >> webui-user.sh

EXPOSE 1234
CMD ["bash", "webui.sh", "-f"]