"""Week 1 Homework: Evidence Desk Patterns.

Complete each function using the data structure pattern named in the docstring.

Rules:
- Python 3.11+
- Standard library only
- Do not change function names or parameters
- Run tests with: pytest -q
"""

from collections import deque
from typing import Dict, List, Optional


# -----------------------------------------------------------------------------
# Required Problem 1
# -----------------------------------------------------------------------------

def count_evidence(evidence: List[str]) -> Dict[str, int]:
    """Return a dictionary counting how many times each evidence label appears.

    Pattern: frequency counting
    Data structure: dictionary
    """
    counts = {}

    for item in evidence:
        counts[item] = counts.get(item, 0) + 1

    return counts


# -----------------------------------------------------------------------------
# Required Problem 2
# -----------------------------------------------------------------------------

def first_repeated_id(ids: List[str]) -> Optional[str]:
    """Return the first suspect ID that appears a second time.

    Pattern: seen before
    Data structure: set
    """
    seen = set()

    for suspect_id in ids:
        if suspect_id in seen:
            return suspect_id

        seen.add(suspect_id)

    return None


# -----------------------------------------------------------------------------
# Required Problem 3
# -----------------------------------------------------------------------------

def valid_tags(tags: str) -> bool:
    """Return True if all bracket-style evidence tags are balanced.

    Pattern: stack matching
    Data structure: list used as a stack
    """
    stack = []

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    openings = set(pairs.values())

    for char in tags:
        if char in openings:
            stack.append(char)

        elif char in pairs:
            if not stack:
                return False

            if stack.pop() != pairs[char]:
                return False

    return len(stack) == 0


# -----------------------------------------------------------------------------
# Required Problem 4
# -----------------------------------------------------------------------------

def lookup_alias(aliases: Dict[str, str], alias: str) -> Optional[str]:
    """Return the real name connected to an alias.

    Pattern: lookup table
    Data structure: dictionary
    """
    return aliases.get(alias)


# -----------------------------------------------------------------------------
# Optional Challenge 1
# -----------------------------------------------------------------------------

def process_reports(reports: List[str]) -> List[str]:
    """Return case reports in first-in, first-out processing order.

    Pattern: queue processing
    Data structure: collections.deque
    """
    queue = deque(reports)
    processed = []

    while queue:
        processed.append(queue.popleft())

    return processed


# -----------------------------------------------------------------------------
# Optional Challenge 2
# -----------------------------------------------------------------------------

def largest_time_gap(times: List[int]) -> int:
    """Return the largest gap between neighboring event times after sorting.

    Pattern: sorting + scan
    Data structure: list
    """
    if len(times) < 2:
        return 0

    sorted_times = sorted(times)
    largest_gap = 0

    for i in range(1, len(sorted_times)):
        gap = sorted_times[i] - sorted_times[i - 1]

        if gap > largest_gap:
            largest_gap = gap

    return largest_gap