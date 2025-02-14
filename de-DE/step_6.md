## Füge eine Schleife hinzu

Anstatt dein Programm durch Drücken von <kbd>F5</kbd> immer wieder zu starten, kannst du eine Schleife hinzufügen, damit es selbst weiter läuft.

+ Du kannst das `Schlaf`-Modul verwenden, um das Programm zwischen Pixeln zu pausieren. Füge zunächst einen weiteren `import` am Anfang deiner Datei hinzu.

```python
from time import sleep
```

+ Füge dann eine Endlosschleife auf der Zeile unterhalb der `Import`-Anweisungen hinzu.

[[[generic-python-while-true]]]

+ Rücke alle Codezeilen, die deine Variablen und `set_pixel` enthalten, ein damit sie innerhalb der Schleife sind:

--- hints ---
--- hint ---

In einer Endlosschleife wird der darin enthaltene Code für immer ausgeführt. Hier ist der Code, um eine Endlosschleife zu beginnen. Vergiss nicht, dass `True` mit einem großen `T` geschrieben sein muss.

```python
while True:
```

--- /hint ---

--- hint ---

So sollte dein neuer Code aussehen:

```python
while True:
    x = randint(0, 7)
    y = randint(0, 7)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    sense.set_pixel(x, y, r, g, b)
```

--- /hint ---
--- /hints ---

+ Füge am unteren Rand deines Programms eine Codezeile hinzu, um eine Pause von 0,1 Sekunden einzulegen. Vergewissere dich, dass diese Zeile mit der Zeile `set_pixel` eingerückt ist, um zu zeigen, dass sie sich innerhalb der Schleife befindet.

[[[generic-python-sleep]]]


+ Führe den Code aus und du solltest zufälliges Funkeln in Aktion sehen!

![Fertiges Ergebnis](images/finished-result.gif)
