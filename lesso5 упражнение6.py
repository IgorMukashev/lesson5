result_dict = {}
with open("file4") as file:
    for line in file:
        lesson_tupe, *lessons = line.strip()
        lesson_count = [int(lesson.rstrip('(л)(пр)(лаб)')) for lesson in lesson if lesson]
        result_dict.update({lesson_tupe.rstrip(":"): sum(lesson_count)})

print(result_dict)