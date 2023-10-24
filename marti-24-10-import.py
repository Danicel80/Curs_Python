class ExampleJson:
    file_path = "C:\\Users\\LEXX\\PycharmProjects\\Curs_Python\\example.json"

    def read_file(self):
        with open(file=self.file_path, mode="r") as file:
            print(file.readlines())


x = ExampleJson()
x.read_file()
