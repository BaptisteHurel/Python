#!/bin/bash

docker run -d --name elasticsearch-container -v $(pwd)/elas1:/usr/share/elasticsearch/data -p 9200:9200 -p 9300:9300 -e "ELASTICSEARCH_HEAP_SIZE=128m" docker.elastic.co/elasticsearch/elasticsearch:7.11.1

printf "✅ Elastic Container OK ✅ \n"

docker ps 
