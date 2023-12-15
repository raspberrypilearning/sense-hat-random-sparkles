## Usando el módulo `random`

Hasta ahora, elegiste tus propios números aleatorios, pero puedes dejar que la computadora los elija usando el módulo `random`.

+ Añade otra línea `import` en la parte **superior** de tu programa:

```python
from random import randint
```

+ Cambia tus variables `x` e `y` para que sean iguales a un número aleatorio entre 0 y 7. Ahora el programa seleccionará automáticamente una posición aleatoria en la matriz LED.

[[[generic-python-random]]]

+ Ejecuta tu programa de nuevo, y deberías ver otro píxel aleatorio colocado en la pantalla de Sense HAT. Será del mismo color que eligiste anteriormente.

+ Cambia tus variables `r`, `g`, y `b` para que cada una de ellas sea igual a un número aleatorio entre 0 y 255. Ahora tu programa seleccionará automáticamente un color aleatorio.

+ Ejecuta el programa de nuevo, y deberías ver otro píxel en una ubicación aleatoria, esta vez con un color aleatorio.

+ Ejecútalo unas cuantas veces más y deberías ver que más de la cuadrícula se llena con píxeles aleatorios.

Si tienes la línea `sensor.clear()` en tu código, necesitarás eliminarla. De lo contrario, cada vez que el programa se vuelve a ejecutar, la pantalla se borrará y tu píxel anterior desaparecerá.

![Píxeles aleatorios](images/random-pixels.png)
