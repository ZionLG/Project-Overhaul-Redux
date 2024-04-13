def format_warband_script(script):
    indent_level = 0
    formatted_script = ""
    for line in script.splitlines():
        stripped = line.lstrip()
        leading_spaces = len(line) - len(stripped)
        if stripped in ["(try_begin),", "(else_try),"]:
            formatted_script += " " * leading_spaces + "\t" * indent_level + stripped + "\n"
            indent_level += 1
        elif stripped == "(try_end),":
            indent_level -= 1
            formatted_script += " " * leading_spaces + "\t" * indent_level + stripped + "\n"
        else:
            formatted_script += " " * leading_spaces + "\t" * indent_level + stripped + "\n"
    return formatted_script

def format_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    formatted_content = format_warband_script(content)
    with open(filename, 'w') as file:
        file.write(formatted_content)

format_file('module_scripts.py')