class IconFamily:
    def get_inner_node_icon(self):
        pass

    def get_leaf_node_icon(self):
        pass

class DefaultIconFamily(IconFamily):
    def get_inner_node_icon(self):
        return ""

    def get_leaf_node_icon(self):
        return ""

class PokerFaceIconFamily(IconFamily):
    def get_inner_node_icon(self):
        return "♢"

    def get_leaf_node_icon(self):
        return "♤"

class ConfigurableIconFamily(IconFamily):
    def __init__(self, config):
        self.config = config

    def get_inner_node_icon(self):
        return self.config.get("inner_node_icon", "")

    def get_leaf_node_icon(self):
        return self.config.get("leaf_node_icon", "")
