# avem nevoie de o singura instanta pe tot parcursul proiectului
# cum ar fi o baza de date sau o clasa utilitara ce lucreaza cu fisiere
# """""""obiect ce se instantiaza o singura data"""""""

class SingletonClass:
    __instanta = None
    bec = False
    kilometraj = 0
    destination_path = "/home/daniel/backup_logs"
    source_path = "/home/daniel/logs"
    #putem sa punem cate atribute vrem noi aici

    def __init__(self, bec=False):
        self.bec = bec

    # new pentru singleton
    # def __new__(cls, *args, **kwargs):
    #     if cls.__instanta is None:
    #         # aceast obiect se instantiaza o singura data in a lifetime
    #         cls.__instanta = object.__new__(cls)
    #
    #     # de vreme ce instanta noastra a fost creeata la inceput
    #     # urmatoarele instante vor fi identice cu aceasta
    #     return cls.__instanta

    def __new__(cls, *args, **kwargs):
        cls.__instanta = object.__new__(cls)
        return cls.__instanta

    def move_logs(self):
        pass
    def move(self):
        self.kilometraj += 100

    def aprinde_bec(self):
        self.bec = True

    def stinge_bec(self):
        self.bec = False

    def __str__(self):
        return f"km {self.kilometraj}"


instance1 = SingletonClass(bec=True)
instance1.move()
instance1.move()

instance2 = SingletonClass()
instance2.move()
instance2.move()
instance3 = SingletonClass(bec=True)
instance3.move()

# is verifica egalitatea a 2 obiecte in totalitate(valoare dar si adresa de memorie)
if instance1 is instance2 and instance2 is instance3:
    print("toate instantele sunt la fel")


class PresedinteRomania:
    _instance = None  # Variabila pentru a stoca instanta unica

    def __new__(cls):
        # Verificăm dacă instanța există deja
        if not cls._instance:
            # Dacă nu există, creăm instanța și o stocăm în variabila de clasă
            cls._instance = super(PresedinteRomania, cls).__new__(cls)
        return cls._instance

    def __str__(self):
        return "Eu sunt presedintele Romaniei"

    def say_hello(self):
        return f'Salut! {self}'

# Testăm Singleton
a = PresedinteRomania()
b = PresedinteRomania()

print(f'ID(a) = {id(a)}')
print(f'ID(b) = {id(b)}')
print(f'Acelasi obiect? {a is b}')