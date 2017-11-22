from elasticsearch import Elasticsearch
from nltk.tokenize import TweetTokenizer, word_tokenize
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

#query method is limited to 10000 hits, use scrollquery to get results above 10000
#change "action against" to query other results out

tweetcheck = es.search(index='tweet2', doc_type='tweets',body={"size":10000,"query" : {"match_phrase" :{"tweet" : "action against"}}})

#prints length
print(tweetcheck['hits']['total'])

#prints results
tweets = []
for i in range(int(tweetcheck['hits']['total'])):
    t = tweetcheck['hits']['hits'][i]['_source']['tweet']
    print(t)
