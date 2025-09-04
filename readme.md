### Models Download
* [FORGE](https://raw.githubusercontent.com/OneLevelStudio/IMAGEN/refs/heads/main/docker/forge/download_models.sh)
  ```
  wget https://raw.githubusercontent.com/OneLevelStudio/IMAGEN/refs/heads/main/docker/forge/download_models.sh && bash download_models.sh
  ```
* [COMFY](https://raw.githubusercontent.com/OneLevelStudio/IMAGEN/refs/heads/main/docker/comfy/download_models.sh)
  ```
  wget https://raw.githubusercontent.com/OneLevelStudio/IMAGEN/refs/heads/main/docker/comfy/download_models.sh && bash download_models.sh
  ```

### Build and push Docker images

```
0. git clone https://github.com/OneLevelStudio/IMAGEN
0. cd IMAGEN/docker
0. docker compose build --no-cache

# Docker Hub
1. docker login
2. docker tag docker-forge onelevelstudio/imagen:forge && docker tag docker-comfy onelevelstudio/imagen:comfy && docker tag docker-forge onelevelstudio/imagen:latest
3. docker push onelevelstudio/imagen:forge && docker push onelevelstudio/imagen:comfy && docker push onelevelstudio/imagen:latest

# Github GHCR
1. docker login ghcr.io -u baobuiquang -p <PUT_TOKEN_HERE>
  - Generate Token: https://github.com/settings/tokens/new > 90 days > write:packages
2. docker tag docker-forge ghcr.io/onelevelstudio/imagen:forge && docker tag docker-comfy ghcr.io/onelevelstudio/imagen:comfy && docker tag docker-forge ghcr.io/onelevelstudio/imagen:latest
3. docker push ghcr.io/onelevelstudio/imagen:forge && docker push ghcr.io/onelevelstudio/imagen:comfy && docker push ghcr.io/onelevelstudio/imagen:latest
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
