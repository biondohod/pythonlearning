from prettytable import PrettyTable
from prettytable import from_csv
from prettytable import DOUBLE_BORDER
with open("champions.csv") as file:
    table = from_csv(file)

table.set_style(DOUBLE_BORDER)
table.del_column("Difficulty")
table.align = "r"
table.align["Champion name"] = "c"
table.reversesort = True
print(table.get_string(sortby="Champion name", start=1))
table.border = False
print(table)


