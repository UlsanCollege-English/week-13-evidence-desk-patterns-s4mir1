# Week 1 Homework: Evidence Desk Patterns

## Student Name

Samir Bhandari

## Summary

This homework focuses on practicing common data structure patterns in Python. The tasks include counting occurrences using dictionaries, detecting duplicates using sets, validating balanced brackets using a stack, and performing lookups with dictionaries. It also provides optional challenges involving queue processing with deque and sorting with scanning techniques. These exercises help strengthen problem-solving skills and understanding of fundamental data structures.

## How to Run Tests

From the repository root, run:

```bash
pytest -q
```

To run one test file:

```bash
pytest -q tests/test_challenges.py
```

## Required Problems

Complete these functions in `src/challenges.py`:

1. `count_evidence`
2. `first_repeated_id`
3. `valid_tags`
4. `lookup_alias`

## Optional Challenges

These are extra practice unless your instructor tells you otherwise:

1. `process_reports`
2. `largest_time_gap`

Optional tests are skipped by default. To run them, remove the `@pytest.mark.skip(...)` line above the optional test you want to check.

---

# Problem Notes

## 1. Evidence Counter

### Pattern

Frequency Counting

### Data Structure

Dictionary

### Approach

* Step 1: Create an empty dictionary to store counts.
* Step 2: Loop through each evidence label.
* Step 3: Update the count for each label and return the dictionary.

### Complexity

* Time: `O(n)`
* Space: `O(n)`

Explain briefly:

The function visits each item once and stores counts in a dictionary. The number of dictionary entries depends on the number of unique labels.

### Edge Cases Checked

* [x] Empty list
* [x] One item
* [x] Repeated items
* [x] Different labels

---

## 2. Repeat Suspect ID

### Pattern

Seen Before

### Data Structure

Set

### Approach

* Step 1: Create an empty set called `seen`.
* Step 2: Loop through each ID and check whether it already exists in the set.
* Step 3: Return the first repeated ID or `None` if no repetition is found.

### Complexity

* Time: `O(n)`
* Space: `O(n)`

Explain briefly:

Each lookup and insertion into a set is approximately constant time, making the overall solution efficient.

### Edge Cases Checked

* [x] Empty list
* [x] No repeated IDs
* [x] First two IDs match
* [x] Multiple repeated IDs

---

## 3. Evidence Tag Validator

### Pattern

Stack Matching

### Data Structure

List Used as a Stack

### Approach

* Step 1: Create an empty stack and define matching bracket pairs.
* Step 2: Push opening brackets onto the stack.
* Step 3: When a closing bracket appears, verify that it matches the most recent opening bracket.

### Complexity

* Time: `O(n)`
* Space: `O(n)`

Explain briefly:

The string is scanned once. The stack stores unmatched opening brackets and ensures proper nesting.

### Edge Cases Checked

* [x] Empty string
* [x] Correctly nested tags
* [x] Mismatched tags
* [x] Closing tag before opening tag
* [x] Unclosed opening tag
* [x] Non-bracket characters

---

## 4. Alias Directory

### Pattern

Lookup Table

### Data Structure

Dictionary

### Approach

* Step 1: Check whether the alias exists in the dictionary.
* Step 2: Return the associated real name or `None`.

### Complexity

* Time: `O(1)`
* Space: `O(1)`

Explain briefly:

Dictionary lookups are performed in constant time on average.

### Edge Cases Checked

* [x] Known alias
* [x] Unknown alias
* [x] Empty dictionary

---

# Assistance & Sources

## AI Used?

* [x] Yes
* [ ] No

## If yes, what did AI help with?

* Reviewed solution logic and complexity analysis.
* Helped explain data structure patterns used in each problem.
* Assisted with formatting and completing the README documentation.

## Other Sources

None
