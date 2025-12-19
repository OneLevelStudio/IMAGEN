FROM pytorch/pytorch:2.9.1-cuda12.8-cudnn9-runtime
RUN apt-get update && apt-get install -y --no-install-recommends git wget libgl1 libglib2.0-0 g++ && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
WORKDIR /WORKDIR

RUN git clone --depth 1 --branch neo "https://github.com/OneLevelStudio/NEO" NEO                      && \
    echo 'venv_dir="-"'                                              >> NEO/webui-user.sh             && \
    echo 'export COMMANDLINE_ARGS="--api --listen --port 1234 --uv"' >> NEO/webui-user.sh             && \
    wget -P NEO "https://raw.githubusercontent.com/OneLevelStudio/FORGE/refs/heads/main/webui.sh"

EXPOSE 1234
CMD ["bash", "NEO/webui.sh", "-f"]