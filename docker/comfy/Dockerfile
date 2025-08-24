FROM pytorch/pytorch:2.3.1-cuda12.1-cudnn8-runtime
RUN apt-get update && apt-get install -y --no-install-recommends git wget libgl1 libglib2.0-0 && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /WORKDIR

RUN pip install -q torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

RUN git clone --depth 1 --branch master https://github.com/comfyanonymous/ComfyUI COMFY     && \
    pip install -r COMFY/requirements.txt

EXPOSE 4321
CMD ["python3", "COMFY/main.py", "--listen=0.0.0.0", "--port=4321"]