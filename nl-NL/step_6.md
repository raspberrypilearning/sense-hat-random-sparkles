## Voeg een lus toe

In plaats van je programma steeds opnieuw uit te voeren door op <kbd>F5</kbd> te drukken, kun je een lus toevoegen zodat deze vanzelf blijft lopen.

+ Je kunt de `sleep` module gebruiken om het programma tussen pixels te pauzeren. Om dit te doen, voeg eerst nog een `import` toe aan de bovenkant van je bestand.

```python
from time import sleep
```

+ Voeg een oneindige lus toe op de regel onder de `import`-commando's.

[[[generic-python-while-true]]]

+ Laat alle regels code inspringen die je variabelen en `set_pixel` bevatten zodat ze binnen de lus zitten:

--- hints ---
 --- hint ---

Een oneindige lus zal de code erbinnen voor altijd blijven uitvoeren. Hier is de code om een oneindige lus te beginnen. Vergeet niet dat `True` een hoofdletter `T` moet hebben.

```python
while True:
```

--- /hint ---

--- hint ---

Dit is hoe je code eruit zou moeten zien:

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

+ Voeg een regel code toe aan de onderkant van je programma om 0.1 seconde te pauzeren. Zorg ervoor dat deze regel gelijk ingesprongen is met de `set_pixel` regel om te laten zien dat deze zich binnen de lus bevindt.

[[[generic-python-sleep]]]


+ Voer de code uit en je zou willekeurige fonkelingen in actie moeten zien!

![Eindresultaat](images/finished-result.gif)
