## Pixels willekeurig instellen

Eerst zullen we wat willekeurige getallen bedenken en de `set_pixel` functie gebruiken om een ​​willekeurige kleur op een willekeurige locatie op de Sense HAT display te laten oplichten.

+ Open de IDLE-editor.

[[[rpi-gui-idle-opening]]]

+ Maak een nieuw bestand aan en sla het op als `sparkles.py`.

+ Begin in het nieuwe bestand met het importeren van de `SenseHat`-module:

    ```python
    from sense_hat import SenseHat
    ```

+ Maak vervolgens een verbinding met je Sense HAT door de volgende regel code toe te voegen:

    ```python
    sense = SenseHat()
    ```


Vervolgens definiëren we x en y, om te kiezen welke pixel op de Sense HAT licht geeft.

+ Maak een variabele met de naam `x`, en stel het in op een getal van je keuze tussen 0 en 7. Dit wordt de x-coördinaat van je pixel op het scherm. [[[generic-python-creating-a-variable]]]

+ Maak een andere variabele met de naam `y`, en stel deze in op een ander getal tussen 0 en 7. Dit wordt de y-coördinaat van je pixel op het scherm.


+ Als je de kleur van je pixel wilt kiezen, denk dan aan drie getallen tussen 0 en `255`, en wijs ze toe aan variabelen met de naam `r`, `g` en `b`. Deze variabelen geven de kleur van je pixel weer als hoeveelheden rood (r), groen (g) en blauw (b).


+ Gebruik nu de `set_pixel` functie om een pixel te zetten met jouw willekeurig gekozen kleur op jouw willekeurig gekozen locatie op het display.

**Opmerking:** de onderstaande opvouwbare aanwijzingen gebruiken een andere bestandsnaam dan die van jou, en gebruiken Trinket in plaats van IDLE.

[[[rpi-sensehat-single-pixel]]]

De `set_pixel` methode neemt gegevens in de volgende volgorde: x-coördinaat, y-coördinaat, rood, groen en blauw

Om je `set_pixel` methode te definiëren, moet je de namen van de variabelen inpluggen op de vraagtekens in deze regel code in de juiste volgorde: x-coördinaat, y-coördinaat, rood, groen, blauw.

```python
sense.set_pixel(?, ?, ?, ?, ?)
```

Bekijk de hint hieronder als je vastzit.

--- hints ---

--- hint ---

Hier is hoe je voltooide code eruit zou moeten zien — je zal waarschijnlijk verschillende getallen gekozen hebben:

![Willekeurige pixeloplossing](images/random-pixel-solution.png)

--- /hint ---

--- /hints ---


+ Voer je code uit door op <kbd>F5</kbd> te drukken. Je zou een enkele LED moeten zien oplichten op het LED-display van de Sense HAT.

+ Verander nu alle getallen in je programma en voer het programma opnieuw uit. Een tweede LED moet gaan branden.
