import io
from contextlib import redirect_stdout
# Este numai pentru functii care afiseaza un rezultat


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
