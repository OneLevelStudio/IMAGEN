# Python 3.11.14
FROM python:3.11.14-slim
RUN apt-get update && apt-get install -y --no-install-recommends git wget libgl1 libglib2.0-0 g++ && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /WORKDIR
# ====================================================================================================
RUN pip install --no-cache-dir -q torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN git clone --depth 1 --branch main "https://github.com/OneLevelStudio/FORGE" FORGE                                                      && \
    pip install --no-cache-dir -r FORGE/requirements_versions.txt                                                                          && \
    echo 'export COMMANDLINE_ARGS="$COMMANDLINE_ARGS --always-cpu --skip-torch-cuda-test --use-cpu all --no-half --precision full"' >> FORGE/webui-user.sh     && \
    echo 'venv_dir="-"' >> FORGE/webui-user.sh
RUN pip install --no-cache-dir -q svglib==1.5.1 insightface==0.7.3
RUN mkdir -p FORGE/models/RealESRGAN && mkdir -p FORGE/models/GFPGAN                                                                       && \
    wget -P FORGE/models/RealESRGAN "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth"                && \
    wget -P FORGE/models/RealESRGAN "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.2.4/RealESRGAN_x4plus_anime_6B.pth"     && \
    wget -P FORGE/models/GFPGAN     "https://github.com/xinntao/facexlib/releases/download/v0.1.0/detection_Resnet50_Final.pth"            && \
    wget -P FORGE/models/GFPGAN     "https://github.com/xinntao/facexlib/releases/download/v0.2.2/parsing_parsenet.pth"                    && \
    wget -P FORGE/models/GFPGAN     "https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth"                         && \
    mkdir -p FORGE/extensions && mkdir -p FORGE/models/Stable-diffusion && mkdir -p FORGE/models/Lora

# ====================================================================================================

EXPOSE 1234
CMD ["bash", "FORGE/webui.sh", "-f"]