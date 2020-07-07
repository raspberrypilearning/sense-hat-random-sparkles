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

+ Exécute-le encore plusieurs fois, et tu devrais voir une plus grande partie de la grille se remplir de pixels aléatoires.

Si tu as la ligne `sense.clear()` dans ton code, tu dois la supprimer. Sinon, chaque fois que le programme est relancé, l'affichage sera effacé et ton pixel précédent disparaîtra.

![Pixels aléatoires](images/random-pixels.png)
