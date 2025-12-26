# Python 3.11.14
FROM pytorch/pytorch:2.9.1-cuda12.8-cudnn9-runtime
RUN apt-get update && apt-get install -y --no-install-recommends git wget libgl1 libglib2.0-0 g++ && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /WORKDIR

# ====================================================================================================

RUN git clone --depth 1 --branch main "https://github.com/deepbeepmeep/Wan2GP" WANGP     && \
    pip install --no-cache-dir -r WANGP/requirements.txt

# ====================================================================================================

EXPOSE 7860
CMD ["python3", "WANGP/wgp.py"]