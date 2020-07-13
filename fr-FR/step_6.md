## Ajouter une boucle

Plutôt que d'exécuter ton programme encore et encore en appuyant sur <kbd>F5</kbd>, tu peux ajouter une boucle pour qu'elle continue de s'exécuter.

+ Tu peux utiliser le module `sleep` pour mettre en pause le programme entre les pixels. Pour ce faire, ajoute d'abord un autre `import` en haut de ton fichier.

```python
from time import sleep
```

+ Ajoute une boucle infinie sur la ligne sous les instructions `import`.

[[[generic-python-while-true]]]

+ Indente toutes les lignes de code contenant tes variables et `set_pixel` afin qu'elles soient dans la boucle :

--- hints ---
 --- hint ---

Une boucle infinie continuera à exécuter le code à l'intérieur indéfiniment. Voici le code pour commencer une boucle infinie. N'oublie pas que `True` doit avoir un `T` en lettre capital.

```python
while True:
```

--- /hint ---

--- hint ---

Voici à quoi devrait ressembler ton code :

```python
while True:
    x = randint(0, 7)
    y = randint(0, 7)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    sense.set_pixel(x, y, r, g, b)
```

--- /hint ------ /hints ---

+ Ajoute une ligne de code en bas de ton programme pour mettre en pause pendant 0,1 seconde. Assure-toi que cette ligne est en retrait avec la ligne `set_pixel` pour montrer qu'elle est à l'intérieur de la boucle.

[[[generic-python-sleep]]]


+ Exécute le code, et tu devrais voir des scintillements aléatoires en action !

![Résultat final](images/finished-result.gif)
