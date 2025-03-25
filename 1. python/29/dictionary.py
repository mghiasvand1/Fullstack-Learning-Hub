course = {
    "title": "Python Course",
    "teacher": "Mohammad Ordooknani",
    "Time": 8.5,
    "videoCount": 30,
    "tags": ["python", "online course", "free python course"],
    "shortLink": "toplearn.com/c/o2V3",
    "sessions": [
        {
            "title": "session-1",
            "time": 5
        },
        {
            "title": "session-2",
            "time": 7
        },
        {
            "title": "session-3",
            "time": 9
        }
    ],
    "relatedCourses": [
        {
            "title": "Java Course",
            "teacher": "Mohammad Ghari",
            "Time": 20,
            "videoCount": 42,
            "tags": ["java", "online course", "free java course"],
            "shortLink":"toplearn.com/c/82m",
        },
        {
            "title": "CSharp Course",
            "teacher": "Iman Madaeny",
            "Time": 10,
            "videoCount": 22,
            "tags": ["csharp", "online course", "free csharp course"],
            "shortLink":"toplearn.com/c/mZO",
        }
    ]
}


# for related in course["relatedCourses"]:
#     print(related["title"])

total_time = 0

for session in course["sessions"]:
    total_time += session["time"]

print(total_time)