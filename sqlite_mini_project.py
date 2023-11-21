import os
import sqlite3
import io
from contextlib import redirect_stdout


def add_border(function):
    def inside_f(*args):
        result = io.StringIO()
        with redirect_stdout(result):
            function(*args)
        max_line_length = 0
        result_list = result.getvalue().split("\n")
        for line in result_list:
            line_l = len(line)
            if max_line_length < line_l:
                max_line_length = line_l
        dec = ""
        for i in range(max_line_length+10):
            dec += "*"
        print(dec)
        space_front = "    "
        for line in result_list:
            space_end = ""
            space_end += " "*(max_line_length + 4 - len(line))
            print(f"*{space_front}{line}{space_end}*")
        print(dec)
    return inside_f


class ManageDb:
    db_list = []
    db_in_use = ""
    con = None
    cursor = None
    table = ""

    def __init__(self):
        # create or update a list with all db files from current folder
        self.update_db_list()

    # update db_list
    def update_db_list(self):
        self.db_list.clear()
        for file in os.listdir():
            if file.endswith(".db"):
                self.db_list.append(file.split(".")[0])

    # use a specific db
    def use_db(self, db_name):
        try:
            if self.db_in_use != "":
                self.close_db()
            self.db_in_use = db_name
            self.con = sqlite3.connect(self.db_in_use + ".db")
            if self.db_in_use not in self.db_list:
                self.update_db_list()
            self.cursor = self.con.cursor()
            self.con.commit()
        except Exception as err:
            print(f"DB connect Failed: {str(err)}")

    def del_db(self, db_name):
        warning_answer = input("Warning no turning back, are you sure? 'y / n':   ").lower()
        if warning_answer == "y":
            if db_name in self.db_list:
                if db_name == self.db_in_use:
                    self.close_db()
                try:
                    if os.path.exists(f"{db_name}.db"):
                        os.remove(f"{db_name}.db")
                    else:
                        raise FileNotFoundError
                except (FileNotFoundError, IOError):
                    print("Error File or Path Not Found")
                finally:
                    self.update_db_list()
            else:
                print(f"Database {db_name} is not in the list")
        else:
            print("Answer not recognized, Deletion Cancelled")

    @add_border
    # show all db from a list created after scanning the folder
    def show_all_db(self):
        for db in self.db_list:
            print(db)

    @add_border
    def show_db(self):
        if self.db_in_use != "":
            print(self.db_in_use)
        else:
            print("No db selected")

    # use a specific table
    def use_table(self, tb_name):
        if self.db_in_use != "":
            self.table = tb_name
        else:
            print("No db selected. Run 'use_db' first to select a database")

    @add_border
    # show all tables from selected db
    def show_all_tb(self):
        if self.db_in_use != "":
            try:
                self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = self.cursor.fetchall()
                for table_name in tables:
                    print(table_name[0])
            except Exception as err:
                print(f"Query Failed: {str(err)}")
        else:
            print("No db selected. Run 'use_db' first to select a database")

    @add_border
    # show all column names in a single line
    def show_tb_col(self):
        if self.table != "":
            try:
                self.cursor.execute(f"SELECT * FROM {self.table};")
                col_str = ""
                for col in self.cursor.description:
                    col_str += col[0] + "     "
                print(col_str)
            except Exception as err:
                print(f"Query Failed: {str(err)}")
        else:
            print("Missing table name. Run 'use_table' first")

    # create table
    def create_table(self, table):
        if self.db_in_use != "":
            content = input("Enter column names and attributes, divided by ',':\n")
            try:
                self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table}({content});")
                self.con.commit()
            except Exception as err:
                print(f"Query Failed: {str(err)}")
        else:
            print("No db selected. Run 'use_db' first to select a database")

    def del_tb(self, table_to_del):
        if self.db_in_use != "":
            warning_answer = input("Warning, no turning back, are you sure? 'y / n':   ").lower()
            if warning_answer == "y":
                try:
                    self.cursor.execute(f"DROP TABLE {table_to_del}")
                    self.con.commit()
                    if table_to_del == self.table:
                        self.table = ""
                except Exception as err:
                    print(f"Deletion Failed:  {err}")
            else:
                print("Answer not recognized, Deletion Cancelled")
        else:
            print("No db selected. Run 'use_db' first to select a database")

    # insert info in existing table
    def insert(self):
        if self.table != "":
            self.show_tb_col()
            col = input("Insert column names separated by ',':\n")
            val = input("Insert values in order, separated by '$$':\n")
            val_tuple = tuple(val.split("$$"))
            try:
                self.cursor.execute(f"INSERT INTO {self.table} ({col}) VALUES {val_tuple};")
                self.con.commit()
            except Exception as err:
                print(f"Query Failed: {str(err)}")
        else:
            print("Missing table name. Run 'use_table' first")

    #@add_border not working
    # get data from database, WHERE clause is optional
    def select(self):
        if self.table != "":
            col = input("Insert column names separated by ',':\n")
            where = input("Insert 'WHERE' clause if necessary (ex: column_name = 42):\n")
            try:
                if where != "":
                    self.cursor.execute(f"SELECT {col} FROM {self.table} where {where};")
                else:
                    self.cursor.execute(f"SELECT {col} FROM {self.table};")
                data = self.cursor.fetchall()
                for row in data:
                    print(row)
            except Exception as err:
                print(f"Select Error:  {err}")
        else:
            print("Missing table name. Run 'use_table' first")

    def update(self):
        if self.table != "":
            data = input("Insert column-values separated by ',' (ex: column_name=test1, column_name2=test2):\n")
            where = input("Insert 'WHERE' clause (ex: column_name = 42):\n")
            try:
                if where != "":
                    self.cursor.execute(f"UPDATE {self.table} SET {data} where {where};")
                    self.con.commit()
                else:
                    print("'Where' is empty")
            except Exception as err:
                print(f"Update Error: {err}")
        else:
            print("Missing table name. Run 'use_table' first")

    def delete(self, where):
        if self.table != "":
            try:
                if where != "":
                    self.cursor.execute(f"DELETE FROM {self.table} WHERE {where};")
                    self.con.commit()
                else:
                    print("Without 'where' all records will be deleted.")
                    answer = input("Delete all??? 'y / n':   ")
                    if answer == "y":
                        self.cursor.execute(f"DELETE FROM {self.table};")
                        self.cursor.execute(f"DELETE FROM sqlite_sequence WHERE name = '{self.table}';")
                        self.con.commit()
                    elif answer == "n":
                        n_where = input("Input 'WHERE' clause:   ")
                        self.delete(n_where)
                    else:
                        print("Answer not recognized, abort Delete")
            except Exception as err:
                print(f"Delete Error:  {err}")
        else:
            print("Missing table name. Run 'use_table' first")

    def close_db(self):
        if self.db_in_use != "":
            self.con.close()
            self.db_in_use = ""
            self.table = ""

    @staticmethod
    @add_border
    def info():
        print("The app is just a test")
        print("It is a very simple database manager")
        print("v1.0 - Created by Danicel Alexandru")
        print("Date 8.11.2023")

    @staticmethod
    @add_border
    def help():
        print("end or exit - Exit application")
        print("create_db name - Creates specified (name) database and connects to it")
        print("show_all_db - Shows all db files from current folder")
        print("use_db name - Use specified (name) db file, it will be created if does not exists")
        print("show_db - Show db in use")
        print("delete_db name - Delete specified (name) database")
        print("use_table name - Use specified (name) table from selected database")
        print("show_all_tb - Show all tables from selected database")
        print("show_tb_col - Show columns from selected table")
        print("create_table name - Creates specified (name) table in selected database")
        print("delete_table name - Delete specified (name) table from selected database")
        print("insert - Insert data in selected table")
        print("select - Get data from selected table")
        print("update - Change data in selected table")
        print("delete where - Delete selected record, delete all records if no 'WHERE' clause")
        print("about - Info about app")

    # main part, infinite while to receive commands from user
    def run(self):
        end = False
        # param is for certain functions that need an extra value
        param = ""
        print("Welcome. Enter 'h' or 'help' for a list of commands, 'exit' to exit the app")
        while end != True:
            try:
                command_list = input("Enter command\n---  ").split(" ")
                command = command_list[0]
                if len(command_list) > 1:
                    param = command_list[1]
                elif command == "create_db":
                    self.use_db(param)
                if command == "show_all_db":
                    self.show_all_db()
                elif command == "show_db":
                    self.show_db()
                elif command == "use_db":
                    self.use_db(param)
                elif command == "delete_db":
                    self.del_db(param)
                elif command == "use_table":
                    self.use_table(param)
                elif command == "show_all_tb":
                    self.show_all_tb()
                elif command == "show_tb_col":
                    self.show_tb_col()
                elif command == "create_table":
                    self.create_table(param)
                elif command == "delete_table":
                    self.del_tb(param)
                elif command == "insert":
                    self.insert()
                elif command == "select":
                    self.select()
                elif command == "update":
                    self.update()
                elif command == "delete":
                    self.delete(param)
                elif command == "h" or command == "help":
                    self.help()
                elif command == "about":
                    self.info()
                elif command == "end" or command == "exit":
                    end = True
                    self.close_db()
                    print("Goodbye")
                else:
                    print(f"Command  {command}  is not a proper command, enter 'h' or 'help' for a command list")
            except KeyboardInterrupt:
                end = True
                self.close_db()
                print("Goodbye")


x = ManageDb()
x.run()
