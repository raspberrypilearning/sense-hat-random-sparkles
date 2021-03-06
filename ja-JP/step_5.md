## `random`（ランダム）モジュールを使う

ここまでは自分でランダムな数字を選びましたが、かわりに`random`（ランダム）モジュールを使ってコンピュータに選ばせることができます。

+ プログラムの**先頭**にもうひとつ`import`（インポート）を追加します。

```python
from random import randint
```

+ `x`変数と`y`変数を0から7までのランダムな数字に変更します。 これでプログラムがLEDマトリクス上のランダムな位置を自動的に選びます。

[[[generic-python-random]]]

+ もう一度プログラムを実行すると、Sense HATのディスプレイに別のランダムなピクセルが表示されます。 色は前に選んだのと同じになります。

+ 変数`r`、`g`、`b`をそれぞれ0から255までのランダムな数に変更します。 これでプログラムが自動的にランダムな色を選びます。

+ もう一度プログラムを実行すると、ランダムな位置に別のピクセルが表示され、今回はランダムな色で表示されます。

+ 何回かこれをくり返すと、多くのグリッドがランダムなピクセルでいっぱいになるはずです。

コードに`sense.clear()`がある場合、それを削除する必要があります。 そうしないと、プログラムを再実行するたびにディプレイの表示がクリアされ、前にあったピクセルが消えます。

![ランダムなピクセル](images/random-pixels.png)
