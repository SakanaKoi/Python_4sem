#Напишите код, который по имени метода, заданному строкой, вызовет этот метод в объекте некоторого пользовательского класса.

class Object:
    def calledMethod(self):
        print("\"called Method\" completed")

obj = Object()
mName = 'calledMethod'
method = getattr(obj, mName)
print(method)
method()