### Models Download
* [HF/onelevelstudio/IMAGEN](https://huggingface.co/onelevelstudio/IMAGEN)
* [HF/onelevelstudio/VIDGEN](https://huggingface.co/onelevelstudio/VIDGEN)

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
