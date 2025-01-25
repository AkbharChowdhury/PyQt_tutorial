class MyCounter:
    counter = 0

    def number(self):
        self.counter += 1
        return self.counter
    def __str__(self):
        return self.number()