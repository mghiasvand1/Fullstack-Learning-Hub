class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            num = self.current
            self.current += 1
            return num
        raise StopIteration


myCounter = Counter(10, 20)

for num in myCounter:
    print(num)

range(3, 10, 2)
# for num in Counter(10, 30):
#     print(num)


# for num in range(10, 30):
#     print(num)
#
# list
