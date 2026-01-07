### Models Download
* [HF/onelevelstudio/IMAGEN](https://huggingface.co/onelevelstudio/IMAGEN/blob/main/README.md)
* [HF/onelevelstudio/VIDGEN](https://huggingface.co/onelevelstudio/VIDGEN/blob/main/README.md)
```
wget -P COMFY/models/text_encoders "https://huggingface.co/onelevelstudio/VIDGEN/resolve/main/SHARED/UMT5XXL.safetensors" && wget -P COMFY/models/vae "https://huggingface.co/onelevelstudio/VIDGEN/resolve/main/SHARED/W21_VAE.safetensors" && wget -P COMFY/models/clip_vision "https://huggingface.co/onelevelstudio/VIDGEN/resolve/main/SHARED/CLIPV_H.safetensors" && wget -P COMFY/models/loras "https://huggingface.co/onelevelstudio/VIDGEN/resolve/main/W22_ANI/W22_ANI_RELI.safetensors" && wget -P COMFY/models/loras "https://huggingface.co/onelevelstudio/VIDGEN/resolve/main/W22_ANI/W22_ANI_LX2V.safetensors" && wget -P COMFY/models/diffusion_models "https://huggingface.co/onelevelstudio/VIDGEN/resolve/main/W22_ANI/W22_ANI_FP8.safetensors"
```

### Build and push Docker images

New process:
```
git clone https://github.com/OneLevelStudio/IMAGEN
cd IMAGEN/docker
docker compose build --no-cache

docker push onelevelstudio/imagen:forge
docker push onelevelstudio/imagen:comfy
docker push onelevelstudio/imagen:remjx
docker push onelevelstudio/imagen:forge-cpu
docker push onelevelstudio/imagen:comfy-cpu
```
```
docker push onelevelstudio/imagen:remjx && docker push onelevelstudio/imagen:comfy-cpu && docker push onelevelstudio/imagen:forge-cpu && docker push onelevelstudio/imagen:comfy && docker push onelevelstudio/imagen:forge
```

Old process:
```
git clone https://github.com/OneLevelStudio/IMAGEN
cd IMAGEN/docker
docker compose build --no-cache

# Docker Hub
docker login
docker tag docker-forge onelevelstudio/imagen:forge && docker tag docker-comfy onelevelstudio/imagen:comfy && docker tag docker-remjx onelevelstudio/imagen:remjx && docker tag docker-remjx onelevelstudio/imagen:latest
docker push onelevelstudio/imagen:forge && docker push onelevelstudio/imagen:comfy && docker push onelevelstudio/imagen:remjx && docker push onelevelstudio/imagen:latest

# Github GHCR (Generate Token: https://github.com/settings/tokens/new > write:packages)
docker login ghcr.io -u baobuiquang -p <PUT_TOKEN_HERE>
docker tag docker-forge ghcr.io/onelevelstudio/imagen:forge && docker tag docker-comfy ghcr.io/onelevelstudio/imagen:comfy && docker tag docker-remjx ghcr.io/onelevelstudio/imagen:remjx && docker tag docker-remjx ghcr.io/onelevelstudio/imagen:latest
docker push ghcr.io/onelevelstudio/imagen:forge && docker push ghcr.io/onelevelstudio/imagen:comfy && docker push ghcr.io/onelevelstudio/imagen:remjx && docker push ghcr.io/onelevelstudio/imagen:latest
```
