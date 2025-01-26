class MyCounter:
    def __init__(self, start_index=0):
        self._num = start_index

    def get_counter(self):
        self._num += 1
        return self._num