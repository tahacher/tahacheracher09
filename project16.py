def find_duplicates(x):
    seen = set()
    duplicates = set()
    for item in x:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

names = ["Taha", "Mehdi", "Aymen", "Yassine", "Taha", "Mehdi"]
print(find_duplicates(names))  # ['Taha', 'Mehdi']
