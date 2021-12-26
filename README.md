# Experimentation RORPO
Ce projet contient les codes sources et résulats des expérimentations du projet RORPO 

Code source du projet RORPO et rapport d'analyse sur nos expérimentations.
## Prérequis
Le projet doit être buildé avec CMake (version minimale : 2.8).    
Si vous ne l'avez pas installé, vous pouvez télécharger CMake ici : 
- [Windows](https://github.com/Kitware/CMake/releases/download/v3.22.1/cmake-3.22.1.zip)
- [Linux](https://github.com/Kitware/CMake/releases/download/v3.22.1/cmake-3.22.1.tar.gz)
- [Mac](https://github.com/Kitware/CMake/releases/download/v3.22.1/cmake-3.22.1-macos-universal.dmg)

Il faut également installer la librairie libpng.

Linux
```
sudo apt-get install libpng-dev
```
Mac
```
brew install libpng
```

Pour tester la feature de direction, il faut avoir le module scikit-image
```
pip install scikit-image 
```

## Utilisation

### Build
Pour compiler le code, il faut d'abord créer un dossier de build dans le repertoire du projet 
``` 
cd path/to/projet
mkdir build
```
Ensuite, on précompile le code, ce qui permet de générer un makefile:
```
cd build
cmake path/to/CMakeLists.txt
```
Enfin on compile le projet en exécutant 
```
make
```
Ceci génère un exécutable RORPO2D.

### Fonctionnement
L'exécutable RORPO2D s'utilise de la manière suivante : 
```
RORPO2D <imageEntree> <Lmin> <factorEchelle> <nbEchelles> <robutesse> <imageSortie>
```

## Exemples
Les exemples de l'article peuvent être testé avec les commandes suivantes:

Image Artificielle 
```
./RORPO2D synthetic_image.png 30 1 1 1 synthetic_image_RORPO_30_1_1_1.png
```

Image Rétine
```
./RORPO2D retinal_image.png 25 1.5 2 1 retinal_image_RORPO_25_1.5_2_1.png
```

Image fissure 
```
./RORPO2D cracks_image.png 10 1 1 1 cracks_image_RORPO_10_1_1_1.png
```

Pour tester la feature de direction, il faut remplacer les valeurs des paramètres par l'image et les résultats obtenus pour cette même image avec l'algorithme RORPO.
```
imageName = "./images/<imageEntree>.png"
rorpoIntensityName = "./results/<imageSortie>.png"
rorpoDirectionVxName = "./results/<imageSortie>_vx.png"
rorpoDirectionVyName = "./results/<imageSortie>_vy.png"
```


## Références
Le projet RORPO est un projet de recherche mené par : Odyssée Merveille, Benoit Naegel, Hugues Talbot, Laurent Najman, Nicolas Passat.


