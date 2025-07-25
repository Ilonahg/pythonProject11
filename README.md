# Edu Platform Homework

## Інструкція для запуску

1. Встановіть залежності:
```
pip install -r requirements.txt
```

2. Зробіть міграції:
```
python manage.py migrate
```

3. Запустіть сервер:
```
python manage.py runserver
```

4. Перевірте API (Postman):
- `POST /api/subscribe/` — підписка/відписка
- `GET /api/courses/` — список курсів (з пагінацією)
- `GET /api/lessons/` — список уроків (з пагінацією)
