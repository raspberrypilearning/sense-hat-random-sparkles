## Das `Zufalls`-Modul verwenden

Bisher hast du deine eigenen zufälligen Zahlen ausgewählt, aber du kannst stattdessen den Computer diese mit Hilfe des `Zufalls`-Moduls auswählen lassen.

+ Füge eine weitere `import`-Zeile ganz **oben** in deinem Programm hinzu:

```python
from random import randint
```

+ Ändere deine `x` und `y`-Variablen auf eine zufällige Zahl zwischen 0 und 7. Jetzt wählt dein Programm automatisch eine zufällige Position innerhalb deiner LED Matrix aus.

[[[generic-python-random]]]

+ Führe dein Programm erneut aus, und du solltest ein anderes beliebiges Pixel sehen, das auf dem Display platziert wird. Es wird die gleiche Farbe haben, die du zuvor gewählt hast.

+ Ändere deine `r`, `g` und `b`-Variablen auf eine zufällige Zahl zwischen 0 und 255. Jetzt wählt dein Programm automatisch eine zufällige Farbe.

+ Führe es erneut aus, und du solltest ein Pixel an einem zufälligen Ort mit einer zufälligen Farbe aufleuchten sehen.

+ Führe es noch ein paar Mal aus, und du solltest sehen, dass sich das Display mit zufälligen Pixeln füllt.

Wenn du die `sense.clear()`-Zeile in deinem Code hast, musst du sie entfernen. Andernfalls wird jedes Mal, wenn das Programm erneut ausgeführt wird, das Display gelöscht und deine vorherigen Pixel verschwinden.

![Zufällige Pixel](images/random-pixels.png)
