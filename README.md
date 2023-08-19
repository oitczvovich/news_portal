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
### Проект
Работает по адресу http://158.160.31.83/
superuser : super@mail.ru
username: SuperUser
password: super342rf364g4645



## Авторы проекта
### Скалацкий Владимир
e-mail: skalakcii@yandex.ru<br>
https://github.com/oitczvovi<br>
Telegramm: @OitcZvovich
