# mysql 

### mysql base mysql 

### Container execute		    
docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=1234 -v /Users/lune/Documents/GitHub/docker/mysql:/app --name=mysql mysql

### Container shell connection
docker exec -it mysql /bin/bash
