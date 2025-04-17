List IMG                        docker images
List CON                        docker ps -a

Build IMG                       docker-compose build
Run CON detached                docker-compose up -d
Build IMG + Run CON detached    docker-compose up -d --build
Stop CON + Remove CON           docker-compose down

Remove everything               1. docker stop $(docker ps -a -q)
                                2. docker rm -f $(docker ps -a -q)
                                3. docker rmi -f $(docker images -q)
                                4. docker volume rm -f $(docker volume ls -q)
                                5. docker network rm $(docker network ls -q)
                                6. docker system prune -a --volumes -f

Push to Docker Hub              1. docker login
                                2. docker tag imagelocal onelevelstudio/imagehub:tag01
                                3. docker push onelevelstudio/imagehub:tag01