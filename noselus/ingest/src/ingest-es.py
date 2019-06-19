from elasticsearch import Elasticsearch
import csv
import json
from datetime import datetime


es = Elasticsearch(['localhost'])


def ingest_one_file(filename, mandat_name):
    path = "../../../data/" +filename 
    with open(path) as file:
        reader = csv.reader(file, delimiter='\t')

        header = []
        idx_count = 0

        for row in reader:
            #Fill header for first row
            if len(header) <= 0 :
                for field in row:
                    header.append(field)
            else :
                doc = dict()
                doc['mandat'] = mandat_name

                pos = 0
                for field in row:
                    doc[header[pos]] = field
                    pos = pos +1

                idx_count = idx_count+1
                idx_str = "{}-{}".format(mandat_name,idx_count)
                res = es.index(index="mandat-idx", id=idx_count, body=doc)

                #print(res)
                if (idx_count%1000 == 0):
                    print("{} : {}".format(filename, idx_str))


ingest_one_file("1-rne-cm.txt", "cm")
ingest_one_file("2-rne-epci.txt", "epci")
ingest_one_file('3-rne-cd.txt', "cd")
ingest_one_file("4-rne-cr.txt", "cr")
ingest_one_file("5-rne-cac.txt", "cac")
ingest_one_file("6-rne-rpe.txt", "rpe")
ingest_one_file("7-rne-senateurs.txt", "senateurs")
ingest_one_file("8-rne-deputes.txt", "deputes")
ingest_one_file("9-rne-maires.txt", "maires")
