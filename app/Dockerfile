# Utilisez l'image Python officielle comme base
FROM python:3.9-slim

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le fichier contenant votre code Python dans le conteneur
COPY first_program.py .

# Installez les dépendances de votre application
# Si vous avez un fichier requirements.txt, vous pouvez l'utiliser pour installer les dépendances.
COPY requirements.txt .
RUN pip install -r requirements.txt

# Exposez le port si votre application écoute sur un port spécifique
EXPOSE 5000

# Commande pour exécuter votre application
CMD ["python", "first_program.py"]
