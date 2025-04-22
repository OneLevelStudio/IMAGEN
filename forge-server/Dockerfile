FROM pytorch/pytorch:2.3.1-cuda12.1-cudnn8-runtime
RUN apt-get update && apt-get install -y --no-install-recommends git wget libgl1 libglib2.0-0 && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /WORKDIR

RUN git clone --depth 1 --branch main https://github.com/OneLevelStudio/FORGE .                                                  && \
    printf 'venv_dir="-"' >> webui-user.sh                                                                                       && \
    wget -P models/Lora https://huggingface.co/onelevelstudio/diffusion/resolve/main/000000/LORA_GHXST_V1.safetensors            && \
    wget -P models/Stable-diffusion https://huggingface.co/onelevelstudio/diffusion/resolve/main/573152/LVSTIFY_V5.0.safetensors

EXPOSE 1234
CMD ["bash", "webui.sh", "-f"]