# Python 3.11.14
FROM python:3.11.14-slim
RUN apt-get update && apt-get install -y --no-install-recommends git wget libgl1 libglib2.0-0 g++ && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /WORKDIR

# ====================================================================================================
RUN pip install --no-cache-dir -q torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN git clone --depth 1 --branch master "https://github.com/comfyanonymous/ComfyUI" COMFY                                                                 && \
    pip install --no-cache-dir -r COMFY/requirements.txt
RUN pip install --no-cache-dir -q opencv-python matplotlib gguf ftfy imageio-ffmpeg scikit-image diffusers accelerate pywavelets onnx onnxruntime-gpu rembg
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
    git clone --depth 1 --branch main "https://github.com/jags111/efficiency-nodes-comfyui"                         COMFY/custom_nodes/Efficiency         && \
    mkdir -p COMFY/models/diffusion_models && mkdir -p COMFY/models/text_encoders && mkdir -p COMFY/models/loras && mkdir -p COMFY/models/vae

# ====================================================================================================

EXPOSE 4321
CMD ["python3", "COMFY/main.py", "--cpu", "--listen=0.0.0.0", "--port=4321"]