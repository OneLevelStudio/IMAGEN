# Python 3.11 - PyTorch CPU
FROM python:3.11.11-slim
RUN apt-get update && apt-get install -y --no-install-recommends git wget libgl1 libglib2.0-0 && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /WORKDIR

# ====================================================================================================

RUN git clone --depth 1 --branch main https://github.com/OneLevelStudio/FORGE FORGE     && \
    echo 'venv_dir="-"' >> FORGE/webui-user.sh                                          && \
    echo 'export COMMANDLINE_ARGS="$COMMANDLINE_ARGS --skip-torch-cuda-test --use-cpu all --precision full"' >> FORGE/webui-user.sh     && \
    mkdir -p FORGE/models/Stable-diffusion && mkdir -p FORGE/models/Lora

# ====================================================================================================

EXPOSE 1234
CMD ["bash", "FORGE/webui.sh", "-f"]