FROM pytorch/pytorch:2.3.1-cuda12.1-cudnn8-runtime
RUN apt-get update && apt-get install -y --no-install-recommends git wget libgl1 libglib2.0-0 && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /WORKDIR

RUN pip install -q torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

RUN git clone --depth 1 --branch master https://github.com/comfyanonymous/ComfyUI COMFY       && \
    pip install -r COMFY/requirements.txt                                                     && \
    mkdir -p COMFY/custom_nodes                                                               && \
    git clone https://github.com/Comfy-Org/ComfyUI-Manager COMFY/custom_nodes/comfyui-manager

# RUN git clone https://github.com/Comfy-Org/ComfyUI-Manager COMFY/custom_nodes/comfyui-manager

# RUN wget -P COMFY/models/diffusion_models https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors
# RUN wget -P COMFY/models/diffusion_models https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors
# RUN wget -P COMFY/models/text_encoders    https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors
# RUN wget -P COMFY/models/loras            https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors
# RUN wget -P COMFY/models/loras            https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors
# RUN wget -P COMFY/models/vae              https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors

EXPOSE 4321
CMD ["python3", "COMFY/main.py", "--listen=0.0.0.0", "--port=4321"]
