#Напишите код, который выведет на экране все имена полей объекта произвольного пользовательского класса, кроме служебных имен.

class Object:
    def __init__(self, form, consistency):
        self.form = form
        self.consistency = consistency

p = Object("Square", "Solid")
all_names = dir(p)
print(all_names)

field_names = [name for name in all_names if not name.startswith("__")]
print(",    ".join(field_names))