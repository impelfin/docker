## centos

### centos base dokken:centos-8

### Container execute		    
docker run -d -it --name centos -p 8000:8000 -v /Users/lune/Documents/GitHub/UNIX:/app centos 

### Container shell connection
docker exec -it centos /bin/bash
