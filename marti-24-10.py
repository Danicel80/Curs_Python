import json


class Todolist:
    todo = {}
    file_addr = "C:\\Users\\LEXX\\PycharmProjects\\Curs_Python\\todo.json"

    def insert_task(self, key, value):
        self.todo.update({key: value})

    def end_task(self, task_name):
        self.todo.pop(task_name)

    def show_todo_keys(self):
        print(self.todo.keys())

    def show_all(self):
        print("===============================================")
        for k, v in self.todo.items():
            print(f"{k}  -  {v}")
        print("===============================================")

    def __create_file(self):
        file = open(file=self.file_addr, mode="w")
        file.writelines("{}")
        file.close()

    def save_todo_file(self):
        file = open(file=self.file_addr, mode="w")
        for_file = json.dumps(self.todo, indent=4)
        file.write(for_file)
        file.close()

    def read_todo_file(self):
        try:
            file = open(file=self.file_addr, mode="r+")
        except FileNotFoundError:
            self.__create_file()
            file = open(file=self.file_addr, mode="r+")
        self.todo = json.loads(file.read())
        file.close()

    def run(self):
        self.read_todo_file()
        end = False
        while end != True:
            command = input("insert command ").lower()
            if command == "insert_task":
                self.insert_task(input("enter name: "), input("enter value: "))
            elif command == "show_keys":
                self.show_todo_keys()
            elif command == "show_key_detail":
                self.show_task(input("Enter task name: "))
            elif command == "end_task":
                self.end_task(input("Enter task to end: "))
            elif command == "show_all":
                self.show_all()
            elif command == "info":
                self.__info()
            elif command == "help" or command == "h":
                print("===================================================")
                print("|  insert_task - insert a new task                |")
                print("|  show_keys - shows all tasks                    |")
                print("|  show_key_detail - shows a task detail          |")
                print("|  show_all - shows all todo tasks with details   |")
                print("|  end_task - delete a task                       |")
                print("|  info - info about the app                      |")
                print("|  exit app - end                                 |")
                print("===================================================")
            elif command == "end":
                end = True
                self.save_todo_file()
            else:
                print(f"Command  {command}  is not a proper command, enter 'h' or 'help' for a command list")

    def __info(self):
        print("===============================================")
        print("| This app is created by Danicel Alexandru    |")
        print("| The app is just a test, i am still learning |")
        print("===============================================")

    def show_task(self, task_name):
        if task_name not in self.todo.keys():
            print(f"task {task_name} is not in list, do you want to add it?")
            answer = input(":")
            if answer == "yes":
                task_detail = input("Please enter task details  ")
                self.insert_task(task_name, task_detail)
            if answer == "no":
                print("Good Bye")
        else:
            print(self.todo[task_name])


first_todo = Todolist()
first_todo.run()
