0. git clone https://github.com/OneLevelStudio/IMAGEN
0. cd IMAGEN/docker
0. docker compose build --no-cache

### Docker Hub
1. docker login
2. docker tag docker-imagen onelevelstudio/imagen:latest
3. docker push onelevelstudio/imagen:latest

### Github GHCR
1. docker login ghcr.io -u baobuiquang -p <PUT_TOKEN_HERE>
  - Generate Token: https://github.com/settings/tokens/new > 90 days > write:packages
2. docker tag docker-imagen ghcr.io/onelevelstudio/imagen:latest
3. docker push ghcr.io/onelevelstudio/imagen:latest
