FROM pytorch/pytorch:2.4.1-cuda12.1-cudnn9-runtime
RUN apt-get update && apt-get install -y --no-install-recommends git wget libgl1 libglib2.0-0 g++ && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /WORKDIR

RUN git clone --depth 1 --branch neo "https://github.com/Haoming02/sd-webui-forge-classic" NEO                  && \
    echo 'venv_dir="-"' >> NEO/webui-user.sh                                                                    && \
    echo 'export COMMANDLINE_ARGS="--api --listen --port 1234"' >> NEO/webui-user.sh

COPY webui.sh NEO/

EXPOSE 1234
CMD ["bash", "NEO/webui.sh", "-f"]