В рамках учебного дипломного проекта выполнена реализация бэкенд-части SPA веб-приложения "Образовательные модули".

Направление: Backend
Теги: PostgreSQL, ORM, MVT/MTV, FBV/CBV, Serialiers, Viewset/Generic, Git, Readme, PEP8, Swagger, Tests, Docker
Описание: Написать небольшой проект на Django и Django Rest Framework с моделью "Образовательные модули". 
В них есть: порядковый номер, название, описание.

Детализация ТЗ к MVP:
1. На платформе будут размещаться только бесплатные образовательные модули. Интеграция с платежными сервисами не требуется.
2. Регистрация пользователя происходит по электронному адресу, имени и паролю. Верификация электронного адреса не требуется. После регистрации, пользователь сразу становится активным.
3. Аутентификация пользователя происходит по электронному адресу и паролю.
4. Пользователь может просмотреть, отредактировать и удалить свой профиль. 
5. Просматривать и редактировать профиль пользователя может сотрудник заказчика. Сотрудникам доступен просмотр всего списка пользователей. 
6. Образовательный модуль включает курс и уроки к нему. Реализация тестов в рамках MVP не требуется. 
7. Главная страница сайта содержит список курсов с постраничной пагинацией. Список курсов доступен всем. 
8. Создавать курсы и уроки, а также просматривать детальную информацию о курсах и уроках могут только зарегистрированные пользователи. 
9. Обновлять информацию о курсах/ уроках могут только владельцы курсов/ уроков, а также сотрудники заказчика. 
10. Удалять информацию о курсах/ уроках могут только владельцы курсов/ уроков.
11. При создании нового курса все зарегистрированные пользователи получают об этом уведомление на адрес электронной почты, указанный при регистрации (отложенная задача).
12. Проект покрыт авто-тестами на 90% (модели, сериалайзеры и представления - на 100%)

Инструкции для запуска:
Перед запуском приложения, необходимо создать файл .env. (см. файл .env.sample.)
Для запуска приложения необходимо выполнить команды:
docker-compose build
docker-compose up

Приложение разработано для запуска в ОС Windows.
В случае запуска приложения в ОС Linux необходимо скорректировать команды в контейнерах celery и celery-beat в файле docker-compose.yml.
