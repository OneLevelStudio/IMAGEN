FROM pytorch/pytorch:2.3.1-cuda12.1-cudnn8-runtime
RUN apt-get update && apt-get install -y --no-install-recommends git wget libgl1 libglib2.0-0 && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /WORKDIR

RUN git clone --depth 1 --branch main https://github.com/OneLevelStudio/FORGE .                                                                       && \
    printf 'venv_dir="-"' >> webui-user.sh                                                                                                            && \
    mkdir -p models/Lora && mkdir -p models/Stable-diffusion                                                                                          && \
    wget -O models/Stable-diffusion/WAI_V11.0.safetensors https://huggingface.co/onelevelstudio/IMAGEN/resolve/main/CHECKPOINT/WAI_V11.0.safetensors
    
    # wget -O models/Stable-diffusion/HSK_V2.2.safetensors https://huggingface.co/onelevelstudio/IMAGEN/resolve/main/CHECKPOINT/HSK_V2.2.safetensors    && \
    # wget -O models/Stable-diffusion/JNK_V4.0.safetensors https://huggingface.co/onelevelstudio/IMAGEN/resolve/main/CHECKPOINT/JNK_V4.0.safetensors    && \
    # wget -O models/Stable-diffusion/NVA_V8.0.safetensors https://huggingface.co/onelevelstudio/IMAGEN/resolve/main/CHECKPOINT/NVA_V8.0.safetensors    && \
    # wget -O models/Stable-diffusion/PRF_V1.0.safetensors https://huggingface.co/onelevelstudio/IMAGEN/resolve/main/CHECKPOINT/PRF_V1.0.safetensors    && \
    # wget -O models/Stable-diffusion/WAI_V11.0.safetensors https://huggingface.co/onelevelstudio/IMAGEN/resolve/main/CHECKPOINT/WAI_V11.0.safetensors  && \
    # wget -O models/Stable-diffusion/WAI_V14.0.safetensors https://huggingface.co/onelevelstudio/IMAGEN/resolve/main/CHECKPOINT/WAI_V14.0.safetensors

    # wget -O models/Stable-diffusion/MODEL.safetensors https://huggingface.co/onelevelstudio/diffusion/resolve/main/827184/WAI_V14.0.safetensors
    # wget -O models/Lora/LORA_V1.safetensors https://huggingface.co/onelevelstudio/diffusion/resolve/main/000000/LORA_GHXST_V1.safetensors          && \
    # wget -O models/Lora/LORA_V2.safetensors https://huggingface.co/onelevelstudio/diffusion/resolve/main/000000/LORA_GHXST_V2.safetensors          && \
    # wget -O models/Lora/LORA_V3.safetensors https://huggingface.co/onelevelstudio/diffusion/resolve/main/000000/LORA_GHXST_V3.safetensors          && \
    # wget -O models/Lora/LORA_V4.safetensors https://huggingface.co/onelevelstudio/diffusion/resolve/main/000000/LORA_GHXST_V4.safetensors          && \
    # wget -O models/Stable-diffusion/MODEL.safetensors https://huggingface.co/onelevelstudio/diffusion/resolve/main/573152/LVSTIFY_V5.0.safetensors

EXPOSE 1234
CMD ["bash", "webui.sh", "-f"]