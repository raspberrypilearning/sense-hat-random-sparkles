## Встановлення пікселів випадковим чином

Спочатку придумай кілька випадкових чисел і використай функцію `set_pixel`, щоб розмістити випадковий колір у випадковому місці на дисплеї Sense HAT.

+ Відкрий редактор Thonny.

+ Створи новий файл і збережи його як `sparkles.py`.

+ У новому файлі почни з імпорту модуля `SenseHat`:

    ```python
    from sense_hat import SenseHat
    ```

+ Далі під'єднай Sense HAT, додавши цей рядок коду:

    ```python
    sense = SenseHat()
    ```


Потім визнач x і y, щоб вибрати, який піксель на Sense Hat буде світитися.

+ Створи змінну з назвою `x` та запиши в неї число від 0 до 7 на твій вибір. Це буде координата х твого пікселя на дисплеї. 
[[[generic-python-creating-a-variable]]]

+ Створи змінну з назвою `y`, та запиши в неї інше число від 0 до 7 на твій вибір. Це буде координата y твого пікселя на дисплеї.


+ Щоб вибрати колір пікселя, придумай три числа від 0 до `255`, а потім запиши їх у змінні з назвою `r`, `g` та `b`. Ці змінні будуть представляти колір твого пікселя у вигляді кількості червоного (r), зеленого (g) і синього (b).


+ Тепер скористайся функцією `set_pixel` для розміщення пікселя з випадково обраним кольором у випадково обраному місці на дисплеї.

**Примітка:** наведені нижче вказівки у згорнутому вигляді використовують інше ім'я файлу та використовують Trinket замість IDLE.

[[[rpi-sensehat-single-pixel]]]

Функція `set_pixel` приймає дані в наступному порядку: координата x, координата y, червоний (r), зелений (g), синій (b)

Щоб визначити функцію `set_pixel`, введи імена змінних замість знаків запитання у цьому рядку коду в правильному порядку: координата x, координата y, r, g, b.

```python
sense.set_pixel(?, ?, ?, ?, ?)
```

Подивись підказку нижче, якщо щось не виходить.

--- hints ---

--- hint ---

Ось як повинен виглядати готовий код — скоріше за все у тебе будуть інші цифри:

![Рішення з випадковим пікселем](images/random-pixel-solution.png)

--- /hint ---

--- /hints ---


+ Запусти свій код, натиснувши <kbd>F5</kbd>. Ти маєш побачити, що на світлодіодному дисплеї Sense HAT засвітився один світлодіод.

+ Тепер зміни всі цифри у програмі і запусти її знову. Другий світлодіод має засвітитися.
