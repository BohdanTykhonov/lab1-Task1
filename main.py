def valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if 1 <= value <= 100:
                return value
            else:
                print("Число повинно бути в діапазоні від 1 до 100. Спробуйте ще раз.")
        except ValueError:
            print("Будь ласка, введіть дійсне число.")

a = valid_input("Введіть a (від 1 до 100): ")
b = valid_input("Введіть b (від 1 до 100): ")

if a > b:
    X = 2 * a / b + 1
elif a == b:
    X = -445
else:
    X = (b + 5) / a

print(f"Значення X: {X}")
