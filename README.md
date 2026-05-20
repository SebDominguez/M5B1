# M5 -Brief 1 -Déployer un projet IA en architecture modulaire avec CI/CD

Dans ce projet, vous allez poser les bases d’une architecture moderne en séparant le frontend et le backend, en dockerisant les composants, en définissant une logique de calcul simple, et en préparant le projet pour une intégration continue. Ce template servira de socle aux futurs projets déployés.

### Référentiels
Compétences transversales

### Ressources
- ./ressources/opco-atlas-docker-compose.docx
- ./ressources/opco-atlas-github-actions-ci.pdf

### Contexte du projet
FastIA souhaite mettre en place une architecture de base pour ses projets IA.

L’objectif est d’avoir un frontend utilisateur simple, une API FastAPI bien structurée, un environnement conteneurisé avec Docker et une automatisation des tests via GitHub Actions.

**Cette architecture servira de modèle reproductible pour tous les futurs projets de déploiement.**

L'équipe MLOps vous confie donc la mission de créer un template minimaliste, facilement extensible, conforme aux bonnes pratiques d’ingénierie logicielle.

Vos tâches seront de :

- structurer le dépôt de code et versionner le code.
- préparer un script de déploiement de l’API (FastAPI).
- connecter les différentes étapes de test, déploiement, mise à jour et suivi à travers une chaîne CI/CDD via GitHub Actions

Ce geste professionnel s’inscrit dans une logique d’amélioration continue, où les données évolutives, les retours métier et les performances du modèle sont pris en compte pour piloter les mises à jour futures.

### Modalités pédagogiques
Projet individuel. Les livrables doivent être versionnés dans un dépôt Git propre, organisé, avec un fichier README clair.

Les outils à utiliser sont :

- Streamlit pour le frontend
- FastAPI + Pydantic pour l’API
- Docker & Docker Compose pour l’environnement
- Loguru pour les logs
- pytest pour les tests backend
- GitHub + GitHub Actions pour l’intégration continue

**Contraintes techniques spécifiques :**

- Le champ du frontend envoie un entier vers une API REST.
- L’API retourne le carré de l’entier après validation du type.
- Le calcul se fait dans un fichier dédié modules/calcul.py.
- Le backend contient un dossier tests/ avec un test de cette fonction.
- Le Docker Compose ne doit lancer que le frontend et le backend.
- Aucune base de données n’est requise à ce stade.

Structure à respecter :
```txt
📁 frontend/
└── app.py (Streamlit + Loguru)
└── Dockerfile
📁 backend/
└── main.py (FastAPI avec 3 routes)
└── modules/calcul.py
└── tests/test\_calcul.py
└── Dockerfile
📄 docker-compose.yml
```


### Modalités d'évaluation
L’API répond bien aux 3 routes définies (/, /health, /calcul)
Le frontend affiche une UI simple et fonctionnelle
Le calcul est correct et validé via Pydantic
La structure du projet est propre et conforme
Le Docker Compose démarre sans erreur les deux services
Les logs sont lisibles et correctement intégrés via Loguru
Les tests pytest fonctionnent et couvrent la fonction calcul()
Un fichier .github/workflows/test.yml valide l’exécution des tests automatisés


### Livrables

Dépôt Git avec :
- frontend/app.py + Dockerfile
- backend/main.py, modules/calcul.py, tests/test_calcul.py, Dockerfile
- docker-compose.yml
- .github/workflows/test.yml

README.md décrivant l’architecture, les routes, les instructions de lancement


### Critères de performance
Le projet respecte les standards de développement MLOps (modularité, logs, tests, CI/CD)
L’environnement Docker est isolé, reproductible et bien configuré
La logique métier est découplée, testable, réutilisable
L’intégration continue fonctionne dès le push sur GitHub
Le code est clair, documenté, et facilement maintenable


dépot git https://github.com/SebDominguez/M5B1

---

## Architecture

```
frontend (Streamlit, port 8501)  ──POST /calcul──▶  backend (FastAPI, port 8000)
                                                    └── modules/calcul.py
```

## Routes API

| Méthode | Route     | Description                                |
|---------|-----------|--------------------------------------------|
| GET     | `/`       | Landing page                          |
| GET     | `/health` | Statut de l'API (`{"status": "ok"}`)       |
| POST    | `/calcul` | Retourne `{"result": n^2}` à partir de `{"value": n}` |

```bash
curl 127.0.0.1:8501
curl 127.0.0.1:8000/health
curl --json '{"value": 5}' 127.0.0.1:8000/calcul
```

## Lancement avec Docker

```bash
# sur macOS sans docker-engine installer colima (brew install colima) et executer : colima start
docker compose up --build
```


- Frontend : http://localhost:8501
- Backend  : http://localhost:8000 (docs : http://localhost:8000/docs)

## Lancement en local (sans Docker)

```bash
# Backend
cd backend
# activer au besoin un venv
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend (dans un autre terminal)
cd frontend
# venv stuff
pip install -r requirements.txt
streamlit run app.py
# pour avoir le reload --server.runOnSave true
```

## Tests

```bash
cd backend
pytest -v
```

Output :

```bash
========================== test session starts ==========================
platform darwin -- Python 3.12.13, pytest-9.0.3, pluggy-1.6.0 -- /Users/sebastien/M5B1/backend/.venv/bin/python3.12
cachedir: .pytest_cache
rootdir: /Users/sebastien/M5B1/backend
plugins: anyio-4.13.0
collected 3 items

tests/test_calcul.py::test_calcul_positive PASSED                 [ 33%]
tests/test_calcul.py::test_calcul_zero PASSED                     [ 66%]
tests/test_calcul.py::test_calcul_negative PASSED                 [100%]

=========================== 3 passed in 0.01s ===========================
```

Les tests sont également exécutés automatiquement à chaque push via GitHub Actions (`.github/workflows/test.yml`).

Tester les Actions:

avec `act`

```bash
# brew install act
act push
# sur macOS avec colima ajouter :
#act push --container-daemon-socket -
```


Brief-2:

Le contenu des test du brief 1 on ete copié dans le docker-publish.yml workflow

Pour eviter de polluer docker hub avec des build foireu on publish dans docker-hub uniquement si les test passent.

Avant de lancer le  workflow on peu verifier si les images build:

pour tester que les images build:


```bash
docker build -t m5b2-backend:test ./backend


docker build -t m5b2-backend:test ./frontend
```

**Note** : on peut aussi utiliser `buildx` vu que `docker build` est déprécié, et parce que tous les outils ont maintenant besoin d'un `x` en suffixe.

```bash
sur macos brew install docker-buildx
```

Vérifier que les conteneurs démarrent sans erreur :

```bash
docker compose up --build
```







