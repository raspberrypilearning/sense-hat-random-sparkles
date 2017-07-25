## Using the random module

So far you picked your own random numbers, but you can let the computer choose them instead.

- Add another `import` line at the top of your program, below `from sense_hat import SenseHat`:

    ```python
    from random import randint
    ```

- Now change your `x = ` and `y = ` lines to automatically select a random position:

    ```python
    x = randint(0, 7)
    y = randint(0, 7)
    ```

    *The `randint` function (random integer) chooses a random number between the two given numbers, in this case 0 and 7.*

- Run your program again, and you should see another random pixel being placed on the display. It will be the same colour you chose previously.

- Now change your colour value lines to:

    ```python
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    ```

    Now your program will automatically select a random colour.

- Run it again, and you should see another pixel appear in a random location with a random colour.

- Run it a few more times, and you should see more of the grid fill up with random pixels.

<iframe src="https://trinket.io/embed/python/744a00dba6" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

