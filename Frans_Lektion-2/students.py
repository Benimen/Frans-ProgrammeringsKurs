data = {
    "studenter": [
        ("Alice", {"ålder": 25, "ämnen": ("Matematik", "Fysik"), "aktiv": True}),
        ("Bob", {"ålder": 22, "ämnen": ("Biologi",), "aktiv": False}),
        ("Charlie", {"ålder": 23, "ämnen": ("Matematik", "Biologi"), "aktiv": True}),
        ("Diana", {"ålder": 24, "ämnen": ("Fysik",), "aktiv": False}),
        ("Eve", {"ålder": 21, "ämnen": ("Matematik", "Fysik", "Biologi"), "aktiv": True}),
    ],
    "kurser": {
        "Matematik": {"studenter": {"Alice", "Charlie", "Eve"}},
        "Fysik": {"studenter": {"Alice", "Diana", "Eve"}},
        "Biologi": {"studenter": {"Bob", "Charlie", "Eve"}},
    }
}

#Create a tuple for active students
def get_active_students(data):
    return tuple(
    name for name, info in data["studenter"] if info["aktiv"]
)

#Create a tuple for inactive students
def get_inactive_students(data):
    return tuple(
    name for name, info in data["studenter"] if not info["aktiv"]
)



active_students = get_active_students(data)
inactive_students = get_inactive_students(data)


print("These students are active", active_students)
print("These students are inactive: ", inactive_students)