a=5
b=6
c=5
d=7
e=10
print(a.__add__(b))
print(a.__lt__(b) and "{a} {b}".format(a=a,b=b))
print(a.__lt__(b) and f"{a} меньше {b}")
print(e.__le__(d) and f"{d} меньше или равно {e}")
print(d.__le__(e) and f"{d} меньше или равно {e}")
print(f"{e.__ne__(a)}: {e.__ne__(a)} {e} не равно {a}")
print(a.__gt__(b) and f"{a} больше {b}")
print(a.__ge__(b) and f"{a} больше или равно {b}")
print(d.__mul__(e) and f"произведение {d} и {e} равно {d.__mul__(e)}")
print(f"целочисленое деление {e} на 6 равно {e.__floordiv__(6)}")
print(f"{e} делим на {e} равно {int(e.__truediv__(e))}")
print(f"{e} делим на {d} остаётся {e.__mod__(d)}")
print(f"деление с остатком {e.__divmod__(d)}")
print(f"возведение в  степень {e.__pow__(2)}")





print("\n--- Побитовые операции с магическими методами ---")
a, b = 5, 3  # 101 и 011

# __and__ (&)   101 & 011 = 001 — биты равны 1 только если оба 1
print(f"{a} & {b} = {a.__and__(b)} (через метод)")
print(f"{a} & {b} = {a & b} (через оператор)")

# __or__ (|)    101 | 011 = 111 — бит равен 1 если хотя бы один 1
print(f"{a} | {b} = {a.__or__(b)}")

# __xor__ (^)   101 ^ 011 = 110  — бит равен 1 если биты разные
print(f"{a} ^ {b} = {a.__xor__(b)}")

# __lshift__ (<<)   101 << 1 = 1010  — добавляет нули справа (умножение на 2ⁿ)
print(f"{a} << 1 = {a.__lshift__(1)}")

# __rshift__ (>>)   101 >> 1 = 10 — убирает биты справа (деление на 2ⁿ)
print(f"{a} >> 1 = {a.__rshift__(1)}")





class Frange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step

    def __iter__(self):
        self.value = self.start - self.step
        return self


    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


fr = Frange(0,2,0.5)

# print(fr.__next__())
# print(fr.__next__())
# print(fr.__next__())
# print(fr.__next__())
# print(fr.__next__())

# print(next(fr))
# print(next(fr))
# print(next(fr))
# print(next(fr))  #вместо этого легче написать способом ниже

for x in fr:
    print(x)

class Frange2D:
    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
        self.rows = rows
        self.fr = Frange(start,stop,step)

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return iter(self.fr)
        else:
            raise StopIteration


fr = Frange2D(0,2,0.5, 4)
for row in fr:
    for x in row:
        print(x, end=" ")
    print()
