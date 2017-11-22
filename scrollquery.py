from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

#this is a faster way to query things out of elasticsearch, to query to check for results, use resultsChecker.
#this also allows querying past 10k results which is not possible to do when using resultsChecker

tweetArray = []
# Initialize the scroll
page = es.search(index='tweet2',doc_type='tweets',
    scroll='1m',
    size=50,
    body={
        "query": {"match_phrase": {"tweet": "something"}}
    })
sid = page['_scroll_id']
scroll_size = page['hits']['total']

# before you scroll, process your current batch of hits
for hit in page['hits']['hits']:
    # print(hit['_source']['tweet'])
    tweetArray.append(hit['_source']['tweet'])

# Start scrolling
while (scroll_size > 0):
    page = es.scroll(scroll_id=sid, scroll='50m')
    # Update the scroll ID
    sid = page['_scroll_id']

    # Get the number of results that we returned in the last scroll
    scroll_size = len(page['hits']['hits'])
    # print("scroll size: " + str(scroll_size))

    # Do something with the obtained page
    for hit in page['hits']['hits']:
        # print(hit['_source']['tweet'])
        tweetArray.append(hit['_source']['tweet'])

#output results into file
f = open("output/test.txt","w",encoding="utf8")
for readlines in tweetArray:
    f.writelines(str(readlines) + "\n")
f.close()