# Образовательныей портал

Реализован на Python 3.9 / Django 3.2

Для запуска:
1. Склонируйте репозиторий 
2. В папке проекта наберите 
    
    <code>python manage.py makemigrations
    
    python manage.py migrate</code>

3. Создайте суперпользователя

    <code>python manage.py createsuperuser</code>

4. Запустите тестовый сервер. 

    <code>python manage.py runserver</code>

5. Для наполнения базы данных перейдите по адресу <code>http://localhost:8000/admin/</code> и введите данные суперпользователя, указанные на шаге 4

6. Зайдите на стартовую страницу <code>http://localhost:8000/</code> 