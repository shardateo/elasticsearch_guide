import elasticsearch
es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200

#deletes elasticsearch index (table), need to specify index name to delete index properly
es.indices.delete(index="tweet2", ignore=[400, 404])
print("File deleted")
