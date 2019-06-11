from elasticsearch import Elasticsearch
import csv
import json
from datetime import datetime


es = Elasticsearch(['localhost'])

with open('../../../data/1-rne-cm.txt') as maire_file:
    reader = csv.reader(maire_file, delimiter='\t')

    header = []
    idx_count = 0

    for row in reader:
        #Fill header for first row
        if len(header) <= 0 :
            for field in row:
                header.append(field)
        else :
            doc = dict()
            pos = 0
            for field in row:
                doc[header[pos]] = field
                pos = pos +1

            idx_count = idx_count+1
            res = es.index(index="mandat-idx", id=idx_count, body=doc)

            #print(res)
            if (idx_count%1000 == 0):
                print(idx_count)



exit()
SystemExit()




es = Elasticsearch(['localhost'])

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}

print(type(doc))

res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
print(res['result'])

res = es.get(index="test-index", doc_type='tweet', id=1)
print(res['_source'])

es.indices.refresh(index="test-index")

res = es.search(index="test-index", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])





