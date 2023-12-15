## Setting pixels at random

First, we'll think up some random numbers and use the `set_pixel` function to place a random colour on a random location on the Sense HAT display.

+ Open the Thonny editor.

+ Create a new file and save it as `sparkles.py`.

+ In the new file, start by importing the `SenseHat` module:

    ```python
    from sense_hat import SenseHat
    ```

+ Next, create a connection to your Sense HAT by adding this line of code:

    ```python
    sense = SenseHat()
    ```


We will then define x and y, to choose which pixel on the Sense HAT will light.

+ Create a variable called `x`, and set it equal to a number of your choice between 0 and 7. This will be the x coordinate of your pixel on the display. [[[generic-python-creating-a-variable]]]

+ Create another variable called `y`, and set it equal to another number between 0 and 7. This will be the y coordinate of your pixel on the display.


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
