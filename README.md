# noselus



## Import des données.

```
cd noselus
```

Maintenant, nous allons lancer les conteneurs pour elasticsearch et pour kibana

```
sudo docker-compose up -d
```

L'ingestion des données se fera à partir du repository [rne-history](https://github.com/regardscitoyens/rne-history) que nous allons récupérer en lancant le script suivant.

```
cd ingest/src
bash gather-from-rne-history.sh
```

Maintenant, il va falloir faire l'ingestion dans elasticsearch

### Installation des dépendances
```
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Lancement de l'ingestion

```
python ingest-es.py
```





