import requests

# response = requests.get("https://barnamenevisan.info/api/courses/getactivecourses")
# # data = response.text  # string
# jsonData = response.json()
#
# for course in jsonData:
#     print(f"{course['title']} مدرس : {course['teacher']}")

# res = requests.post("https://jsonplaceholder.typicode.com/posts")
# print(res.json())

res = requests.get("https://jsonplaceholder.typicode.com/comments", params={'postId': 2})
# print(res.json())

for data in res.json():
    print(data)
