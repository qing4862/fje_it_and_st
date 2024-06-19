import json
import argparse
from fje.icon_family import PokerFaceIconFamily, DefaultIconFamily, ConfigurableIconFamily
from fje.strategy import TreeVisualizationStrategy, RectangleVisualizationStrategy
from fje.context import VisualizationContext

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def get_icon_family(icon_family_name):
    with open("config/icon_config.json", "r", encoding='utf-8') as f:
        config = json.load(f)
    if icon_family_name in config["icon_families"]:
        return ConfigurableIconFamily(config["icon_families"][icon_family_name])
    elif icon_family_name == "poker":
        return PokerFaceIconFamily()
    else:
        return DefaultIconFamily()

def main():
    parser = argparse.ArgumentParser(description='Funny JSON Explorer')
    parser.add_argument('-f', '--file', required=True, help='Path to the JSON file')
    parser.add_argument('-s', '--style', required=True, choices=['tree', 'rectangle'], help='Visualization style')
    parser.add_argument('-i', '--icon', required=True, help='Icon family')
    args = parser.parse_args()

    data = load_json(args.file)
    icon_family = get_icon_family(args.icon)

    context = VisualizationContext(TreeVisualizationStrategy() if args.style == 'tree' else RectangleVisualizationStrategy())
    context.execute_strategy(data, icon_family)

if __name__ == '__main__':
    main()
