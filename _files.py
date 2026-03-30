import os

def clean_student_profile(raw_student):
    name = raw_student["name"].strip().title()
    roll = int(raw_student["roll"])
    marks = [int(mark.strip()) for mark in raw_student["marks_str"].split(",")]
    return {"name": name, "roll": roll, "marks": marks}


def is_valid_name(name):
    return all(word.isalpha() for word in name.split())


def grade_label(mark):
    if 90 <= mark <= 100:
        return "A+"
    if 80 <= mark <= 89:
        return "A"
    if 70 <= mark <= 79:
        return "B"
    if 60 <= mark <= 69:
        return "C"
    return "F"


def task_1():
    raw_students = [
        {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
        {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
        {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
        {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
        {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
    ]

    cleaned_students = []
    print("Task 1 — Data Parsing & Profile Cleaning")
    for raw_student in raw_students:
        student = clean_student_profile(raw_student)
        cleaned_students.append(student)
        validity = "✓ Valid name" if is_valid_name(student["name"]) else "✗ Invalid name"
        print("================================")
        print(f"Student : {student['name']}")
        print(f"Roll No : {student['roll']}")
        print(f"Marks   : {student['marks']}")
        print("================================")
        print(validity)
        print()

    target = next((s for s in cleaned_students if s["roll"] == 103), None)
    if target:
        print(f"Roll 103 name in ALL CAPS : {target['name'].upper()}")
        print(f"Roll 103 name in lowercase : {target['name'].lower()}")
    print()
    return cleaned_students


def task_2():
    student_name = "Ayesha Sharma"
    subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
    marks = [88, 72, 95, 60, 78]

    print("Task 2 — Marks Analysis Using Loops & Conditionals")
    print(f"Student: {student_name}")
    for subject, mark in zip(subjects, marks):
        print(f"{subject:<10} : {mark:<3} Grade {grade_label(mark)}")

    total = sum(marks)
    average = round(total / len(marks), 2)
    highest_index = marks.index(max(marks))
    lowest_index = marks.index(min(marks))
    print(f"Total marks    : {total}")
    print(f"Average marks  : {average:.2f}")
    print(f"Highest subject: {subjects[highest_index]} ({marks[highest_index]})")
    print(f"Lowest subject : {subjects[lowest_index]} ({marks[lowest_index]})")
    print()

    new_subjects_added = 0
    while True:
        subject_name = input("Enter a new subject name (or type done to finish): ").strip()
        if subject_name.lower() == "done":
            break
        if subject_name == "":
            print("Invalid subject name. Please enter a non-empty name.")
            continue

        marks_input = input(f"Enter marks for {subject_name} (0-100): ").strip()
        if not marks_input.isdigit():
            print("Invalid marks input. Please enter a number between 0 and 100.")
            continue

        mark_value = int(marks_input)
        if mark_value < 0 or mark_value > 100:
            print("Invalid marks range. Please enter a number between 0 and 100.")
            continue

        subjects.append(subject_name)
        marks.append(mark_value)
        new_subjects_added += 1
        print(f"Added {subject_name} with marks {mark_value}.\n")

    updated_average = round(sum(marks) / len(marks), 2) if marks else 0.0
    print(f"New subjects added: {new_subjects_added}")
    print(f"Updated average across all subjects: {updated_average:.2f}")
    print()
    return subjects, marks


def task_3():
    class_data = [
        ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
        ("Rohit Verma",    [55, 68, 49, 72, 61]),
        ("Priya Nair",     [91, 85, 88, 94, 79]),
        ("Karan Mehta",    [40, 55, 38, 62, 50]),
        ("Sneha Pillai",   [75, 80, 70, 68, 85]),
    ]

    print("Task 3 — Class Performance Summary")
    print("Name              | Average | Status")
    print("----------------------------------------")

    pass_count = 0
    fail_count = 0
    averages = []

    for name, marks in class_data:
        avg = round(sum(marks) / len(marks), 2)
        status = "Pass" if avg >= 60 else "Fail"
        averages.append(avg)
        if status == "Pass":
            pass_count += 1
        else:
            fail_count += 1
        print(f"{name:<17} | {avg:7.2f} | {status}")

    topper_index = averages.index(max(averages))
    class_avg = round(sum(averages) / len(averages), 2)

    print()
    print(f"Students passed: {pass_count}")
    print(f"Students failed: {fail_count}")
    print(f"Class topper   : {class_data[topper_index][0]} ({averages[topper_index]:.2f})")
    print(f"Class average  : {class_avg:.2f}")
    print()


def task_4():
    essay = (
        "  python is a versatile language. it supports object oriented, functional, and procedural programming. "
        "python is widely used in data science and machine learning.  "
    )

    clean_essay = essay.strip()
    print("Task 4 — String Manipulation Utility")
    print(f"Clean essay: {clean_essay}")
    print(f"Title Case: {clean_essay.title()}")
    print(f"Python count: {clean_essay.lower().count('python')}")
    print(f"Replaced essay: {clean_essay.replace('python', 'Python 🐍')}")

    sentences = clean_essay.split('. ')
    print(f"Sentences list: {sentences}")
    print("Numbered sentences:")
    for index, sentence in enumerate(sentences, start=1):
        sentence = sentence.strip()
        if not sentence.endswith('.'):
            sentence = sentence + '.'
        print(f"{index}. {sentence}")
    print()


def task_5():
    notes_path = os.path.join(os.path.dirname(__file__), "python_notes.txt")
    initial_lines = [
        "Topic 1: Variables store data. Python is dynamically typed.",
        "Topic 2: Lists are ordered and mutable.",
        "Topic 3: Dictionaries store key-value pairs.",
        "Topic 4: Loops automate repetitive tasks.",
        "Topic 5: Exception handling prevents crashes.",
    ]
    extra_lines = [
        "Topic 6: Functions help organize reusable code.",
        "Topic 7: File I/O enables data persistence.",
    ]

    with open(notes_path, "w", encoding="utf-8") as notes_file:
        for line in initial_lines:
            notes_file.write(line + "\n")
    print("File written successfully.")

    with open(notes_path, "a", encoding="utf-8") as notes_file:
        for line in extra_lines:
            notes_file.write(line + "\n")
    print("Lines appended.")

    with open(notes_path, "r", encoding="utf-8") as notes_file:
        lines = [line.rstrip("\n") for line in notes_file]

    print("\nFile contents:")
    for index, line in enumerate(lines, start=1):
        print(f"{index}. {line}")

    print(f"\nTotal number of lines: {len(lines)}")

    keyword = input("Enter a keyword to search for: ").strip()
    if keyword == "":
        print("No keyword entered. Skipping search.")
        return

    matches = [line for line in lines if keyword.lower() in line.lower()]
    if matches:
        print("\nMatching lines:")
        for match in matches:
            print(match)
    else:
        print(f"No lines found containing '{keyword}'.")
    print()


def main():
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()


if __name__ == "__main__":
    main()
