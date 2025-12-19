# Python 3.11.14
FROM pytorch/pytorch:2.9.1-cuda12.8-cudnn9-runtime
RUN apt-get update && apt-get install -y --no-install-recommends git wget libgl1 libglib2.0-0 g++ && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /WORKDIR

# ====================================================================================================

RUN git clone --depth 1 --branch main "https://github.com/OneLevelStudio/FORGE" FORGE                                                      && \
    pip install -r FORGE/requirements_versions.txt                                                                                         && \
    echo 'venv_dir="-"' >> FORGE/webui-user.sh
RUN pip install -q svglib==1.5.1 insightface==0.7.3
RUN mkdir -p FORGE/models/RealESRGAN && mkdir -p FORGE/models/GFPGAN                                                                       && \
    wget -P FORGE/models/RealESRGAN "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth"                && \
    wget -P FORGE/models/RealESRGAN "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.2.4/RealESRGAN_x4plus_anime_6B.pth"     && \
    wget -P FORGE/models/GFPGAN     "https://github.com/xinntao/facexlib/releases/download/v0.1.0/detection_Resnet50_Final.pth"            && \
    wget -P FORGE/models/GFPGAN     "https://github.com/xinntao/facexlib/releases/download/v0.2.2/parsing_parsenet.pth"                    && \
    wget -P FORGE/models/GFPGAN     "https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth"                         && \
    mkdir -p FORGE/extensions && mkdir -p FORGE/models/Stable-diffusion && mkdir -p FORGE/models/Lora

# ====================================================================================================

RUN git clone --depth 1 --branch master "https://github.com/comfyanonymous/ComfyUI" COMFY                                                                 && \
    pip install -r COMFY/requirements.txt
RUN pip install -q opencv-python matplotlib gguf ftfy imageio-ffmpeg scikit-image diffusers accelerate pywavelets onnx onnxruntime-gpu
RUN mkdir -p COMFY/custom_nodes                                                                                                                           && \
    git clone --depth 1 --branch main "https://github.com/Comfy-Org/ComfyUI-Manager"                                COMFY/custom_nodes/Manager            && \
    git clone --depth 1 --branch main "https://github.com/cubiq/ComfyUI_essentials"                                 COMFY/custom_nodes/Essentials         && \
    git clone --depth 1 --branch main "https://github.com/cubiq/ComfyUI_IPAdapter_plus"                             COMFY/custom_nodes/IPAdapter          && \
    git clone --depth 1 --branch main "https://github.com/Fannovel16/comfyui_controlnet_aux"                        COMFY/custom_nodes/ControlNetAux      && \
    git clone --depth 1 --branch main "https://github.com/Fannovel16/ComfyUI-Frame-Interpolation"                   COMFY/custom_nodes/FrameInterpolation && \
    git clone --depth 1 --branch main "https://github.com/city96/ComfyUI-GGUF"                                      COMFY/custom_nodes/GGUF               && \
    git clone --depth 1 --branch main "https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite"                     COMFY/custom_nodes/VHS                && \
    git clone --depth 1 --branch main "https://github.com/ClownsharkBatwing/RES4LYF"                                COMFY/custom_nodes/RES4LYF            && \
    git clone --depth 1 --branch main "https://github.com/BigStationW/ComfyUi-Scale-Image-to-Total-Pixels-Advanced" COMFY/custom_nodes/ScaleImageAdv      && \
    git clone --depth 1 --branch main "https://github.com/kijai/ComfyUI-KJNodes"                                    COMFY/custom_nodes/KJNodes            && \
    git clone --depth 1 --branch main "https://github.com/kijai/ComfyUI-WanVideoWrapper"                            COMFY/custom_nodes/WanVideoWrapper    && \
    git clone --depth 1 --branch main "https://github.com/kijai/ComfyUI-segment-anything-2"                         COMFY/custom_nodes/SegmentAnything2   && \
    mkdir -p COMFY/models/diffusion_models && mkdir -p COMFY/models/text_encoders && mkdir -p COMFY/models/loras && mkdir -p COMFY/models/vae

# ====================================================================================================

EXPOSE 1234 4321
CMD ["bash", "-c", "bash FORGE/webui.sh -f & python3 COMFY/main.py --listen=0.0.0.0 --port=4321 & wait"]