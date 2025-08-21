FROM pytorch/pytorch:2.3.1-cuda12.1-cudnn8-runtime
RUN apt-get update && apt-get install -y --no-install-recommends git wget libgl1 libglib2.0-0 && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /WORKDIR

RUN git clone --depth 1 --branch main https://github.com/OneLevelStudio/FORGE .     && \
    printf 'venv_dir="-"' >> webui-user.sh                                          && \
    mkdir -p models/Lora && mkdir -p models/Stable-diffusion

RUN wget -P models/Stable-diffusion https://huggingface.co/onelevelstudio/IMAGEN/resolve/main/CHECKPOINT/LTF_V05.safetensors
RUN wget -P models/Stable-diffusion https://huggingface.co/onelevelstudio/IMAGEN/resolve/main/CHECKPOINT/WAI_V11.safetensors
RUN wget -P models/Stable-diffusion https://huggingface.co/onelevelstudio/IMAGEN/resolve/main/CHECKPOINT/MJX_V07.safetensors
RUN wget -P models/Lora             https://huggingface.co/onelevelstudio/IMAGEN/resolve/main/LORA/LORA_KoreaDL.safetensors
RUN wget -P models/Lora             https://huggingface.co/onelevelstudio/IMAGEN/resolve/main/LORA/LORA_JapanDL.safetensors
RUN wget -P models/Lora             https://huggingface.co/onelevelstudio/IMAGEN/resolve/main/LORA/LORA_TaiwnDL.safetensors
RUN wget -P models/Lora             https://huggingface.co/onelevelstudio/IMAGEN/resolve/main/LORA/LORA_ChinaDL.safetensors

EXPOSE 1234
CMD ["bash", "webui.sh", "-f"]
