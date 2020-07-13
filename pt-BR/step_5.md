## Usando o módulo `random`

Até agora você escolheu seus próprios números aleatórios, mas você pode deixar que o computador os escolha usando o módulo `random`.

+ Adicione outra linha `import` no **topo** do seu programa:

```python
from random import randint
```

+ Altere suas variáveis `x` e `y` para serem iguais a um número aleatório entre 0 e 7. Agora seu programa selecionará automaticamente uma posição aleatória na matriz LED.

[[[generic-python-random]]]

+ Execute seu programa novamente e você deve ver outro pixel aleatório sendo colocado no visor do Sense HAT. Será da mesma cor que você escolheu anteriormente.

+ Altere suas variáveis `r`, `g` e `b` para que cada uma seja igual a um número aleatório entre 0 e 255. Agora seu programa selecionará automaticamente uma cor aleatória.

+ Execute o programa novamente e você deve ver outro pixel aparecer em uma posição aleatória, desta vez com uma cor aleatória.

+ Execute-o mais algumas vezes e você verá mais da grade preenchida com pixels aleatórios.

Se você tiver a linha `sense.clear()` no seu código, você precisará removê-la. Caso contrário, sempre que o programa for executado novamente, o visor será apagado e o pixel anterior desaparecerá.

![Pixels aleatórios](images/random-pixels.png)
