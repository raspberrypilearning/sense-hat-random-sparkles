## De `random` module gebruiken

Tot nu toe heb je je eigen willekeurige getallen gekozen, maar je kunt de computer ze laten kiezen door de `random` module te gebruiken.

+ Voeg nog een `import` regel toe aan de **bovenkant** van je programma:

```python
from random import randint
```

+ Verander je `x` en `y` variabelen zodat die gelijk zijn aan een willekeurig getal tussen 0 en 7. Nu selecteert je programma automatisch een willekeurige positie op de LED-matrix.

[[[generic-python-random]]]

+ Voer je programma opnieuw uit en je zou een andere willekeurige pixel moeten zien worden geplaatst op het Sense HAT scherm. Het zal dezelfde kleur zijn die je eerder hebt gekozen.

+ Wijzig je `r`, `g` en `b` variabelen zodat die ieder gelijk zijn aan een willekeurig getal tussen 0 en 255. Nu selecteert je programma automatisch een willekeurige kleur.

+ Voer het programma opnieuw uit en je zou een andere pixel op een willekeurige locatie moeten zien verschijnen, ditmaal met een willekeurige kleur.

+ Voer het nog een paar keer uit, en je zou meer van het raster moeten zien vollopen met willekeurige pixels.

Als je de `sense.clear()` regel in je code hebt, moet je deze verwijderen. Anders wordt elke keer als het programma opnieuw wordt opgestart, het scherm gewist en je vorige pixel zal verdwijnen.

![Willekeurige pixels](images/random-pixels.png)
