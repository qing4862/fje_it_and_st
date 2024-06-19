class VisualizationStrategy:
    def visualize(self, data, icon_family):
        pass

class TreeVisualizationStrategy(VisualizationStrategy):
    def visualize(self, data, icon_family):
        def recurse(data, prefix="", is_last=True, depth=0):
            if isinstance(data, dict):
                items = list(data.items())
                for i, (key, value) in enumerate(items):
                    connector = "└─ " if is_last and i == len(items) - 1 else "├─ "
                    new_prefix = prefix + ("    " if is_last and i == len(items) - 1 else "│   ")
                    icon = icon_family.get_inner_node_icon()
                    if isinstance(value, (dict, list)):
                        print(f"{prefix}{connector}{icon} {key}")
                        recurse(value, new_prefix, is_last=(i == len(items) - 1), depth=depth+1)
                    else:
                        leaf_icon = icon_family.get_leaf_node_icon()
                        if value is not None:
                            print(f"{prefix}{connector}{icon} {key}: {leaf_icon} {value}")
                        else:
                            print(f"{prefix}{connector}{icon} {key}")
            elif data is not None:
                print(f"{prefix}└─ {data}")

        recurse(data)

class RectangleVisualizationStrategy(VisualizationStrategy):
    def visualize(self, data, icon_family):
        lines = []

        def recurse(data, prefix="", is_last=True):
            if isinstance(data, dict):
                items = list(data.items())
                for i, (key, value) in enumerate(items):
                    connector = "└─ " if is_last and i == len(items) - 1 else "├─ "
                    icon = icon_family.get_inner_node_icon()
                    if isinstance(value, (dict, list)):
                        line = f"{prefix}{connector}{icon} {key}"
                        lines.append(line)
                        new_prefix = prefix + ("    " if is_last and i == len(items) - 1 else "│   ")
                        recurse(value, new_prefix, is_last=(i == len(items) - 1))
                    else:
                        leaf_icon = icon_family.get_leaf_node_icon()
                        if value is not None:
                            line = f"{prefix}{connector}{icon} {key}: {leaf_icon} {value}"
                        else:
                            line = f"{prefix}{connector}{icon} {key}"
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
