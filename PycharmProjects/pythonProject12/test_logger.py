import pytest
from decorators import log

# Тестируем вывод в консоль
@log()
def successful_function(a, b):
    return a + b

@log()
def failing_function(a, b):
    return a / b

def test_successful_function_logs(capsys):
    # Проверяем логи успешного выполнения
    result = successful_function(2, 3)
    assert result == 5

    # Перехватываем вывод в консоль
    captured = capsys.readouterr()
    assert "Начало выполнения функции: successful_function" in captured.out
    assert "successful_function ok. Результат: 5" in captured.out
    assert "Конец выполнения функции: successful_function" in captured.out

def test_failing_function_logs(capsys):
    # Проверяем логи в случае исключения
    with pytest.raises(ZeroDivisionError):
        failing_function(1, 0)

    # Перехватываем вывод в консоль
    captured = capsys.readouterr()
    assert "Начало выполнения функции: failing_function" in captured.out
    assert "failing_function error: ZeroDivisionError" in captured.out
    assert "Inputs: (1, 0), {}" in captured.out
    assert "Конец выполнения функции: failing_function" in captured.out

# Тестируем логирование в файл
@log(filename="test_log.txt")
def file_logging_function(x, y):
    return x * y

def test_file_logging():
    # Выполнение функции, логи пишутся в файл
    result = file_logging_function(2, 3)
    assert result == 6

    # Проверяем содержимое файла
    with open("test_log.txt", "r") as f:
        logs = f.read()
        assert "Начало выполнения функции: file_logging_function" in logs
        assert "file_logging_function ok. Результат: 6" in logs
        assert "Конец выполнения функции: file_logging_function" in logs
