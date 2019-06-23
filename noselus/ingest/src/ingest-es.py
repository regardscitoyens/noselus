from elasticsearch import Elasticsearch
import csv
import json
import re
from datetime import datetime


es = Elasticsearch(['localhost'])

def ingest_one_file(filename, mandat_name, header):
    path = "../../../data/" +filename
    with open(path) as file:
        reader = csv.reader(file, delimiter='\t')

        dates = []
        idx_count = -1

        for row in header:
            if (re.search('Date', row)):
                dates.append(row)

        for row in reader:
            #ignore the header line
            if (idx_count < 0 ):
                idx_count = 0;
            else:
                #Fill header for first row
                doc = dict()
                doc['mandat'] = mandat_name
                pos = 0
                for field in row:
                    doc[header[pos]] = field
                    pos = pos +1
                for date in dates:
                    if (doc[date]):
                        doc[date] = datetime.strptime(doc[date], "%d/%m/%Y").strftime("%Y-%m-%d")

                idx_count = idx_count+1
                idx_str = "{}-{}".format(mandat_name,idx_count)
                res = es.index(index="mandat-idx", id=idx_str, body=doc)

                #print(res)
                if (idx_count%1000 == 0):
                    print("{} : {}".format(filename, idx_str))


ingest_one_file("1-rne-cm.txt", "cm", ["Code du département", "Libellé du département", "Code Insee de la commune", "Libellé de la commune", "Nom de l'élu", "Prénom de l'élu", "Code sexe", "Date de naissance", "Code profession", "Libellé de la profession", "Date de début du mandat", "Libellé de fonction", "Date de début de la fonction", "Nationalité de l'élu"])
ingest_one_file("2-rne-epci.txt", "epci", ["Code du département de l'EPCI", "N° SIREN", "Libellé de l'EPCI", "Code Insee de la commune", "Code du département", "Libellé de la commune", "Nom de l'élu", "Prénom de l'élu", "Code sexe", "Date de naissance", "Code profession", "Libellé de la profession", "Date de début du mandat", "Libellé de fonction", "Date de début de la fonction"])
ingest_one_file('3-rne-cd.txt', "cd", ["Code du département", "Libellé du département", "Nom de l'élu", "Prénom de l'élu", "Code sexe", "Code du canton", "Libellé du canton", "Libellé de fonction", "Code profession", "Libellé de la profession", "Date de naissance", "Date de début du mandat", "Date de début de la fonction"])
ingest_one_file("4-rne-cr.txt", "cr", ["Code région", "Libellé de la région", "Code du département", "Libellé du département", "Nom de l'élu", "Prénom de l'élu", "Code sexe", "Date de naissance", "Code profession", "Libellé de la profession", "Date de début du mandat", "Libellé de fonction", "Date de début de la fonction"])
ingest_one_file("5-rne-cac.txt", "cac", ["Code région", "Libellé de la région", "Nom de l'élu", "Prénom de l'élu", "Code sexe", "Date de naissance", "Code profession", "Libellé de la profession", "Date de début du mandat", "Libellé de fonction", "Date de début de la fonction"])
# ingest_one_file("6-rne-rpe.txt", "rpe", ["Code CirER", "Libellé CirER", "Nom de l'élu", "Prénom de l'élu", "Code sexe", "Date de naissance", "Code profession", "Libellé de la profession", "Date de début du mandat"])
ingest_one_file("7-rne-senateurs.txt", "senateurs", ["Code du département", "Libellé du département", "Nom de l'élu", "Prénom de l'élu", "Code sexe", "Date de naissance", "Code profession", "Libellé de la profession", "Date de début du mandat"])
ingest_one_file("8-rne-deputes.txt", "deputes", ["Code du département", "Libellé du département", "Code de la circonscription législative", "Libellé de la circonscription législative", "Nom de l'élu", "Prénom de l'élu", "Code sexe", "Date de naissance", "Code profession", "Libellé de la profession", "Date de début du mandat"])
ingest_one_file("9-rne-maires.txt", "maires", ["Code du département", "Libellé du département", "Code Insee de la commune", "Libellé de la commune", "Nom de l'élu", "Prénom de l'élu", "Code sexe", "Date de naissance", "Code profession", "Libellé de la profession", "Date de début du mandat", "Date de début de la fonction"])
