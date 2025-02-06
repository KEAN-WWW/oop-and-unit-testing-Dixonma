from calculator import Calculator


def main():
    calc = Calculator()

    print("Addition: ", calc.addition(10, 5))
    print("Subtraction: ", calc.subtraction(10, 5))
    print("Multiplication: ", calc.multiplication(10, 5))
    print("Division: ", calc.division(10, 5))


if __name__ == "__main__":
    main()
