# Python 3.11 - PyTorch 2.4.1 - CUDA 12.1 - cuDNN 9
FROM pytorch/pytorch:2.4.1-cuda12.1-cudnn9-runtime
RUN apt-get update && apt-get install -y --no-install-recommends git wget libgl1 libglib2.0-0 && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /WORKDIR

# ====================================================================================================

RUN git clone --depth 1 --branch main https://github.com/OneLevelStudio/FORGE FORGE     && \
    printf 'venv_dir="-"' >> FORGE/webui-user.sh                                        && \
    mkdir -p FORGE/models/Stable-diffusion && mkdir -p FORGE/models/Lora

# ====================================================================================================

EXPOSE 1234
CMD ["bash", "FORGE/webui.sh", "-f"]