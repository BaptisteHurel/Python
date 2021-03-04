#!/bin/bash

echo insert data into elasticsearch container 

curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/accounts/docs/_bulk --data-binary "@accounts.json"

printf "\n✅ Insertion account data to elastic node OK ✅ "

curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/movies/_bulk --data-binary "@movies.json"

printf "\n✅ Insertion movies data to elastic node OK ✅ "

curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/products/_bulk --data-binary "@products.json"

printf "\n✅ Insertion products data to elastic node OK ✅ "

curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/receipe/_bulk --data-binary "@receipe.json"

printf "\n✅ Insertion receipe data to elastic node OK ✅ "

curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/orders/_bulk --data-binary "@orders.json"

printf "\n✅ Insertion orders data to elastic node OK ✅ "
