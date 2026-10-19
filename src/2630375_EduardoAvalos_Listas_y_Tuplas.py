# =============================================================================
# FRONT PAGE
# =============================================================================
# Name:       Eduardo Avalos Lopez
# Student ID: 2630375
# Group:      TSU-75018 (IM-103)
# Assignment: Programming Methodology
# =============================================================================

# =============================================================================
# EXECUTIVE SUMMARY
# =============================================================================
# A list is an ordered and mutable collection: items can be added, removed or
# changed after it is created. A tuple is also ordered but immutable: once
# created, its items cannot change, which makes it good for fixed data such as
# coordinates or (word, count) records.
# Mutable means the object can be modified in place (list.append); immutable
# means any "change" would need a new object.
# Both collections are read by position (index), starting at 0, and can hold
# other collections, for example a list that contains lists of grades.
# This document covers four problems: a shopping list (list), points and
# distances (tuple), student grades (list of lists) and a word frequency
# counter (list of tuples).
# Each one defines its inputs, outputs, validations and three test cases.
# The program runs the four problems in order; each one asks for its data with
# input() and decides what to show using if / elif / else.

# =============================================================================
# PRINCIPLES AND GOOD PRACTICES
# =============================================================================
# - Use lists when items must be added or removed often.
# - Use tuples for data that must not change (coordinates, fixed records).
# - Do not modify a list while looping over it; build a new list instead
#   (Problem 1 builds items_list from the split pieces).
# - When two lists describe the same items (student_names and student_grades),
#   keep them aligned: position i in one matches position i in the other.
# - Check that an index or a search result is valid before using it.
# - Check that a list is not empty before computing an average.
# - Write readable code and clear messages for the user.
# - Tools used: print, input, len, range, str, float, sum, round, strip,
#   lower, title, split, replace, join, list append, tuple indexing,
#   in / not in, f-strings and if / elif / else.

# -----------------------------------------------------------------------------
# Constants (UPPER_SNAKE_CASE)
# -----------------------------------------------------------------------------
ERROR_MESSAGE = "Error: invalid input"
DIGITS = "0123456789"
DECIMALS = 2
PASSING_GRADE = 70.0
PUNCTUATION = '.,;:!?()"'

# How the number check works (explained once here, used in Problem 2):
#   - Each text may contain digits, at most one '.', and a '-' only as the
#     very first character.
#   - It must contain at least one digit (so "-" or "." alone are rejected).


# =============================================================================
# Problem 1: Shopping list basics (list operations)
# =============================================================================
# Description:
#   Builds a list of items from a comma-separated text, adds a new item at the
#   end, shows the total number of items and checks if a given item is in the
#   list. Items are stored in lowercase, so the search ignores case.
#   Design decision: empty pieces (like in "apple,,pear") are skipped, and an
#   initial list with no items at all is not accepted (error).
#
# Inputs:
#   - initial_items_text (string; for example "apple,banana,orange")
#   - new_item (string; item to add)
#   - search_item (string; item to search)
#
# Outputs:
#   - "Items list: <items_list>"
#   - "Total items: <len_list>"
#   - "Found item: true|false"
#
# Validations:
#   - initial_items_text is not empty after strip().
#   - The text is split by commas and each piece is cleaned with strip().
#   - new_item and search_item are not empty.
#
# Test cases:
#   1) Normal: "apple, banana ,orange", "grape", "banana"
#      -> ['apple', 'banana', 'orange', 'grape'], total 4, found true
#   2) Border: "apple", "apple", "pear"
#      -> ['apple', 'apple'], total 2, found false
#   3) Error:  "   ", "grape", "apple" -> error (empty initial text)
print("=== Problem 1: Shopping list basics ===")
initial_items_text = input("Enter initial items separated by commas: ").strip()
new_item = input("Enter a new item to add: ").strip().lower()
search_item = input("Enter an item to search: ").strip().lower()

items_list = []
for raw_item in initial_items_text.split(","):
    clean_item = raw_item.strip().lower()
    if clean_item != "":
        items_list.append(clean_item)

if initial_items_text == "":
    print(ERROR_MESSAGE)
elif len(items_list) == 0:
    print(ERROR_MESSAGE)
elif new_item == "" or search_item == "":
    print(ERROR_MESSAGE)
else:
    items_list.append(new_item)
    is_in_list = search_item in items_list

    print(f"Items list: {items_list}")
    print(f"Total items: {len(items_list)}")
    print(f"Found item: {str(is_in_list).lower()}")


# =============================================================================
# Problem 2: Points and distances with tuples
# =============================================================================
# Description:
#   Uses tuples to represent two points in a 2D plane, calculates the
#   Euclidean distance between them and builds a new tuple with the midpoint.
#   Distance and midpoint are rounded to 2 decimals.
#
# Inputs:
#   - x1, y1, x2, y2 (float; coordinates of the points)
#
# Outputs:
#   - "Point A: (x1, y1)"
#   - "Point B: (x2, y2)"
#   - "Distance: <distance>"
#   - "Midpoint: (mx, my)"
#
# Validations:
#   - The 4 inputs can be converted to float (negatives are allowed).
#
# Test cases:
#   1) Normal: 0, 0, 3, 4 -> A (0.0, 0.0), B (3.0, 4.0), distance 5.0,
#      midpoint (1.5, 2.0)
#   2) Border: 2, 2, 2, 2 (same point) -> distance 0.0, midpoint (2.0, 2.0)
#   3) Error:  "a", 0, 3, 4 -> error
print("\n=== Problem 2: Points and distances ===")
x1_text = input("Enter x1: ").strip()
y1_text = input("Enter y1: ").strip()
x2_text = input("Enter x2: ").strip()
y2_text = input("Enter y2: ").strip()

numeric_texts = [x1_text, y1_text, x2_text, y2_text]
all_numbers = True
for text in numeric_texts:
    dot_count = 0
    digit_count = 0
    for index in range(len(text)):
        character = text[index]
        if character in DIGITS:
            digit_count += 1
        elif character == ".":
            dot_count += 1
        elif character != "-" or index != 0:
            all_numbers = False
    if digit_count == 0 or dot_count > 1:
        all_numbers = False

if all_numbers:
    point_a = (float(x1_text), float(y1_text))
    point_b = (float(x2_text), float(y2_text))

    # point[0] is the x coordinate and point[1] is the y coordinate
    distance = ((point_b[0] - point_a[0]) ** 2
                + (point_b[1] - point_a[1]) ** 2) ** 0.5
    midpoint = (
        round((point_a[0] + point_b[0]) / 2, DECIMALS),
        round((point_a[1] + point_b[1]) / 2, DECIMALS),
    )

    print(f"Point A: {point_a}")
    print(f"Point B: {point_b}")
    print(f"Distance: {round(distance, DECIMALS)}")
    print(f"Midpoint: {midpoint}")
else:
    print(ERROR_MESSAGE)


# =============================================================================
# Problem 3: Student grades with lists
# =============================================================================
# Description:
#   Two aligned lists store the data: student_names and student_grades (a list
#   of lists, one list of floats per student; position i of one matches
#   position i of the other). The program reads a student name, finds the
#   position of that student, calculates the average of their grades and
#   tells if the student passed (average >= 70.0).
#   The name is typed in any case and converted with title().
#   The data includes "Diego" with an empty list to show that case.
#
# Inputs:
#   - student_name (string)
#
# Outputs:
#   - If the student exists: "Grades: <grades_list>", "Average: <average>",
#     "Passed: true|false"
#   - If it does not exist: "Error: student not found"
#
# Validations:
#   - student_name is not empty after strip().
#   - student_name is in the student_names list (checked with in).
#   - The grades list is not empty before computing the average.
#
# Test cases:
#   1) Normal: "alice" -> grades [90.0, 85.0, 78.5], average 84.5, passed true
#   2) Border: "Bob" -> grades [60.0, 80.0, 70.0], average 70.0, passed true
#      (exactly on the limit)
#   3) Error:  "Zoe" -> student not found; "" -> invalid input;
#      "Diego" (empty list) -> no grades message
print("\n=== Problem 3: Student grades ===")
student_names = ["Alice", "Bob", "Carla", "Diego"]
student_grades = [
    [90.0, 85.0, 78.5],
    [60.0, 80.0, 70.0],
    [100.0, 95.0, 98.0],
    [],
]

student_name = input("Enter the student name: ").strip().title()

if student_name == "":
    print(ERROR_MESSAGE)
elif student_name not in student_names:
    print("Error: student not found")
else:
    # Find the position of the student in the names list
    student_position = 0
    for position in range(len(student_names)):
        if student_names[position] == student_name:
            student_position = position

    grades_list = student_grades[student_position]
    if len(grades_list) == 0:
        print("Error: no grades for this student")
    else:
        average = sum(grades_list) / len(grades_list)
        is_passed = average >= PASSING_GRADE

        print(f"Grades: {grades_list}")
        print(f"Average: {round(average, DECIMALS)}")
        print(f"Passed: {str(is_passed).lower()}")


# =============================================================================
# Problem 4: Word frequency counter (list of tuples)
# =============================================================================
# Description:
#   Reads a sentence, converts it to lowercase and splits it into a list of
#   words. Then it counts how many times each word appears using two aligned
#   lists (unique_words and word_counts) and builds a list of (word, count)
#   tuples. Finally it finds the most common word (on a tie, the first one
#   found is shown).
#   Design decision: simple punctuation ( . , ; : ! ? ( ) " ) is removed with
#   replace() before splitting.
#
# Inputs:
#   - sentence (string)
#
# Outputs:
#   - "Words list: <words_list>"
#   - "Frequencies: <frequencies_list>"
#   - "Most common word: <word>"
#
# Validations:
#   - sentence is not empty after strip().
#   - The words list is not empty (a sentence with only punctuation fails).
#
# Test cases:
#   1) Normal: "The cat and the dog and the bird"
#      -> frequencies [('the', 3), ('cat', 1), ('and', 2), ('dog', 1),
#      ('bird', 1)], most common word: the
#   2) Border: "Hello!" (one word + punctuation) -> ['hello'], [('hello', 1)]
#   3) Error:  "   " or "..." -> error
print("\n=== Problem 4: Word frequency counter ===")
sentence = input("Enter a sentence: ").strip()

cleaned_sentence = sentence.lower()
for mark in PUNCTUATION:
    cleaned_sentence = cleaned_sentence.replace(mark, "")
words_list = cleaned_sentence.split()

if sentence == "":
    print(ERROR_MESSAGE)
elif len(words_list) == 0:
    print(ERROR_MESSAGE)
else:
    unique_words = []
    word_counts = []
    for word in words_list:
        if word in unique_words:
            for position in range(len(unique_words)):
                if unique_words[position] == word:
                    word_counts[position] += 1
        else:
            unique_words.append(word)
            word_counts.append(1)

    frequencies_list = []
    most_common_word = unique_words[0]
    highest_count = 0
    for position in range(len(unique_words)):
        frequencies_list.append((unique_words[position], word_counts[position]))
        if word_counts[position] > highest_count:
            highest_count = word_counts[position]
            most_common_word = unique_words[position]

    print(f"Words list: {words_list}")
    print(f"Frequencies: {frequencies_list}")
    print(f"Most common word: {most_common_word}")


# =============================================================================
# CONCLUSIONS
# =============================================================================
# Lists are the best choice when items change often, because append() lets the
# collection grow in a flexible way, as in the shopping list of Problem 1.
# Tuples are useful for data that must not change, such as the coordinates of
# a point: reading point[0] and point[1] is safe because nothing can modify
# them by mistake.
# A common pattern I found is the list of lists (one list of grades for each
# student), which keeps each student's data together so it can be averaged.
# Another pattern is keeping two aligned lists (names and grades, words and
# counts) and using the same position to read both.
# A list of tuples, like ('the', 3), is a clean way to show fixed pairs.
# Checking that lists are not empty and that searches find something avoids
# errors and makes the programs safer.

# =============================================================================
# REFERENCES
# =============================================================================
# 1) Python documentation - Sequence Types: list, tuple, range
#    https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
# 2) Python Tutorial - Data Structures (lists, tuples and sequences)
#    https://docs.python.org/3/tutorial/datastructures.html
# 3) Real Python - Lists and Tuples in Python
#    https://realpython.com/python-lists-tuples/
# 4) Real Python - Python's list Data Type: A Deep Dive With Examples
#    https://realpython.com/python-list/
# 5) Downey, A. - Think Python (Lists and Tuples chapters), Green Tea Press
#    https://allendowney.github.io/ThinkPython/
