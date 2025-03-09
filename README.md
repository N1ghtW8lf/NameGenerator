# NameGenerator
📝 Генератор русских имен и фамилий с поддержкой случайного выбора

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

Генератор русских имен и фамилий с возможностью случайного выбора и обработкой текстовых данных. Библиотека предоставляет простой API для работы с русскими именами и фамилиями.

## Особенности
✨ **Поддержка русских имен и фамилий**
✨ **Случайный выбор элементов**
✨ **Обработка текстовых данных**
✨ **Простой и понятный API**
✨ **Легкая интеграция в проекты**

## Установка
```
git clone https://github.com/N1ghtW8lf/NameGenerator
```

## Использование
```python
from NameGenerator.main import Generator

# Создание экземпляра генератора
generator = NameGenerator(sex="male")

# Получение случайного имени
random_name = generator.get_fullname()
print(random_name)  # Например: "Арсений Попов"

```

## API
### NameGenerator
#### `get_fullname()`
Возвращает случайное русское полное имя.

## Вклад
Пул-реквесты приветствуются! Если вы хотите добавить новые функции или улучшить существующие, создайте пул-реквест с описанием изменений.

## Лицензия
Проект распространяется под лицензией MIT. Вы можете свободно использовать, модифицировать и распространять код.

## Автор
👤 **N1ghtW8lf**
- GitHub: [@N1ghtW8lf](https://github.com/N1ghtW8lf)
