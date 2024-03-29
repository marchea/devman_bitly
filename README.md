# Обрезка ссылок с помощью сервиса Bitly

Данный скрипт взаимодействует с сервисом bitly.com (сервис для превращения ссылок в короткие).
Скрипт получает на вход (в качестве аргумента командной строки) длинную ссылку и отдает на выход короткую ссылку формата Bitly (битлинк).
Пример битлинка: bit.ly/ABCDE.
Если в качестве аргумента подается битлинк, то результатом отработки скрипта будет количество обращений по данному битлинку. 

### Как установить

Для работы скрипта необходимо: 
```
1. Зарегистрироваться на сайте https://bitly.com/ 
2. Получить токен (GENERIC ACCESS TOKEN). Инструкции как получить токен размещены на сайте (https://dev.bitly.com/get_started.html/).
3 Cоздать файл с именем ".env", который должен содержать информацию о токене (в формате "BITLY_GENERIC_TOKEN=значение"; см. пример ниже).
4. Разместить файл ".env" рядом со скриптом.
```

Пример содержимого файла ".env":

    BITLY_GENERIC_TOKEN=afnroeroinorf13jr94bg3fn

### Зависимости
Для работы необходим Python 3.
Используйте `pip` (или `pip3`, если есть конфликт с Python 2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Запуск скрипта
Для выполнения скрипта необходимо в качестве аргумента командный строки передать ссылку.

Примеры запуска скрипта:

**Пример 1:**

```
python main.py https://ya.ru
```


Пример результата вывода в консоль:
```
http://bit.ly/2NAEuUD
```
**Пример 2:**

```
python main.py http://bit.ly/2NAEuUD
```

Пример результата вывода в консоль:
```
Количество переходов по ссылке битли: 2
```


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

### Лицензия

MIT
