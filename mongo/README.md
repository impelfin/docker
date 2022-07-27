# mongo

### mongo base mongo

### Container execute		    
docker run -d -p 27017:27017 -v /Users/lune/Documents/GitHub/docker/mongo/:/app -v /Users/lune/Documents/GitHub/docker/mongo/data:/data/db --name=mongo mongo

### Container shell connection
docker exec -it mongo /bin/bash

## Compass connection address
mongodb://localhost:27017
