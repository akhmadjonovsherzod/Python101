class HistoryDict:
    def __init__(self, dictionary):
        self.dict = dictionary
        self.history = []

    def set_value(self, key, value):
        if key not in self.dict or self.dict[key] != value:
            self.dict[key] = value
            self.history.append(key)

            if len(self.history) > 5:
                self.history.pop(0)

    def get_history(self):
        return self.history


d = HistoryDict({"foo": 42})
d.set_value("bar", 43)

print(d.get_history())