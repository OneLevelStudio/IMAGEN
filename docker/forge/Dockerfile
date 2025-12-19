# Python 3.11.14
FROM pytorch/pytorch:2.9.1-cuda12.8-cudnn9-runtime
RUN apt-get update && apt-get install -y --no-install-recommends git wget libgl1 libglib2.0-0 g++ && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /WORKDIR

# ====================================================================================================

RUN git clone --depth 1 --branch main "https://github.com/OneLevelStudio/FORGE" FORGE                                                      && \
    pip install --no-cache-dir -r FORGE/requirements_versions.txt                                                                          && \
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