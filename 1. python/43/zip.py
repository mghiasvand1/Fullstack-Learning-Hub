# numbers_1 = [1, 2, 3, 4, 5]
# numbers_2 = [5, 6, 7, 8, 9, 10]

# result = zip(numbers_1, numbers_2)

# # print(list(result))
# # print(dict(result))

# myList = [(1, 5), (3, 7), (6, 4), (7, 9)]

# print(list(zip(*myList)))


students = ["mohammad", "iman", "sara"]
midterm = [78, 80, 94]
final = [90, 88, 92]

# {"mohammad": 90, "iman": 88, "sara": 94}

# finalGrades = [pair for pair in zip(students,midterm, final)]

finalGrades = {t[0]: max(t[1], t[2]) for t in zip(students, midterm, final)}
print(finalGrades)

average = zip(
    students,
    map(
        lambda pair: (pair[0] + pair[1]) / 2,
        zip(midterm, final)
    )
)

print(dict(average))

