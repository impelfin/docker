# mongo 

### mongo base mongo 

### Container execute		    
docker run -d -p 27017:27017 -v /Users/lune/Documents/GitHub/docker/mongo:/db --restart always --name=mongo mongo --auth 

### Container shell connection
docker exec -it mongo /bin/bash
