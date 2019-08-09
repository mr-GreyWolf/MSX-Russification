## Инструменты для работы с бинарными файлами.

### fragment-from-binary-file.py
Чтение фрагмента файла нужной длины по смещению и запись его в отдельный файл:

Параметры:
1. Исходный файл
1. Файл для сохранения фрагмента
1. Смещение в исходном файле (шестнадцатеричное)
1. Длина (число байт)

Пример:
`./fragment-from-binary-file.py file.bin fragment.bin DA5 288`

### fragment-to-binary-file.py
Запись фрагмента в файл. Исходный файл открывается только на чтение, скрипт создаёт новый файл добавляя к имени исходного суффикс **_new**

Параметры:
1. Исходный файл, в который записывается фрагмент 
1. Файл с фрагментом данных для вставки
1. Смещение в исходном файле (шестнадцатеричное)
1. Длина (число байт)

Пример:
`./fragment-to-binary-file.py file.bin fragment.bin  DA5 288`