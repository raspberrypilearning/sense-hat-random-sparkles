## Utiliser le module `random`

Jusqu'à présent, tu as choisi tes propres nombres aléatoires, mais tu peux laisser l'ordinateur les choisir à la place en utilisant le module `random`.

+ Ajoute une autre ligne `import` en **haut** de ton programme :

```python
from random import randint
```

+ Modifie tes variables `x` et `y` pour qu'elles soient égales à un nombre aléatoire entre 0 et 7. Maintenant, ton programme choisira automatiquement une position aléatoire sur la matrice LED.

[[[generic-python-random]]]

+ Exécute à nouveau ton programme et tu devrais voir un autre pixel aléatoire placé sur l'écran de Sense HAT. Ce sera la même couleur que tu as choisie précédemment.

+ Modifie tes variables `r`, `g`, et `b` pour chacune afin qu'elles soient égales à un nombre aléatoire entre 0 et 255. Maintenant, ton programme choisira automatiquement une couleur aléatoire.

+ Exécute à nouveau le programme et tu devrais voir apparaître un autre pixel dans un endroit aléatoire, cette fois avec une couleur aléatoire.

+ Run it a few more times, and you should see more of the grid fill up with random pixels.

If you have the `sense.clear()` line in your code, you will need to remove it. Otherwise, every time the program is re-run, the display will be cleared and your previous pixel will disappear.

![Random pixels](images/random-pixels.png)
