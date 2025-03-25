# iterable can convert to iterator


numbers = [1, 2, 3, 4, 5, 6]

for num in numbers:
    print(num)


# iter()
# next()

iterNumbers = iter(numbers)

print(next(iterNumbers))
print(next(iterNumbers))
print(next(iterNumbers))
print(next(iterNumbers))
print(next(iterNumbers))
print(next(iterNumbers))
print(next(iterNumbers))
