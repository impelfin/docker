## fedora 

### fedora base fedora:latest

### Container execute		    
docker run -d -it --name fedora -p 8000:8000 -v /Users/lune/Documents/GitHub/docker/fedora:/app fedora 

### Container shell connection
docker exec -it fedora /bin/bash
