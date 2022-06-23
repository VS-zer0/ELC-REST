# ELC-REST
Репозиторий для хранения файлов REST API для работы с базой данных ЭУК

## Сущность Student:

- GET /students - получить список студентов
- POST /students - добавить студента
- GET /students/{id} - получить данные студента по ID
- PATCH /students/{id} - обновить данные студента по его ID
- DELETE /students/{id} - удалить данные студента по его ID
#### Курсы
- GET /students/{id}/status - получить прогресс студента по его курсам
- POST /students/{id}/status - записать студента на курс
- GET /students/{id}/status/{course_id} - получить прогресс студента по определенному курсу
- DELETE /students/{id}/status/{course_id} - исключить студента из курса
#### Тесты
- GET /students/{id}/tests - получить результаты прохождения тестов студентом
- POST /students/{id}/tests - записать студента на прохождение теста
- GET /students/{id}/tests/{test_id} - просмотреть результаты студента по определенному тесту
- GET /students/{id}/tests/{test_id}/answers - просмотреть ответы студента на вопросы теста
- POST /students/{id}/tests/{test_id}/answers - добавить ответ студента на вопрос
- GET /students/{id}/tests/{test_id}/answers/{task_id} - просмотреть ответ студента на определенный вопрос

## Сущность Course:

- GET /courses - получить список курсов
- POST /courses - добавить курс
- GET /courses/{id} - получить данные курса по ID
- PATCH /courses/{id} - обновить данные курса по ID
- DELETE /courses/{id} - удалить данные курса по ID
#### Прогресс студентов
- GET /courses/{id}/status - получить прогресс студентов по курсу
- POST /courses/{id}/status - записать студента на курс
- GET /courses/{id}/status/{student_id} - получить прогресс определенного студента по курсу
- DELETE /courses/{id}/status/{student_id} - исключить определеного студента из курса
#### Категории
- GET /courses/{id}/categories - получить список категорий курса
- POST /courses/{id}/categories - добавить категорию в курс
- GET /courses/{id}/categories/{cat_id} - получить категорию по ID
- PATCH /courses/{id}/categories/{cat_id} - обновить категорию по ID
- DELETE /courses/{id}/categories/{cat_id} - удалить категорию по ID
#### Материалы
- GET /courses/{id}/categories/{cat_id}/materials - получить список материалов категории
- POST /courses/{id}/categories/{cat_id}/materials - добавить данные материалов в категорию
- GET /courses/{id}/categories/{cat_id}/materials/{mat_id} - получить данные материала категории по ID
- PATCH /courses/{id}/categories/{cat_id}/materials/{mat_id} - обновить данные материала категории по ID
- DELETE /courses/{id}/categories/{cat_id}/materials/{mat_id} - удалить данные материала из категории
#### Тесты
- GET /courses/{id}/categories/{cat_id}/tests - получить список тестов в категории
- POST /courses/{id}/categories/{cat_id}/tests - добавить тест в категорию
- GET /courses/{id}/categories/{cat_id}/tests/{test_id} - получить данные определенного теста
- PATCH /courses/{id}/categories/{cat_id}/tests/{test_id} - обновить данные теста
- DELETE /courses/{id}/categories/{cat_id}/tests/{test_id} - удалить тест
- GET /courses/{id}/categories/{cat_id}/tests/{test_id}/tasks - получить список вопросов из теста
- POST /courses/{id}/categories/{cat_id}/tests/{test_id}/tasks - добавить вопрос в тест
- GET /courses/{id}/categories/{cat_id}/tests/{test_id}/tasks/{task_id} - получить данные определеного вопроса из теста
- PATCH /courses/{id}/categories/{cat_id}/tests/{test_id}/tasks/{task_id} - обновить вопрос теста
- DELETE /courses/{id}/categories/{cat_id}/tests/{test_id}/tasks/{task_id} - удалить вопрос из теста
- GET /courses/{id}/categories/{cat_id}/tests/{test_id}/tasks/{task_id}/answers - получить список ответов на вопрос
- POST /courses/{id}/categories/{cat_id}/tests/{test_id}/tasks/{task_id}/answers - добавить ответ на вопрос
- GET /courses/{id}/categories/{cat_id}/tests/{test_id}/tasks/{task_id}/answers/{ans_id} - получить данные определенного ответа
- PATCH /courses/{id}/categories/{cat_id}/tests/{test_id}/tasks/{task_id}/answers/{ans_id} - обновить определенный ответ
- DELETE /courses/{id}/categories/{cat_id}/tests/{test_id}/tasks/{task_id}/answers/{ans_id} - удалить ответ из теста
- GET /courses/{id}/categories/{cat_id}/tests/{test_id}/tasks/{task_id}/attempts - получить список попыток решения вопроса
- GET /courses/{id}/categories/{cat_id}/tests/{test_id}/tasks/{task_id}/attempts/{att_id} - получить данные определенной попытки решения вопроса
- GET /courses/{id}/categories/{cat_id}/tests/{test_id}/results - получить результаты прохождения теста студентами
- GET /courses/{id}/categories/{cat_id}/tests/{test_id}/results/{att_id} - получить данные определенной попытки

