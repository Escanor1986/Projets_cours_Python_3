# The_Boredless_Tourist

## Construire l'image Docker: Une fois que vous avez créé votre Dockerfile et votre fichier Python, vous pouvez construire votre image Docker en exécutant la commande suivante dans le répertoire app :

- docker build -t my_python_app .

### Cela construira une image Docker nommée my_python_app à partir des instructions fournies dans le Dockerfile.

## Exécuter le conteneur Docker: Une fois que l'image est construite, vous pouvez exécuter un conteneur à partir de cette image en utilisant la commande suivante :

- docker run -it --name my_app_container my_python_app /bin/bash

### Cela démarrera un conteneur interactif basé sur votre image my_python_app et vous placera dans un terminal virtuel à l'intérieur du conteneur.
