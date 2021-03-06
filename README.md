# IP5 - Metriken im Bauwesen
**Team:** Luca Dietiker & Ralf Winkelmann

### Auftraggeber
Das Projekt «Flächenmetriken im Bauwesen» wurde von der Kennwerte AG mit Sitz in Brugg AG bei der FHNW eingereicht. 

### Beschreibung
Dieses Projekt beinhaltet die REST-Schnittstelle (FastAPI) für den Schätzer von Flächen Metriken. 

### Local
Lokal kann die API mithilfe von Uvicorn wie folgt genutzt werden

```bash
uvicorn app.main:app --reload
```

### Docker

Neues Docker-Image zu bauen
```bash
docker build -t metriken-bauwesen-api .
```

Docker-Image veröffentlichen
```bash
docker run --name metriken-bauwesen-container -p 8080:80 metriken-bauwesen-api
```

### Google Cloud

Create Docker images for Google Container Registry
```bash
gcloud builds submit --tag gcr.io/metriken-bauwesen-api/{container-name}
```

Deploy the container image
```bash
gcloud run deploy --image gcr.io/metriken-bauwesen-api/{container-name} --platform managed
```

### Installation

```bash
pip install -r requirements.txt
```
