from collections.abc import Iterator, Iterable

class JsonIterator(Iterator):
    def __init__(self, data):
        self.stack = [(data, iter(data.items()) if isinstance(data, dict) else iter(enumerate(data)))]

    def __next__(self):
        while self.stack:
            parent, iterator = self.stack[-1]
            try:
                key, value = next(iterator)
                if isinstance(value, (dict, list)):
                    self.stack.append((value, iter(value.items()) if isinstance(value, dict) else iter(enumerate(value))))
                return key, value, parent
            except StopIteration:
                self.stack.pop()
        raise StopIteration

class JsonIterable(Iterable):
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return JsonIterator(self.data)
