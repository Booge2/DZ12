class StringStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = []

    def push(self, string):
        if len(self.stack) < self.max_size:
            self.stack.append(string)
            print(f"Рядок '{string}' завантажено в стек.")
        else:
            print("Стек повний.")

    def pop(self):
        if self.stack:
            popped_string = self.stack.pop()
            print(f"Рядок '{popped_string}' вивантажено з стеку.")
            return popped_string
        else:
            print("Стек порожній.")
            return None

    def count(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.max_size

    def clear(self):
        self.stack.clear()
        print("Стек очищено.")

    def peek(self):
        if self.stack:
            top_string = self.stack[-1]
            print(f"Верхній рядок стека: '{top_string}'")
        else:
            print("Стек порожній. Немає верхнього рядка.")


def main():
    stack_size = int(input("Введіть розмір стека: "))
    stack = StringStack(stack_size)

    while True:
        print("\n--- Stack Operations ---")
        print("1. Завантажити рядок")
        print("2. Вилучити рядок")
        print("3. Порахувати рядки")
        print("4. Перевірка чи порожній стек")
        print("5. Перевірити чи повний стек")
        print("6. Очистити стек")
        print("7. Переглянути верхній рядок")
        print("8. Вихід")

        choice = input("Введіть ваш вибір: ")

        if choice == "1":
            string = input("Введіть рядок: ")
            stack.push(string)
        elif choice == "2":
            stack.pop()
        elif choice == "3":
            string_count = stack.count()
            print(f"Кількість рядків у стеку: {string_count}")
        elif choice == "4":
            empty_status = stack.is_empty()
            print(f"Стек порожній: {'True' if empty_status else 'False'}")
        elif choice == "5":
            full_status = stack.is_full()
            print(f"Стек повний: {'True' if full_status else 'False'}")
        elif choice == "6":
            stack.clear()
        elif choice == "7":
            stack.peek()
        elif choice == "8":
            print("Вихід з програми.")
            break
        else:
            print("Не правильний вибір. Будь ласка, введіть число від 1 до 8.")


if __name__ == "__main__":
    main()


# Завдання 2
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class StringStack:
    def __init__(self):
        self.top = None

    def push(self, string):
        new_node = Node(string)
        new_node.next = self.top
        self.top = new_node
        print(f"Рядок '{string}' завантажено в стек.")

    def pop(self):
        if self.top:
            popped_string = self.top.value
            self.top = self.top.next
            print(f"Рядок '{popped_string}' вивантажено з стеку.")
            return popped_string
        else:
            print("Стек порожній.")
            return None

    def count(self):
        count = 0
        current_node = self.top
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def is_empty(self):
        return self.top is None

    def clear(self):
        self.top = None
        print("Стек очищено.")

    def peek(self):
        if self.top:
            top_string = self.top.value
            print(f"Верхній рядок стека: '{top_string}'")
        else:
            print("Стек порожній. Немає верхнього рядка.")


def main():
    stack = StringStack()

    while True:
        print("\n--- Stack Operations ---")
        print("1. Завантажити рядок")
        print("2. Вилучити рядок")
        print("3. Порахувати рядки")
        print("4. Перевірка чи порожній стек")
        print("5. Очистити стек")
        print("6. Переглянути верхній рядок")
        print("7. Вихід")

        choice = input("Введіть ваш вибір: ")

        if choice == "1":
            string = input("Введіть рядок: ")
            stack.push(string)
        elif choice == "2":
            stack.pop()
        elif choice == "3":
            string_count = stack.count()
            print(f"Кількість рядків у стеку: {string_count}")
        elif choice == "4":
            empty_status = stack.is_empty()
            print(f"Стек порожній: {'True' if empty_status else 'False'}")
        elif choice == "5":
            stack.clear()
        elif choice == "6":
            stack.peek()
        elif choice == "7":
            print("Вихід з програми.")
            break
        else:
            print("Не правильний вибір. Будь ласка, введіть число від 1 до 7.")


if __name__ == "__main__":
    main()
# Завдання 3
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Перемістити диск 1 з {source} на {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Перемістити диск {n} з {source} на {target}")
    hanoi(n - 1, auxiliary, target, source)


n = 3
hanoi(n, 'Перша вежа', 'Третя вежа', 'Друга вежа')
