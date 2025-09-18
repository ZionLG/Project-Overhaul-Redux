def indent_blocks(input_file, output_file):
    indent_level = 0
    block_start = ["try_begin", "try_for_range", "try_for_range_backwards", 
                   "try_for_parties", "try_for_agents", "try_for_prop_instances", "try_for_players"]
    block_end = ["try_end", "end_try"]
    block_else = ["else_try", "else_try_begin"]
    block_start_open = False

    with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
        for line in in_file:
            stripped = line.lstrip()
            if any(bs in stripped for bs in block_start + block_end + block_else):
                index = min(stripped.index(bs) for bs in block_start + block_end + block_else if bs in stripped)
                if index > 0 and stripped[index - 1] == ':':
                    # This is a variable assignment, ignore it
                    out_file.write(line)
                    continue
            if block_start_open:
                out_file.write("\t" * indent_level + line)
                if ")" in stripped:
                    block_start_open = False
                    indent_level += 1
            elif any(bs in stripped for bs in block_start):
                if ")" in stripped:
                    out_file.write("\t" * indent_level + line)
                    indent_level += 1
                else:
                    out_file.write("\t" * indent_level + line)
                    block_start_open = True
            elif any(be in stripped for be in block_end):
                indent_level -= 1
                out_file.write("\t" * indent_level + line)
            elif any(be in stripped for be in block_else):
                indent_level -= 1
                out_file.write("\t" * indent_level + line)
                indent_level += 1
            else:
                out_file.write("\t" * indent_level + line)

# Usage: (make sure the file is already FORMATTED, this will only fix indentation!, Black python formatter is used.) NOTE: After you indent, make sure to not use Black formatter again, as it will mess up the indentation.
indent_blocks('systems/plugin_troop_tree_presetation.py', 'systems/plugin_troop_tree_presetation_f.py')