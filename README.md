`News_portal` - сайт 'Новостной портал'
#### О проекте:
API для приложения сервис для авторизации, публикации новостей с комментариями и лайками.

## Описание:

🔹У каждого пользователя может быть две роли – пользователь и админ, админ
может зайти в админ-панель, пользователь – нет. Как именно решить эту задачу
не принципиально. Плюсом будет создание кастомного класса для авторизации
наследуемого от BaseAuthentication - нам важно видеть как вы решите эту задачу.

🔹Каждый пользователь может создать новость. Все пользователи могут получать
списки всех новостей с пагинацией. Пользователи могут удалять и изменять свои
новости. Админ может удалять и изменять любую новость.

🔹Также нужно добавить механизм лайков и комментариев новостей – лайкать и
комментировать может любой пользователь, автор может удалять комментарии к
своим новостям, админ может удалять любые комментарии.
При получении списка новостей и одной конкретной новости нужно показать
количество лайков и комментариев. Плюсом будет добавление списка последних
10 комментариев при получении списка новостей и одной новост.
Плюсом будет реализация механизма через микросервис.


## Технологии в проекте<br>
🔹 Python<br>
🔹 Django REST Framework<br>
🔹 PostgreSQL<br>
🔹 Nginx<br>
🔹 Docker<br>

## Подготовка и запуск проекта

- Выполните вход на свой удаленный сервер:
```
ssh username@ip
```
- Установите docker и docker-compose на сервер:
```
sudo apt install docker.io 
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

```

- Клонируйте репозиторий командой:
```
git clone git@github.com:oitczvovich/news_portal.git
``` 
- Перейдите в каталог командой:
```
cd news_portal
```
- Создаем файл .env с переменными окружения:
```
SECRET_KEY='<ключ>'
DB_ENGINE=django.db.backends.postgresql
DB_NAME=<имя_БД>
POSTGRES_USER=<имя_пользователя>
POSTGRES_PASSWORD=<пароль>
DB_HOST=db  # в случаи езменения необходимо исправить файл docker-compose.yml 
DB_PORT=5432  # в случаи езменения необходимо исправить файл docker-compose.yml 
```
- Выполните команду для запуска контейнера:
```
sudo docker-compose up -d --build
``` 
- Выполнить миграции и подключить статику
```
sudo docker-compose exec backend python manage.py makemigrations
sudo docker-compose exec backend python manage.py migrate
sudo docker-compose exec backend python manage.py collectstatic --noinput
``` 
- Создадим суперпользователя:
```
sudo docker-compose exec backend python manage.py createsuperuser
``` 

### Основные эндпоинты
http://158.160.31.83/ - точка входа
http://158.160.31.83/redoc/ - документация.


#### Регистрация пользователя.
`POST` http://158.160.31.83/api/v1/
```
{
  "username": "string",
  "email": "user@example.com",
  "password": "string"
}
```
#### Получение JWT-токена.
`POST` http://158.160.31.83/api/v1/auth/jwt/create/
```
{
  "email": "string",
  "password": "string"
}
```
### Новости

http://158.160.31.83/api/v1/

#### Список всех новостей.
Права доступа: Все пользователи.

`GET` http://158.160.31.83/api/v1/news/  - получить список всех новостий.
 
Responses

``` 
{
  "count": 0,
  "next": "http://example.com",
  "previous": "http://example.com",
  "results": [
    {
      "author": "",
      "title": "string",
      "text": "string",
      "comments": [
        "string"
      ],
      "total_comments": "string",
      "total_like": "string"
    }
  ]
}
```

#### Создать новость
`POST` http://158.160.31.83/api/v1/news/ - создать новость.

Права доступа: Только Аутентифицированный пользователь.

```
{
  "title": "string",
  "text": "string"
}
```

Responses
```
{
  "author": "string",
  "title": "string",
  "text": "string"
}
```

#### Получить определенную новость.

`GET` http://158.160.31.83/api/v1/news/{id}
    
Права доступа: Все пользователи.

Responses
```
{
  "author": "",
  "title": "string",
  "text": "string",
  "comments": [
    "string"
  ],
  "total_comments": "string",
  "total_like": "string"
}
```

#### Изменить новость.
`PUT` http://158.160.31.83/api/v1/news/{id}

Права доступа: Только автор или администратор.

```
{
  "title": "string",
  "text": "string"
}
```

Responses
```
{
  "author": "",
  "title": "string",
  "text": "string"
}
```
#### Удалить новость. 
`DELETE` http://158.160.31.83/api/v1/news/{id}

Только автор или администратор.

Responses
```
code HTTP - 204
```

#### Поставить лайк к новости.

`GET` http://158.160.31.83/api/v1/news/{id}/like/

Права доступа: Только Аутентифицированный пользователь.

```
Ставиться или снимается лайк.
```

### Комментарии.

#### Плучить все комментарии к новости.

`GET` http://158.160.31.83/api/v1/news/{news_id}/comments/

Responses

```
{
  "count": 0,
  "next": "http://example.com",
  "previous": "http://example.com",
  "results": [
    {
      "news": "string",
      "author": "string",
      "text": "string"
    }
  ]
}
```

#### Создать комментарий под новостью.

`POST` http://158.160.31.83/api/v1/news/{news_id}/comments/

Права доступа: Только Аутентифицированный пользователь.

```
{
  "text": "string"
}
```

Responses
```
{
  "news": "string",
  "author": "string",
  "text": "string"
}
```

#### Получить определенные комментарий.

`GET` http://158.160.31.83/api/v1/news/{news_id}/comments/{id}

Права доступа: Только Аутентифицированный пользователь.

Responses
```
{
  "news": "string",
  "author": "string",
  "text": "string"
}
```
#### Удалить определенные комментарий.

`DELETE` http://158.160.31.83/api/v1/news/{news_id}/comments/{id}

Права доступа: Только автор или администратор.

Responses

```
code HTTP - 204
```



### Проект
Работает по адресу:

http://158.160.31.83/<br>
http://158.160.31.83/redoc/ - документация.<br>
superuser : super@mail.ru<br>
username: SuperUser<br>
password: super342rf364g4645<br>



## Авторы проекта
### Скалацкий Владимир
e-mail: skalakcii@yandex.ru<br>
https://github.com/oitczvovi<br>
Telegramm: @OitcZvovich
