class TreeVisualizer:
    def visualize(self, data, icon_family):
        def recurse(data, depth=0, prefix=""):
            if isinstance(data, dict):
                items = list(data.items())
                for i, (key, value) in enumerate(items):
                    is_last = i == len(items) - 1
                    connector = "└─ " if is_last else "├─ "
                    new_prefix = prefix + ("    " if is_last else "│   ")
                    icon = icon_family.get_inner_node_icon()
                    print(f"{prefix}{connector}{icon} {key}", end="")
                    if isinstance(value, (dict, list)):
                        print()
                        recurse(value, depth + 1, new_prefix)
                    elif value is None:
                        print()
                    else:
                        leaf_icon = icon_family.get_leaf_node_icon()
                        print(f": {leaf_icon} {value}")
            elif isinstance(data, list):
                for i, item in enumerate(items):
                    is_last = i == len(items) - 1
                    connector = "└─ " if is_last else "├─ "
                    new_prefix = prefix + ("    " if is_last else "│   ")
                    icon = icon_family.get_inner_node_icon()
                    print(f"{prefix}{connector}{icon} {item}")
                    recurse(item, depth + 1, new_prefix)
            else:
                leaf_icon = icon_family.get_leaf_node_icon()
                print(f"{prefix}└─ {leaf_icon} {data}")

        recurse(data)

class RectangleVisualizer:
    def visualize(self, data, icon_family):
        lines = []

        def recurse(data, depth=0, prefix=""):
            if isinstance(data, dict):
                items = list(data.items())
                for i, (key, value) in enumerate(items):
                    connector = "├─ " if i == 0 else "└─ "
                    icon = icon_family.get_inner_node_icon()
                    line = f"{prefix}{connector}{icon} {key}"
                    lines.append(line)
                    if isinstance(value, (dict, list)):
                        new_prefix = prefix + ("│  " if i == 0 else "   ")
                        recurse(value, depth + 1, new_prefix)
                    elif value is not None:
                        leaf_icon = icon_family.get_leaf_node_icon()
                        line = f"{line}: {leaf_icon} {value}"
                        lines[-1] = line
            elif isinstance(data, list):
                for i, item in enumerate(items):
                    connector = "├─ " if i == 0 else "└─ "
                    icon = icon_family.get_inner_node_icon()
                    line = f"{prefix}{connector}{icon} {item}"
                    lines.append(line)
                    recurse(item, depth + 1, prefix + ("│  " if i == 0 else "   "))
            else:
                leaf_icon = icon_family.get_leaf_node_icon()
                line = f"{prefix}└─ {leaf_icon} {data}"
                lines.append(line)

        recurse(data)

        max_length = max(len(line) for line in lines)
        border_line = "─" * (max_length + 2)

        def print_line(line, end_char):
            print(f"│ {line.ljust(max_length, '─')} {end_char}")

        print(f"┌{border_line}┐")
        for i, line in enumerate(lines):
            end_char = "│"
            if i == len(lines) - 1:
                print_line(line, "┘")
            else:
                next_line = lines[i + 1]
                if "└─ " in next_line or "├─ " in next_line:
                    end_char = "┤"
                print_line(line, end_char)
        print(f"└{border_line}┘")
