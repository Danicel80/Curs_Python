import csv
import json
import pandas as pan


class WorkingWitFiles:

    file_path_txt = "C:\\Users\\LEXX\\PycharmProjects\\Curs_Python\\file.txt"
    file_path_csv = "C:\\Users\\LEXX\\PycharmProjects\\Curs_Python\\file.csv"
    file_path_json = "C:\\Users\\LEXX\\PycharmProjects\\Curs_Python\\file.json"
    txt_content = ""
    json_content = {}

    def read_txt_file(self):
        with open(file=self.file_path_txt, mode="r") as file:
            self.txt_content = file.readlines()
            print(self.txt_content)
            for line in file.readlines():
                line = line.strip()
                print(line)

    def write_txt_file(self, v):
        with open(file=self.file_path_txt, mode="w") as file:
            self.txt_content += "\n"+v
            file.writelines(self.txt_content)

    def read_json_file(self):
        with open(file=self.file_path_json, mode="r") as file:
            self.json_content = json.load(file)
            for k, v in self.json_content.items():
                print(f"{k}  -  {v}")

    def write_json_file(self, k, v):
        with open(file=self.file_path_json, mode="w") as file:
            self.json_content[k] = v
            file.write(json.dumps(self.json_content, indent=4))

    def read_csv_file(self):
        with open(file=self.file_path_csv, mode="r+", newline="\n") as file:
            content = pan.read_csv(file)
            print(content.values)
            csvwriter = csv.writer(file)
            csvwriter.writerow([23, "uuuuuuuu", 222])


e = WorkingWitFiles()
e.write_txt_file("Astazi merg la piata")
e.write_json_file("d", "444")
e.read_csv_file()
e.read_txt_file()
e.read_json_file()
