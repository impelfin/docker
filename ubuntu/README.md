## ubuntu

### ubuntu base ubuntu:latest

### Container execute		    
docker run -d -it --name ubuntu -p 8000:8000 -v /Users/lune/Documents/GitHub/docker/ubuntu:/app ubuntu

### Container shell connection
docker exec -it ubuntu /bin/bash
