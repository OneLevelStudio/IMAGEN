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

### Models Download
* [FORGE](https://raw.githubusercontent.com/OneLevelStudio/IMAGEN/refs/heads/main/docker/forge/download_models.sh)
  ```
  wget https://raw.githubusercontent.com/OneLevelStudio/IMAGEN/refs/heads/main/docker/forge/download_models.sh && bash download_models.sh
  ```
* [COMFY](https://raw.githubusercontent.com/OneLevelStudio/IMAGEN/refs/heads/main/docker/comfy/download_models.sh)
  ```
  wget https://raw.githubusercontent.com/OneLevelStudio/IMAGEN/refs/heads/main/docker/comfy/download_models.sh && bash download_models.sh
  ```

### Download and upload to Huggingface

```
1. git clone https://github.com/OneLevelStudio/IMAGEN -> Open `upload.ipynb`
2. Select Python Kernel
3. Edit variables
  - CivitAI Token:
    + https://civitai.com/user/account > API Keys > Create and copy CivitAI API key
  - HF Write Token:
    + https://huggingface.co/settings/tokens > Create and copy Write Token
4. Run the notebook
5. Check https://huggingface.co/onelevelstudio/IMAGEN
```
