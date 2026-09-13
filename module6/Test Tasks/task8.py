from typing import List


class Counter:
    def __init__(self, values: List[int]):
        self.values = values
    def __add__(self, other):
        return [f"{item} {other}" for item in self.values]