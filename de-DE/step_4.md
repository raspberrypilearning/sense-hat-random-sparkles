## Pixel zufällig einstellen

Zuerst überlegen wir uns einige Zufallszahlen und verwenden die `set_pixel` Funktion, um eine zufällige Farbe an einer zufälligen Stelle auf dem Sense HAT-Display zu platzieren.

+ Öffne den IDLE-Editor.

[[[rpi-gui-idle-opening]]]

+ Erstelle eine neue Datei und speichere sie als `sparkles.py`.

+ Beginne in der neuen Datei mit dem Import des `SenseHat`-Moduls:

    ```python
    from sense_hat import SenseHat
    ```

+ Erstelle als Nächstes eine Verbindung zu deinem Sense HAT, indem du folgende Code-Zeile hinzufügst:

    ```python
    sense = SenseHat()
    ```


Wir werden dann x und y definieren, um auszuwählen, welche Pixel auf dem Sense HAT aufleuchten.

+ Erstelle eine Variable namens `x`, und setze sie gleich einer Zahl deiner Wahl zwischen 0 und 7. Dies wird die X-Koordinate deines Pixels auf dem Display sein. 

[[[generic-python-creating-a-variable]]]

+ Erstelle eine weitere Variable namens `y`, und setze sie gleich einer Zahl deiner Wahl zwischen 0 und 7. Dies ist die y-Koordinate deines Pixels auf dem Display.


+ Um die Farbe deines Pixels auszuwählen, denke an drei Zahlen zwischen 0 und `255`, dann ordne sie den Variablen `r`, `g`, und `b` zu. Diese Variablen repräsentieren die Farbe deines Pixels als rot (r), grün (g) und blau (b).


+ Verwende nun die `set_pixel` Funktion, um deine zufällige Farbe an deinem zufälligen Ort auf dem Display zu platzieren.

**Hinweis:** Die folgenden einklappbaren Anweisungen verwenden einen anderen Dateinamen als deinen und verwenden Trinket anstelle von IDLE.

[[[rpi-sensehat-single-pixel]]]

Die `set_pixel`-Methode erfasst Daten in der folgenden Reihenfolge: X-Koordinate, Y-Koordinate, rot, grün, blau

Um deine `set_pixel`-Methode zu definieren, packe die Namen deiner Variablen in die Fragezeichen in dieser Codezeile in der richtigen Reihenfolge: X-Koordinate, Y-Koordinate, rot, grün, blau.

```python
sense.set_pixel(?, ?, ?, ?, ?)
```

Sieh dir den Hinweis unten an, wenn du nicht weiterkommst.

--- hints ---


--- hint ---

So sollte dein fertiger Code aussehen - du wirst wahrscheinlich andere Zahlen gewählt haben:

![Zufällige Pixellösung](images/random-pixel-solution.png)

--- /hint ---

--- /hints ---


+ Führe deinen Code mit <kbd>F5</kbd> aus. Auf dem LED-Display des Sense HAT sollte eine einzelne LED aufleuchten.

+ Ändere nun alle Nummern in deinem Programm und starte das Programm erneut. Eine zweite LED sollte aufleuchten.
