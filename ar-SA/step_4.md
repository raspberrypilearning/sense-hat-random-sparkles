## ضبط وحدات البكسل عشوائيا

أولاً، سوف نفكر في بعض الأرقام العشوائية ونستخدم الدالة `set_pixel` لوضع لون عشوائي على موقع عشوائي على شاشة Sense HAT.

+ افتح محرر IDLE.

[[[rpi-gui-idle-opening]]]

+ قم بإنشاء ملف جديد واحفظه باسم `sparkles.py`.

+ في الملف الجديد، ابدأ باستيراد الوحدة النمطية `SenseHat`:

    ```python
    from sense_hat import SenseHat
    ```

+ بعد ذلك، قم بإنشاء اتصال بـ Sense HAT الخاص بك عن طريق إضافة هذا السطر من التعليمة البرمجية:

    ```python
    sense = SenseHat()
    ```


سنقوم بعد ذلك بتحديد x و y لاختيار أي بكسل سيضيء على لوحة Sense HAT.

+ قم بإنشاء متغير يسمى `x`، وقم باعطائه عدداً من اختيارك بين 0 و 7. سيكون هذا إحداثي x الخاص بك على الشاشة. 

[[[generic-python-creating-a-variable]]]

+ قم بإنشاء متغير يسمى `y`، وقم باعطائه عدداً من اختيارك بين 0 و 7. سيكون هذا إحداثي y الخاص بك على الشاشة.


+ لاختيار لون البكسل الخاص بك، فكّر في ثلاثة أرقام بين 0 و`255`، ثم قم بتعيينهم إلى متغيرات تسمى `r`، `g`، و`b`. ستمثل هذه المتغيرات لون البكسل الخاص بك كمقادير الأحمر (r) والأخضر (g) والأزرق (b).


+ الآن استخدم الدالة `set_pixel` لوضع بكسل مع اللون الذي تم اختياره عشوائيا في موقعك الذي تم اختياره عشوائيا على الشاشة.

**ملاحظة:** الاتجاهات القابلة للطي أدناه تستخدم اسم ملف مختلف عن اسم ملفك ، وتستخدم Trinket بدلاً من IDLE.

[[[rpi-sensehat-single-pixel]]]

طريقة `set_pixel` تأخذ البيانات بالترتيب التالي: إحداثي x، إحداثي y، أحمر، أخضر، أزرق

لتعريف `set_pixel` الخاصة بك، قم بتوصيل أسماء المتغيرات الخاصة بك إلى علامات الاستفهام في هذا السطر من التعليمات البرمجية، بالترتيب الصحيح: إحداثي x، إحداثي y، أحمر، أخضر، أزرق.

```python
sense.set_pixel(?, ?, ?, ?, ?, ?)
```

عرض التلميح أدناه إذا كنت عالقا.

--- hints ---


--- hint ---

إليك الطريقة التي يجب أن تبدو بها التعليمات البرمجية النهائية - ربما تكون قد اخترت أرقام مختلفة:

![حل بكسل عشوائي](images/random-pixel-solution.png)

--- /hint ---

--- /hints ---


+ قم بتشغيل التعليمات البرمجية بالضغط على <kbd>F5</kbd>. من المفترض أن ترى ضوء LED واحدًا على شاشة LED الخاصة بـ Sense HAT.

+ الآن قم بتغيير جميع الأرقام في برنامجك وقم بتشغيل البرنامج مرة أخرى. يجب تشغيل مصباح LED ثانٍ.
