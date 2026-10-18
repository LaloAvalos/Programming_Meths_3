# =============================================================================
# FRONT PAGE / PORTADA
# =============================================================================
# Name:       Avalos López Eduardo
# Student ID: 2630375
# Group:      TSU-75018 (IM-103)
# Assignment: Programming Methodology (Metodologia de la Programación)

# =============================================================================

# =============================================================================
# EXECUTIVE SUMMARY / RESUMEN EJECUTIVO
# =============================================================================
# A string in Python is the str data type: an ordered sequence of characters.
# Strings are immutable, so every operation (upper, replace, slicing, etc.)
# returns a new string and leaves the original untouched.
# Basic operations include concatenation (+), repetition (*), length (len),
# indexing (text[i]), slicing (text[a:b]), searching (in, find, count) and
# replacing text (replace).
# Validating and normalizing input (strip, lower, split) matters because users
# type extra spaces, mixed case and malformed values that would otherwise
# produce wrong comparisons or garbage data.
# This document covers six problems. Each one describes its inputs, outputs,
# validations and three test cases (normal, border, error), followed by the
# code that implements it and a test runner at the end.

# =============================================================================
# PRINCIPLES AND GOOD PRACTICES / PRINCIPIOS Y BUENAS PRACTICAS
# =============================================================================
# - Strings are immutable: any change creates a new string.
# - Normalize input with strip() and lower() before comparing it.
# - Avoid magic numbers in indexes; document what each slice extracts.
# - Use built-in string methods instead of rewriting basic logic.
# - Validate in order: first that the input is not empty, then its format.
# - Write readable code: clear variable names and understandable messages.

# -----------------------------------------------------------------------------
# CONSTANTS (UPPER_SNAKE_CASE)
# -----------------------------------------------------------------------------
ERROR_MESSAGE = "Error: invalid input"
MIN_NAME_WORDS = 2
MIN_PALINDROME_LENGTH = 3
MIN_PASSWORD_LENGTH = 8
LABEL_LENGTH = 30


# =============================================================================
# Problem 1: Full name formatter (name + initials)
# =============================================================================
# Description:
#   Takes a full name in a single string, normalizes it (strip, extra spaces,
#   case) and shows it in Title Case together with the initials (J.C.T.).
#
# Inputs:
#   - full_name (string)
#
# Outputs:
#   - "Formatted name: <Name In Title Case>"
#   - "Initials: <X.X.X.>"
#
# Validations:
#   - full_name is not empty after strip().
#   - It has at least two words.
#
# Test cases:
#   1) Normal: "juan carlos tovar" -> Juan Carlos Tovar / J.C.T.
#   2) Border: "  ANA    lopez  " (extra spaces, uppercase) -> Ana Lopez / A.L.
#   3) Error:  "   " (only spaces) or "maria" (one word) -> error
def format_full_name(full_name):
    cleaned_name = full_name.strip()
    if cleaned_name == "":
        return [ERROR_MESSAGE]

    # split() without arguments also removes the extra spaces between words
    words = cleaned_name.split()
    if len(words) < MIN_NAME_WORDS:
        return [ERROR_MESSAGE]

    formatted_name = " ".join(words).title()
    initials = ""
    for word in words:
        initials += word[0].upper() + "."  # word[0] = first letter of the word

    return [f"Formatted name: {formatted_name}", f"Initials: {initials}"]


# =============================================================================
# Problem 2: Simple email validator (structure + domain)
# =============================================================================
# Description:
#   Checks the basic structure of an email: exactly one '@', at least one '.'
#   after the '@', and no spaces. If valid, it also shows the domain.
#
# Inputs:
#   - email_text (string)
#
# Outputs:
#   - "Valid email: true" or "Valid email: false"
#   - If valid: "Domain: <domain_part>"
#
# Validations:
#   - email_text is not empty after strip().
#   - Count of '@' is exactly 1.
#   - No spaces inside email_text.
#   - Extra rule (documented): text before '@' is not empty, and the domain
#     does not start or end with '.'.
#
# Test cases:
#   1) Normal: "lalo@gmail.com" -> true, Domain: gmail.com
#   2) Border: "a@b.c" (shortest valid shape) -> true, Domain: b.c
#   3) Error:  "lalo@@gmail.com" or "lalo gmail.com" -> false; "" -> error
def validate_email(email_text):
    cleaned_email = email_text.strip()
    if cleaned_email == "":
        return [ERROR_MESSAGE]

    at_count = cleaned_email.count("@")
    has_spaces = " " in cleaned_email
    if at_count != 1 or has_spaces:
        return ["Valid email: false"]

    at_position = cleaned_email.find("@")
    local_part = cleaned_email[:at_position]       # text before '@'
    domain_part = cleaned_email[at_position + 1:]  # text after '@'

    domain_has_dot = "." in domain_part
    bad_dot_position = domain_part.startswith(".") or domain_part.endswith(".")
    if local_part == "" or not domain_has_dot or bad_dot_position:
        return ["Valid email: false"]

    return ["Valid email: true", f"Domain: {domain_part}"]


# =============================================================================
# Problem 3: Palindrome checker (ignoring spaces and case)
# =============================================================================
# Description:
#   Determines whether a phrase reads the same forwards and backwards,
#   ignoring spaces and uppercase/lowercase. Also shows the normalized text.
#
# Inputs:
#   - phrase (string)
#
# Outputs:
#   - "Is palindrome: true" or "Is palindrome: false"
#   - "Normalized: <text>"
#
# Validations:
#   - phrase is not empty after strip().
#   - Normalized text has at least 3 characters.
#
# Test cases:
#   1) Normal: "Anita lava la tina" -> true
#   2) Border: "AbA" (minimum length, mixed case) -> true
#   3) Error:  "  " -> error; "a b" (normalized length 2) -> error
def check_palindrome(phrase):
    cleaned_phrase = phrase.strip()
    if cleaned_phrase == "":
        return [ERROR_MESSAGE]

    normalized_text = cleaned_phrase.lower().replace(" ", "")
    if len(normalized_text) < MIN_PALINDROME_LENGTH:
        return [ERROR_MESSAGE]

    reversed_text = normalized_text[::-1]  # slice with step -1 reverses it
    result = "true" if normalized_text == reversed_text else "false"
    return [f"Is palindrome: {result}", f"Normalized: {normalized_text}"]


# =============================================================================
# Problem 4: Sentence word stats (lengths and first/last word)
# =============================================================================
# Description:
#   Splits a sentence into words and shows the word count, first word, last
#   word, shortest word and longest word. On ties, the first one found wins.
#   Punctuation is kept as part of the word (simple split by spaces).
#
# Inputs:
#   - sentence (string)
#
# Outputs:
#   - "Word count: <n>", "First word: <...>", "Last word: <...>",
#     "Shortest word: <...>", "Longest word: <...>"
#
# Validations:
#   - sentence is not empty after strip().
#   - At least one word after split().
#
# Test cases:
#   1) Normal: "Python makes strings easy" -> 4 words, first Python,
#      last easy, shortest easy, longest strings
#   2) Border: "  Hello  " (a single word with spaces) -> 1 word, all equal
#   3) Error:  "     " -> error
def sentence_word_stats(sentence):
    cleaned_sentence = sentence.strip()
    if cleaned_sentence == "":
        return [ERROR_MESSAGE]

    words = cleaned_sentence.split()
    if len(words) == 0:
        return [ERROR_MESSAGE]

    shortest_word = words[0]
    longest_word = words[0]
    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word
        if len(word) > len(longest_word):
            longest_word = word

    return [
        f"Word count: {len(words)}",
        f"First word: {words[0]}",
        f"Last word: {words[-1]}",
        f"Shortest word: {shortest_word}",
        f"Longest word: {longest_word}",
    ]


# =============================================================================
# Problem 5: Password strength classifier
# =============================================================================
# Description:
#   Classifies a password as weak, medium or strong. Rules used (documented):
#     - Count how many of these 4 categories appear: uppercase letter,
#       lowercase letter, digit, symbol (non-alphanumeric).
#     - Strong: length >= 8 and all 4 categories.
#     - Medium: length >= 8 and at least 2 categories.
#     - Weak: everything else (too short or too simple).
#
# Inputs:
#   - password_input (string)
#
# Outputs:
#   - "Password strength: weak" / "medium" / "strong"
#
# Validations:
#   - Password is not empty.
#   - Length is checked with len().
#
# Test cases:
#   1) Normal: "Abcdef1!" -> strong
#   2) Border: "abcdefg1" (exactly 8 chars, 2 categories) -> medium
#   3) Error:  "" -> error; "abc" -> weak
def classify_password(password_input):
    if password_input == "":
        return [ERROR_MESSAGE]

    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False
    for character in password_input:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True
        elif not character.isalnum():
            has_symbol = True

    categories_count = sum([has_upper, has_lower, has_digit, has_symbol])

    if len(password_input) < MIN_PASSWORD_LENGTH:
        strength = "weak"
    elif categories_count == 4:
        strength = "strong"
    elif categories_count >= 2:
        strength = "medium"
    else:
        strength = "weak"

    return [f"Password strength: {strength}"]


# =============================================================================
# Problem 6: Product label formatter (fixed-width text)
# =============================================================================
# Description:
#   Builds the label "Product: <NAME> | Price: $<PRICE>" and forces it to be
#   exactly 30 characters: shorter labels are padded with spaces at the end,
#   longer ones are cut with slicing.
#
# Inputs:
#   - product_name (string)
#   - price_value (string or number, must be a positive number)
#
# Outputs:
#   - "Label: "<exactly 30 characters>"" (quotes show the trailing spaces)
#
# Validations:
#   - product_name is not empty after strip().
#   - price_value converts to a number greater than 0.
#
# Test cases:
#   1) Normal: "Mouse", 150 -> padded with spaces to 30 characters
#   2) Border: "Mechanical Keyboard RGB", "1299.90" -> longer, gets cut at 30
#   3) Error:  "Cable", -5 -> error; "  ", 10 -> error; "Pen", "abc" -> error
def format_product_label(product_name, price_value):
    cleaned_name = product_name.strip()
    if cleaned_name == "":
        return [ERROR_MESSAGE]

    price_text = str(price_value).strip()
    try:
        price_number = float(price_text)
    except ValueError:
        return [ERROR_MESSAGE]
    if price_number <= 0:
        return [ERROR_MESSAGE]

    base_label = f"Product: {cleaned_name} | Price: ${price_text}"
    fixed_label = base_label[:LABEL_LENGTH]  # cut if longer than 30
    while len(fixed_label) < LABEL_LENGTH:   # pad with spaces if shorter
        fixed_label += " "

    return [f'Label: "{fixed_label}"', f"Length: {len(fixed_label)}"]


# =============================================================================
# TEST RUNNER / EJECUTOR DE PRUEBAS
# =============================================================================
def run_case(case_type, function, *arguments):
    print(f"  [{case_type}] input: {arguments!r}")
    for line in function(*arguments):
        print(f"      {line}")


def main():
    print("=== Problem 1: Full name formatter ===")
    run_case("Normal", format_full_name, "juan carlos tovar")
    run_case("Border", format_full_name, "  ANA    lopez  ")
    run_case("Error", format_full_name, "   ")
    run_case("Error", format_full_name, "maria")

    print("\n=== Problem 2: Email validator ===")
    run_case("Normal", validate_email, "lalo@gmail.com")
    run_case("Border", validate_email, "a@b.c")
    run_case("Error", validate_email, "lalo@@gmail.com")
    run_case("Error", validate_email, "lalo gmail.com")
    run_case("Error", validate_email, "")

    print("\n=== Problem 3: Palindrome checker ===")
    run_case("Normal", check_palindrome, "Anita lava la tina")
    run_case("Border", check_palindrome, "AbA")
    run_case("Error", check_palindrome, "  ")
    run_case("Error", check_palindrome, "a b")

    print("\n=== Problem 4: Sentence word stats ===")
    run_case("Normal", sentence_word_stats, "Python makes strings easy")
    run_case("Border", sentence_word_stats, "  Hello  ")
    run_case("Error", sentence_word_stats, "     ")

    print("\n=== Problem 5: Password strength classifier ===")
    run_case("Normal", classify_password, "Abcdef1!")
    run_case("Border", classify_password, "abcdefg1")
    run_case("Error", classify_password, "")
    run_case("Error", classify_password, "abc")

    print("\n=== Problem 6: Product label formatter ===")
    run_case("Normal", format_product_label, "Mouse", 150)
    run_case("Border", format_product_label, "Mechanical Keyboard RGB", "1299.90")
    run_case("Error", format_product_label, "Cable", -5)
    run_case("Error", format_product_label, "  ", 10)
    run_case("Error", format_product_label, "Pen", "abc")


if __name__ == "__main__":
    main()

# =============================================================================
# CONCLUSIONS / CONCLUSIONES
# =============================================================================
# Handling strings is essential for reading and writing data, because almost
# every input from a user arrives as text and must be cleaned before use.
# strip() and lower() are useful before comparing, split() and join() when
# working word by word, and replace() when removing or changing characters.
# Normalizing text before comparing it avoids false negatives such as
# "Hello" != "hello" or an extra trailing space breaking a match.
# Designing validations first (empty, format, range) prevents errors and
# garbage data from reaching the main logic of the program.
# I learned that strings are immutable, so each method returns a new string,
# and that slices like text[::-1] or label[:30] make it easy to reverse or
# cut text without loops.

# =============================================================================
# REFERENCES / REFERENCIAS
# =============================================================================
# 1) Python documentation - Built-in Types: Text Sequence Type - str
#    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# 2) Python documentation - String Methods
#    https://docs.python.org/3/library/stdtypes.html#string-methods
# 3) Python Tutorial - An Informal Introduction to Python (Text)
#    https://docs.python.org/3/tutorial/introduction.html
# 4) Real Python - Strings and Character Data in Python
#    https://realpython.com/python-strings/
# 5) Downey, A. - Think Python (Strings chapter), Green Tea Press
#    https://allendowney.github.io/ThinkPython/
