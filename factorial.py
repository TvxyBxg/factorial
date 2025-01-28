def factorial(n):
    """Вычисляет факториал числа n."""
    if n < 0:
        raise ValueError("Факториал не определен для отрицательных чисел.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

if __name__ == "__main__":
    try:
        number = int(input("Введите целое неотрицательное число для вычисления факториала: "))
        print(f"Факториал числа {number} равен {factorial(number)}")
    except ValueError as e:
        print(f"Ошибка: {e}")
