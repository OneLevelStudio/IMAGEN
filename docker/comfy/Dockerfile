FROM pytorch/pytorch:2.3.1-cuda12.1-cudnn8-runtime
RUN apt-get update && apt-get install -y --no-install-recommends git wget libgl1 libglib2.0-0 && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /WORKDIR

RUN pip install -q torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# RUN git clone --depth 1 --branch master https://github.com/comfyanonymous/ComfyUI COMFY                                                      && \
RUN git clone --depth 1 --branch master https://github.com/OneLevelStudio/COMFY COMFY                                                        && \
    pip install -r COMFY/requirements.txt                                                                                                    && \
    mkdir -p COMFY/custom_nodes                                                                                                              && \
    git clone https://github.com/Comfy-Org/ComfyUI-Manager COMFY/custom_nodes/ComfyUI-Manager                                                && \
    git clone https://github.com/rgthree/rgthree-comfy COMFY/custom_nodes/rgthree-comfy                                                      && \
    git clone https://github.com/Fannovel16/ComfyUI-Frame-Interpolation COMFY/custom_nodes/ComfyUI-Frame-Interpolation                       && \
    mkdir -p COMFY/models/diffusion_models && mkdir -p COMFY/models/text_encoders && mkdir -p COMFY/models/loras && mkdir -p COMFY/models/vae

EXPOSE 4321
CMD ["python3", "COMFY/main.py", "--listen=0.0.0.0", "--port=4321"]
