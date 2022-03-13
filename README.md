# api_final
api final

## Коротко о проекте

Данный проект позволяет с помощью API:
1. Создавать посты в сообществе
2. Комментировать посты авторов
3. Подписываться на понравившихся авторов

Данный функционал доступен только для авторизованных пользователей.
Не авторизованным пользователям доступна только фунция просмотра контента.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Gwynrey/api_final_yatube.git
```

```
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
