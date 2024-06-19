import json
from fje.visualizer import TreeVisualizer, RectangleVisualizer
from fje.icon_family import PokerFaceIconFamily, DefaultIconFamily, ConfigurableIconFamily

class VisualizerFactory:
    def create_visualizer(self):
        pass

    def create_icon_family(self, icon_family):
        pass

class TreeVisualizerFactory(VisualizerFactory):
    def create_visualizer(self):
        return TreeVisualizer()

    def create_icon_family(self, icon_family):
        with open("config/icon_config.json", "r", encoding='utf-8') as f:
            config = json.load(f)
        if icon_family in config["icon_families"]:
            return ConfigurableIconFamily(config["icon_families"][icon_family])
        elif icon_family == "poker":
            return PokerFaceIconFamily()
        else:
            return DefaultIconFamily()

class RectangleVisualizerFactory(VisualizerFactory):
    def create_visualizer(self):
        return RectangleVisualizer()

    def create_icon_family(self, icon_family):
        with open("config/icon_config.json", "r", encoding='utf-8') as f:
            config = json.load(f)
        if icon_family in config["icon_families"]:
            return ConfigurableIconFamily(config["icon_families"][icon_family])
        elif icon_family == "poker":
            return PokerFaceIconFamily()
        else:
            return DefaultIconFamily()
