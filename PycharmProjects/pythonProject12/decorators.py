import logging
from functools import wraps


def log(filename=None):
    """
    Декоратор для логирования начала, конца и ошибок выполнения функции.

    :param filename: str или None. Если задано, логи записываются в файл, иначе в консоль.
    """
    # Настройка логирования
    logger = logging.getLogger("FunctionLogger")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()  # Удаляем предыдущие обработчики, чтобы избежать дублирования

    # Настройка обработчика
    if filename:
        handler = logging.FileHandler(filename, mode='a')
    else:
        handler = logging.StreamHandler()

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Логируем начало выполнения функции
            logger.info(f"Начало выполнения функции: {func.__name__}")
            try:
                result = func(*args, **kwargs)
                # Логируем успешное выполнение
                logger.info(f"{func.__name__} ok. Результат: {result}")
                return result
            except Exception as e:
                # Логируем ошибку
                logger.error(
                    f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                )
                raise
            finally:
                # Логируем завершение выполнения
                logger.info(f"Конец выполнения функции: {func.__name__}")

        return wrapper

    return decorator
