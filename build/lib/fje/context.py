class VisualizationContext:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def execute_strategy(self, data, icon_family):
        self._strategy.visualize(data, icon_family)
