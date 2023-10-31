file_path_txt = "C:\\Users\\LEXX\\PycharmProjects\\Curs_Python\\file.txt"
lista = ["Go", "Kotlin", "Swift"]


def read_txt():
    with open(file=file_path_txt, mode="r") as file:
        print(file.readlines())


def write_txt():
    with open(file=file_path_txt, mode="a") as file:
        for s in lista:
            file.write(s + "\n")


read_txt()
write_txt()
read_txt()
