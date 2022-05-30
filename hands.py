import numpy as np


class Hands:
    """
    Class to handle all functions relating to processing of hand coordinates
    This will run in the same process as main program

    handles drawing, fetching data from process queue and gesture prediction
    """

    def __init__(self):
        self.hand_coordinates = None  # Will hold hand coordinate data
        pass

    def draw(self):
        # TODO
        pass

    def update(self, queue):
        self.hand_coordinates = queue.get()

    def predict(self):
        # TODO
        pass
