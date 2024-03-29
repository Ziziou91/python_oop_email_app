"""Functions to aid in the formatting and layout of text to be printed to the user CLI."""
import math

class Color:
    """Allows easier formatting of string color."""
    purple = '\033[95m'
    cyan = '\033[96m'
    darkcyan = '\033[36m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    bold = '\033[1m'
    underline = '\033[4m'
    end = '\033[0m'

def create_char_line(char:str="-", count:int=79) -> str:
    """Creates a line of characters for formatting in the terminal."""
    return f"{char*count}"

def create_title(title_str:str, line_width:int=79) -> str:
    """Creates a box that includes a title string to help the user navigate through the app."""
    box_length = 22
    internal_space = int((box_length-len(title_str))/2)
    outside_space = int((line_width/2) - (box_length/2))
    if len(title_str) % 2:
        return f"{" "*outside_space}{'-'*24}\n{" "*outside_space}|{' '*internal_space}{title_str}{' '*(internal_space+1)}|\n{" "*outside_space}{'-'*24}"
    else:
        return f"{" "*outside_space}{'-'*24}\n{" "*outside_space}|{' '*internal_space}{title_str}{' '*(internal_space)}|\n{" "*outside_space}{'-'*24}"


# ==============Logic to build table for printing============
def create_table_cell(item:str, cell_width:int) -> str:
    """Creates each cell to populate a table of values generated by create_line."""
    spacing = (cell_width - len(str(item))) / 2
    if spacing.is_integer():
        return f"{' '*int(spacing)}{item}{' '*int(spacing)}"
    else:
        return f"{' '*int(math.floor(spacing))}{item}{' '*int(math.ceil(spacing))}"


def create_table_row(cell_1_string:str="Number", cell_2_string: float="Subject") -> str:
    """Creates each line in a table of menu items, prices, stock and stock value."""
    cell_2_width = 60

    if len(cell_2_string) > cell_2_width:
        table_row = create_multi_line_table_row(cell_1_string, cell_2_string, cell_2_width)
    else:
        table_row = f"|{create_table_cell(cell_1_string, 16)}|{create_table_cell(cell_2_string, cell_2_width)}|"

    return table_row


def create_multi_line_table_row(cell_1_string:str, cell_2_string:str, cell_2_width:int) -> str:
    """Creates table rows of height more than 1. Required when cell_2_string string is longer than cell_2_width."""
    table_row = ""
    remaining_str = cell_2_string

    # Keep looping while there is still text to be added to a subsequent line of table_row.
    while len(remaining_str) > cell_2_width:
        cell_2_list = remaining_str[0:cell_2_width].split(" ")
        current_line = " ".join(cell_2_list[0:-1])
        remaining_str = cell_2_list[-1] + remaining_str[cell_2_width:]
        table_row += f"|{create_table_cell(cell_1_string, 16)}|{create_table_cell(current_line, cell_2_width)}|\n"
        cell_1_string = ""

    # Add final line to table_row.
    table_row += f"|{create_table_cell("", 16)}|{create_table_cell(remaining_str, cell_2_width)}|"
    print(table_row)
    return table_row
