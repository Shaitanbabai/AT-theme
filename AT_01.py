def calculate_remainder(dividend, divisor):
    if divisor == 0:
        raise ValueError("Деление на ноль недопустимо.")

    remainder = dividend % divisor

    # Если делитель отрицательный и делимое отрицательное, делаем остаток отрицательным
    if dividend < 0 < divisor:
        if remainder != 0:
            remainder -= abs(divisor)
    elif dividend > 0 > divisor:
        remainder += abs(divisor)

    return remainder


def main():
    try:
        dividend = float(input("Введите делимое: "))
        divisor = float(input("Введите делитель: "))

        remainder = calculate_remainder(dividend, divisor)
        print(f"Остаток от деления {dividend} на {divisor} равен {remainder:.4f}.")

    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла неожиданная ошибка: {e}")


if __name__ == "__main__":
    main()
