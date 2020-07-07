## Réglage des pixels au hasard

Tout d'abord, nous allons trouver des nombres aléatoires et utiliser la fonction `set_pixel` pour placer une couleur aléatoire sur un emplacement aléatoire sur l'écran Sense HAT.

+ Ouvre l'éditeur IDLE.

[[[rpi-gui-idle-opening]]]

+ Crée un nouveau fichier et enregistre-le en tant que `sparkles.py`.

+ Dans le nouveau fichier, commence par importer le module `SenseHat` :

    ```python
    from sense_hat import SenseHat
    ```

+ Ensuite, crée une connexion à ton Sense HAT en ajoutant cette ligne de code :

    ```python
    sense = SenseHat()
    ```


Nous allons alors définir x et y pour choisir quel pixel sur le Sense HAT va éclairer.

+ Crée une variable appelée `x`, et définis-la comme égale à un nombre de ton choix entre 0 et 7. Ce sera la coordonnée x de ton pixel sur l'écran. [[[generic-python-creating-a-variable]]]

+ Crée une autre variable appelée `y`, et définis-la comme égale à un autre nombre entre 0 et 7. Ce sera la coordonnée y de ton pixel à l'écran.


+ Pour choisir la couleur de ton pixel, pense à trois nombres entre 0 et `255`, puis attribue-les aux variables appelées `r`, `g`, et `b`. Ces variables représenteront la couleur de ton pixel comme des quantités de rouge (r), de vert (g), et de bleu (b).


+ Utilise maintenant la fonction `set_pixel` pour placer un pixel avec ta couleur choisie aléatoirement à l'emplacement choisi sur l'écran.

**Remarque :** les directions réductibles ci-dessous utilisent un nom de fichier différent du tien et utilisent Trinket au lieu de IDLE.

[[[rpi-sensehat-single-pixel]]]

La méthode `set_pixel` prend des données dans l'ordre suivant : coordonnée x, coordonnée y, rouge, vert, bleu

Pour définir ta méthode `set_pixel`, mets les noms de tes variables en points d'interrogation de cette ligne de code, dans le bon ordre : coordonnée x, coordonnée y, rouge, vert, bleu.

```python
sense.set_pixel(?, ?, ?, ?, ?)
```

Regarde l'indice ci-dessous si tu es bloqué.

--- hints ---

--- hint ---

Voici à quoi devrait ressembler ton code fini — tu auras probablement choisi différents nombres :

![Solution de pixel aléatoire](images/random-pixel-solution.png)

--- /hint ---

--- /hints ---


+ Exécute ton code en appuyant sur <kbd>F5</kbd>. Tu devrais voir une seule LED s'allumer sur l'écran LED du Sense HAT.

+ Maintenant, change tous les nombres dans ton programme et exécute le programme à nouveau. Une seconde LED devrait s'allumer.
