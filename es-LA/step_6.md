## Añadir un bucle

En lugar de ejecutar tu programa una y otra vez presionando <kbd>F5</kbd>, puedes añadir un bucle para que siga funcionando por sí mismo.

+ Puede utilizar el módulo `sleep` para pausar el programa entre píxeles. Para hacerlo, primero agrega otro `import` al principio de tu archivo.

```python
from time import sleep
```

+ Añade un bucle infinito en la línea debajo de las sentencias `import`.

[[[generic-python-while-true]]]

+ Indenta todas las líneas de código que contienen tus variables y `set_pixel` para que estén dentro del bucle:

--- hints --- --- hint ---

Un bucle infinito seguirá ejecutando el código dentro de él para siempre. Aquí está el código para comenzar un bucle infinito. No olvides que `True` debe tener una `T` mayúscula.

```python
while True:
```

--- /hint ---

--- hint ---

Tu código debería lucir así:

```python
while True:
    x = randint(0, 7)
    y = randint(0, 7)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    sensor.set_pixel(x, y, r, g, b)
```

--- /hint --- --- /hints ---

+ Añade una línea de código en la parte inferior de tu programa para pausar durante 0.1 segundos. Asegúrate de que esta línea esté indentada con la línea `set_pixel` para mostrar que está dentro del bucle.

[[[generic-python-sleep]]]


+ ¡Ejecuta el código, y deberías ver chispas aleatorias en acción!

![Resultado terminado](images/finished-result.gif)
