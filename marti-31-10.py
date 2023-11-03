import random


# class ReversIterator:
#     def __init__(self, note):
#         self.i = iter(note[::-1])
#
#     def __iter__(self):
#         return self.i
#
#     def __next__(self):
#         return next(self.i)
#
#
# n = [1, 2, 3, 4, 5]

# rev = ReversIterator(n)
# print(next(rev))
# print(next(rev))


class Autovehicul:
    culoare = ""

    def __init__(self):
        self.culoare = "alb"

    @property
    def p_culoare(self):
        return self.culoare

    @p_culoare.setter
    def p_culoare(self, c):
        self.culoare = c

    # @property
    # def temp_cc(self):
    #     return str(self.temp)
    #
    # @temp_cc.setter
    # def temp_cc(self, t):
    #     self.temp = t

    # @temp.getter
    # def temp(self):
    #    return str(self._temp)


class Masina(Autovehicul):
    # culoare = "rosu"
    pass


a = Autovehicul()
# a._culoare = "gri"
print(a.culoare)
a.culoare = "verde"
print(a.culoare)
b = Masina()
b.culoare = "xxx"
print(b.culoare)
print(a.culoare)
print("---------")


def gen():
    total_nr = 0
    while True:
        if total_nr >= 6:
            nr = "All 6 nr are out"
        else:
            nr = random.randint(6, 49)
        yield nr
        total_nr += 1


gen_nr = gen()
print(next(gen_nr))
print(next(gen_nr))
print(next(gen_nr))
print(next(gen_nr))
print(next(gen_nr))
print(next(gen_nr))
print(next(gen_nr))
print(next(gen_nr))
print(next(gen_nr))
# for nr in gen_nr:
#    print(nr)
