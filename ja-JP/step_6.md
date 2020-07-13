## ループを追加する

<kbd>F5</kbd>キーを押して何回もプログラムを実行するのではなく、ループを追加して実行しつづけるようにできます。

+ `sleep`（スリープ）モジュールを使って、ピクセルごとにプログラムを一時停止することができます。 そうするには、まずプログラムの先頭にもうひとつ`import`（インポート）を追加します。

```python
from time import sleep
```

+ `import`（インポート）文の下の行に無限ループを追加します。

[[[generic-python-while-true]]]

+ 変数と`set_pixel`を含むコードの行をすべてインデントし、ループの中に入れます：

--- hints ---
 --- hint ---

無限ループはその中のコードをずっと実行しつづけます。 無限ループを開始するコードは次のとおりです。 `True`（真）は最初の文字を大文字`T`にする必要があることを忘れないでください。

```python
while True:
```

--- /hint ---

--- hint ---

コードは次のようになります：

```python
while True:
    x = randint(0, 7)
    y = randint(0, 7)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    sense.set_pixel(x, y, r, g, b)
```

--- /hint ------ /hints ---

+ プログラムの最後に0.1秒間停止するコードを追加します。 この行がループ内にあることを示すために、`set_pixel`行と同じレベルでインデントされているか確認してください。

[[[generic-python-sleep]]]


+ コードを実行すると、実際にランダムにきらめくのが見られるはずです！

![完成した結果](images/finished-result.gif)
