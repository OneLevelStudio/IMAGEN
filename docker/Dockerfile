FROM pytorch/pytorch:2.3.1-cuda12.1-cudnn8-runtime
RUN apt-get update && apt-get install -y --no-install-recommends git wget libgl1 libglib2.0-0 && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /WORKDIR

RUN git clone --depth 1 --branch main https://github.com/OneLevelStudio/FORGE .                                                                       && \
    printf 'venv_dir="-"' >> webui-user.sh                                                                                                            && \
    mkdir -p models/Lora && mkdir -p models/Stable-diffusion                                                                                          && \
    wget -O models/Stable-diffusion/LTF_V05.0.safetensors https://huggingface.co/onelevelstudio/IMAGEN/resolve/main/CHECKPOINT/LTF_V05.0.safetensors  && \
    wget -O models/Lora/LORA_XOUSX.safetensors https://huggingface.co/onelevelstudio/IMAGEN/resolve/main/LORA/LORA_XOUSX.safetensors                  && \
    # wget -O models/Stable-diffusion/WAI_V11.0.safetensors https://huggingface.co/onelevelstudio/IMAGEN/resolve/main/CHECKPOINT/WAI_V11.0.safetensors  && \
    echo ">>> Completed!"

EXPOSE 1234
CMD ["bash", "webui.sh", "-f"]