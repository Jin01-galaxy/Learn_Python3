class MyClass1:
    def __init__(self, text='Nemo'):
        self.text = text
a = MyClass1()
b = MyClass1(text='Swift')
c = MyClass1(text='Mars')

print(a.text)
print(b.text)
print(c.text)