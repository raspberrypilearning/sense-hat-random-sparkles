## Ρύθμιση τυχαίων εικονοστοιχείων

Αρχικά, θα σκεφτούμε μερικούς τυχαίους αριθμούς και θα χρησιμοποιήσουμε τη συνάρτηση ` set_pixel ` για να τοποθετήσουμε ένα τυχαίο χρώμα σε μια τυχαία θέση στην οθόνη Sense HAT.

+ Άνοιξε το πρόγραμμα επεξεργασίας IDLE.

[[[rpi-gui-idle-opening]]]

+ Δημιούργησε ένα νέο αρχείο και αποθήκευσέ το ως ` sparkles.py `.

+ Στο νέο αρχείο, ξεκίνησε κάνοντας import το module ` SenseHat `:

    ```python
    from sense_hat import SenseHat
    ```

+ Στη συνέχεια, δημιούργησε μια σύνδεση με το δικό σου Sense HAT προσθέτοντας αυτήν τη γραμμή κώδικα:

    ```python
    sense = SenseHat()
    ```


We will then define x and y, to choose which pixel on the Sense HAT will light.

+ Δημιούργησε μια μεταβλητή με όνομα ` x ` και τιμή έναν αριθμό της επιλογής σου μεταξύ 0 και 7. This will be the x coordinate of your pixel on the display. [[[generic-python-creating-a-variable]]]

+ Δημιούργησε μια άλλη μεταβλητή με όνομα ` y ` και τιμή έναν άλλο αριθμό μεταξύ 0 και 7. Αυτή θα είναι η συντεταγμένη y του εικονοστοιχείου σου στην οθόνη.


+ To choose the colour of your pixel, think of three numbers between 0 and `255`, then assign them to variables called `r`, `g`, and `b`. These variables will represent the colour of your pixel as amounts of red (r), green (g), and blue (b).


+ Now use the `set_pixel` function to place a pixel with your randomly chosen colour at your randomly chosen location on the display.

**Note:** the collapsible directions below use a different filename than yours, and uses Trinket instead of IDLE.

[[[rpi-sensehat-single-pixel]]]

The `set_pixel` method takes data in the following order: x coordinate, y coordinate, red, green, blue

To define your `set_pixel` method, plug the names of your variables into the question marks in this line of code, in the right order: x coordinate, y coordinate, red, green, blue.

```python
sense.set_pixel(?, ?, ?, ?, ?)
```

View the hint below if you are stuck.

--- hints ---

--- hint ---

Here is how your finished code should look — you will probably have chosen different numbers:

![Random pixel solution](images/random-pixel-solution.png)

--- /hint ---

--- /hints ---


+ Run your code by pressing <kbd>F5</kbd>. You should see a single LED light up on the Sense HAT's LED display.

+ Now change all of the numbers in your program and run the program again. A second LED should turn on.
