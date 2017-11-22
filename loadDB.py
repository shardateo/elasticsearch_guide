import elasticsearch
from elasticsearch.helpers import bulk

es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200

# this creates the index in ElasticSearch
# ignore 400 cause by IndexAlreadyExistsException when creating an index
es.indices.create(index='index', ignore=400)

#reading and loading data into array to port into database
file = open("files/SinglishGenericOut_unique.txt","r")
temp=file.read().splitlines()

singArray = []
for i in temp:
    singArray.append(i)
print(str(len(singArray)) + " rows found")
file.close()

#porting data into database
singArrayid=0
dataLoad = []
for x in singArray:
    dataLoad.append({"_index":'tweet2',"_type":'tweets', "id":singArrayid, 'tweet': x})
    singArrayid=singArrayid+1
    print(str(singArrayid) + " rows loaded")
bulk(es,dataLoad)

print("Loaded successfully")
