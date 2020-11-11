# blue-origin-x-20-21-soa-20-21-f
* Auteurs: **Team F**
    * AINADOU Florian
    * DJEKINOU Paul-Marie
    * KOFFI Paul
    * NABAGOU Djotiham
* Version actuelle : DELIVERY-FINAL
* Livrables :
    * [delivery-first](https://github.com/pns-si5-soa/box-20-21-team-f/releases/tag/delivery-first) : Première livraison
    * [delivery-final](https://github.com/pns-si5-soa/box-20-21-team-f/releases/tag/delivery-final) : Livraison finale
* Statuts d'Intégration continue : ![CI Build](https://github.com/pns-si5-soa/box-20-21-team-f/workflows/CI/badge.svg?branch=master)
  
# Vue d'ensemble
 Cette étude de cas est utilisée pour illustrer les différentes technologies impliquées dans le cours d'Architecture Orienté Services (SOA) donné à Polytech Nice - Sophia Antipolis en 5e année. Ce code de démonstration nécessite les technologies suivantes pour fonctionner correctement :
       
   * Environnement de déploiement : Docker 2.2.0.5 (Stable)
   * Langage d'implémentation Python & Pip : Python3 & Pip3
   
   
  ## Vision du produit
  La dernière version du produit à implémenter est décrite  [ici](./docs/scope_final.pdf).
    
  L'architecture logicielle à développer dans ce projet est incrémentale et évolue tout le long du projet.
  
  Le schéma final d'architecture se présente comme suit : 
  <p align="center">
      <img src="./docs/final_architecture.png"/>
  </p>
  
 ## Rapport du projet
 Le rapport final du projet se trouve 👉 [ici](./docs/rapport-delivery-final.pdf)
 
 PS : 
 * Toutes les images et illustrations utilisées dans ce rapport et dont les dimensions sont réduites en raison du format A4, sont disponibles en taille *réelle* dans le répertoire [docs](./docs) à la racine de ce projet.
 * S'assuer d'être bien authentifié sur github (ou d'avoir les droits sur le repo) si accès aux images directement depuis les liens inscrits dans le rapport (en légende des figures).
 * Le rapport du livrable *delivery-first* est également disponible 👉 [ici](./docs/rapport-delivery-first.pdf)
 
 
  
  ## Comment utiliser ce repository
  * La branche `master` (la branche par défaut) représente la dernière version stable du système.
  * La branche `develop` représente le système en cours de développement en parallèle des autres branches de développement spécifiques à des problématiques ou relatifs aux diverses tâches attribuées.
  * Les issues peuvent être créés en utilisant le [système de ticket de Github](https://github.com/pns-si5-soa/blue-origin-x-20-21-soa-20-21-f/issues)
  
  ### Récupération du projet
  Effectuer un clone classique du projet en faisant ```git clone https://github.com/pns-si5-soa/box-20-21-team-f.git``` ou en récupérant le zip depuis cette page.
  
  ## Compilation & Exécution  
  La compilation et l'exécution s'effectuent via des conteneurs *Docker* correspondants aux différents micro-services et autres acteurs du système.
  Le lancement et démarrage de ces conteneurs est automatisé grace à l'exécution de scripts.
     
  1- Exécuter le fichier [prepare.sh](./prepare.sh) à la racine du projet afin de compiler et exécuter toutes les images docker.
  
  PS : 
  
    - La première fois, la compilation et exécution (prepare.sh) peut prendre du temps en raison du téléchargement des images docker.
   
  2- Exécuter le fichier [run.sh](./run.sh) pour lancer les scénarios et tests d'acceptance.  
  
  <p align="center">
    <img src="./docs/prepare.jpg"/>
  </p>

  <p align="center">
    <img src="./docs/run.jpg"/>
  </p>
  
  Vous pouvez vous rendre dans la partie github Actions pour voir en détail l'exécution du prépare et des tests.
  
  ### Auto-évaluation du travail réalisé
  
  Avec une bonne base d'architecture dès les 2 premier scopes, nous avons démarré le projet sur les bons rails. Au fur et à mesure que nous
  recevions de nouvelles User Story, nous avons toujours isolé les blocs de fonctionnalités dans des petits services pour éviter un fort couplage. Cette démarche 
  nous a certes conduit à un grand nombre de microservices mais ce découpage très fin nous a permis d'intégrer kafka très facilement. Au final, nous n'avons pas vraiment eut
  un gros blocage technique. Notre seul regret reste la migration de nos services nodeJS vers python dûe à la latence des consumers node. On aurait bien aimer continuer avec
  les 2 technos. 
  
  Nous avons également tirer leçon des erreurs de notre premier rendu qui concernait plus l'exécution du projet lui même que la solution
  proposée.
    
  Chaque membre du groupe s’est sérieusement impliqué dans ce projet. De ce fait, nous nous répartissons les 400 points de la façon suivante :
    
  Florian AINADOU : ```100 points```
    
  Djotiham NABAGOU : ```100 points```
    
  Paul KOFFI  : ```100 points```
    
  Paul-Marie DJEKINNOU : ```100 points```
  
  ## Pile technologique
  
  <p align="center">
    <img src="./docs/stack.jpg"/>
  </p>
