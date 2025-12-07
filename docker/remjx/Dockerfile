FROM pytorch/pytorch:2.4.1-cuda12.1-cudnn9-runtime
RUN apt-get update && apt-get install -y --no-install-recommends git wget libgl1 libglib2.0-0 && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /WORKDIR

# ====================================================================================================

RUN git clone --depth 1 --branch main https://github.com/OneLevelStudio/FORGE FORGE     && \
    printf 'venv_dir="-"' >> FORGE/webui-user.sh                                        && \
    mkdir -p FORGE/models/Stable-diffusion && mkdir -p FORGE/models/Lora

# ====================================================================================================

RUN pip install -q torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121                                                                 && \
    pip install -q opencv-python imageio-ffmpeg matplotlib scikit-image diffusers ftfy accelerate gguf onnx onnxruntime-gpu
# RUN git clone --depth 1 --branch master https://github.com/OneLevelStudio/COMFY COMFY                                                                            && \
RUN git clone --depth 1 --branch master https://github.com/comfyanonymous/ComfyUI COMFY                                                                            && \
    pip install -r COMFY/requirements.txt                                                                                                                          && \
    mkdir -p COMFY/custom_nodes                                                                                                                                    && \
    git clone --depth 1 --branch main https://github.com/Comfy-Org/ComfyUI-Manager                                COMFY/custom_nodes/ComfyUI-Manager               && \
    git clone --depth 1 --branch main https://github.com/rgthree/rgthree-comfy                                    COMFY/custom_nodes/rgthree-comfy                 && \
    git clone --depth 1 --branch main https://github.com/cubiq/ComfyUI_essentials                                 COMFY/custom_nodes/ComfyUI_essentials            && \
    git clone --depth 1 --branch main https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite                     COMFY/custom_nodes/ComfyUI-VideoHelperSuite      && \
    git clone --depth 1 --branch main https://github.com/Fannovel16/comfyui_controlnet_aux                        COMFY/custom_nodes/comfyui_controlnet_aux        && \
    git clone --depth 1 --branch main https://github.com/Fannovel16/ComfyUI-Frame-Interpolation                   COMFY/custom_nodes/ComfyUI-Frame-Interpolation   && \
    git clone --depth 1 --branch main https://github.com/kijai/ComfyUI-WanVideoWrapper                            COMFY/custom_nodes/ComfyUI-WanVideoWrapper       && \
    git clone --depth 1 --branch main https://github.com/kijai/ComfyUI-KJNodes                                    COMFY/custom_nodes/ComfyUI-KJNodes               && \
    git clone --depth 1 --branch main https://github.com/kijai/ComfyUI-segment-anything-2                         COMFY/custom_nodes/ComfyUI-segment-anything-2    && \
    git clone --depth 1 --branch main https://github.com/city96/ComfyUI-GGUF                                      COMFY/custom_nodes/ComfyUI-GGUF                  && \
    git clone --depth 1 --branch main https://github.com/BigStationW/ComfyUi-Scale-Image-to-Total-Pixels-Advanced COMFY/custom_nodes/Scale-Image-Advanced          && \
    git clone --depth 1 --branch main https://github.com/ClownsharkBatwing/RES4LYF                                COMFY/custom_nodes/RES4LYF                       && \
    mkdir -p COMFY/models/diffusion_models && mkdir -p COMFY/models/text_encoders && mkdir -p COMFY/models/loras && mkdir -p COMFY/models/vae

# ====================================================================================================

EXPOSE 1234 4321
CMD ["bash", "-c", "bash FORGE/webui.sh -f & python3 COMFY/main.py --listen=0.0.0.0 --port=4321 & wait"]