import json
import sys
from fje.factories import TreeVisualizerFactory, RectangleVisualizerFactory

class JSONExplorer:
    def __init__(self, file, style, icon_family):
        self.file = file
        self.style = style
        self.icon_family = icon_family

    def run(self):
        with open(self.file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if self.style == "tree":
            factory = TreeVisualizerFactory()
        elif self.style == "rectangle":
            factory = RectangleVisualizerFactory()
        else:
            print("Unsupported style")
            return

        visualizer = factory.create_visualizer()
        icons = factory.create_icon_family(self.icon_family)
        visualizer.visualize(data, icons)

def main():
    if len(sys.argv) != 7:
        print("Usage: fje -f <json file> -s <style> -i <icon family>")
    else:
        file = sys.argv[2]
        style = sys.argv[4]
        icon_family = sys.argv[6]

        explorer = JSONExplorer(file, style, icon_family)
        explorer.run()
