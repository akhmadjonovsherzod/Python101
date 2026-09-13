class Counter:
    def __init__(self, start=0, stop=None):
        self.start = start
        self.stop = stop

    def get(self):
        return self.start

    def increment(self):
        if self.stop is None:
            self.start += 1
        else:
            if self.start != self.stop:
                self.start += 1
            else:
                print("Maximal value is reached.")