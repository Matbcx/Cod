from tkinter import *

# Функція для обробки натискання на кнопки з цифрами
def button_click(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, str(current) + str(number))

# Функція для очищення вмісту відображення
def button_clear():
    display.delete(0, END)

# Функція для виконання арифметичних операцій
def button_operation(op):
    global f_num
    global math
    math = op
    f_num = int(float(display.get())) # Використовуємо int(), щоб перетворити у ціле число
    display.delete(0, END)

# Функція для виконання обчислень та відображення результату
def button_equal():
    second_number = int(float(display.get())) # Використовуємо int(), щоб перетворити у ціле число
    display.delete(0, END)
    if math == "add":
        display.insert(0, f_num + second_number)
    elif math == "subtract":
        display.insert(0, f_num - second_number)
    elif math == "multiply":
        display.insert(0, f_num * second_number)
    elif math == "divide":
        try:
            display.insert(0, f_num / second_number)
        except ZeroDivisionError:
            display.insert(0, "Error")

# Створення вікна
root = Tk()
root.title("Калькулятор")

# Відображення введення та результату
display = Entry(root, font=("Arial", 18), width=14, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Створення кнопок
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Додавання кнопок до вікна
for (text, row, col) in buttons:
    button = Button(root, text=text, font=("Arial", 18), padx=20, pady=15,
                    command=lambda t=text: button_click(t) if t != "=" else button_equal())
    button.grid(row=row, column=col)

# Кнопка очищення
clear_button = Button(root, text="C", font=("Arial", 18), padx=20, pady=15, command=button_clear)
clear_button.grid(row=5, column=0, columnspan=2)

# Кнопки для арифметичних операцій
add_button = Button(root, text="+", font=("Arial", 18), padx=20, pady=15, command=lambda: button_operation("add"))
add_button.grid(row=1, column=3)
subtract_button = Button(root, text="-", font=("Arial", 18), padx=22, pady=15, command=lambda: button_operation("subtract"))
subtract_button.grid(row=2, column=3)
multiply_button = Button(root, text="*", font=("Arial", 18), padx=20, pady=15, command=lambda: button_operation("multiply"))
multiply_button.grid(row=3, column=3)
divide_button = Button(root, text="/", font=("Arial", 18), padx=22, pady=15, command=lambda: button_operation("divide"))
divide_button.grid(row=4, column=3)

root.mainloop()