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


def get_active_students(data):
    return tuple(student for student, info in data["studenter"] if info["aktiv"])



def active_students_subjects(data):
    subjects = set()

    for name, info in data["studenter"]:
        if info["aktiv"]:
            print(f"{name} is studying: {", ".join(info["ämnen"])}")
            subjects.update(info["ämnen"])

    return subjects

# call functions
active_students = get_active_students(data)

print(f"The current active students are: {active_students}")

unique_subjects = active_students_subjects(data)