"""Day 6: Custom Customs
https://adventofcode.com/2020/day/6
"""

from typing import List
from collections import Counter

def groups_in_file(input_file):
    """Reads in the input file, and yields a "group"
    (a list of strings) of responses. Groups in the input
    file are separated by newlines.
    """

    with open(input_file) as file:
        current_group = []
        for line in file:
            if line != '\n':
                current_group.append(line.strip())
            else:
                yield current_group
                current_group = []
        # At the end of the file, we'll still have one
        # group left (because there's no new \n at the end)
        yield current_group


def total_yes_responses(group: List[str]) -> int:
    """Computes the total number of yes responses
    for a given group (for Part 1)
    """
    response_set = set()
    for response in group:
        # First we convert our response to a list
        # (For example, 'abc' --> ['a', 'b', 'c'])
        # Then, we convert that to a set, and take
        # the union of our response_set and this set,
        # which takes care of duplicate removal for us
        response_set |= set(list(response))
    return len(response_set)


def total_agreeances(group: List[str]) -> int:
    """Computes the total number of yes's in a group
    where *everyone* said yes to the same question
    (for Part 2)
    """
    # We need to know 1) the amount of people who were
    # in the group:
    total_people = len(group) # since one person per element

    # 2) the number of people who agreed per response.
    answer_counts = Counter()  # a dict subclass built for this purpose
    # The counter will have questions as keys and # of yes responses as
    # values.

    for response in group:
        # First we convert our response to a list
        # (For example, 'abc' --> ['a', 'b', 'c'])
        # Then, we update our counter dict with this list:
        answer_counts.update(list(response))

    # Calling answer_counts.values() will give us all the yes counts in our response.
    # What we'll do is filter this iterable to give us only counts equal to the total
    # number of people in our group:
    full_agreeance = list(filter(lambda count: count == total_people, answer_counts.values()))

    # How many questions did everyone say yes to?
    return len(full_agreeance)


combined_yes_responses = 0
questions_everyone_said_yes_to = 0

for group in groups_in_file('inputs/day_6.txt'):
    combined_yes_responses += total_yes_responses(group)
    questions_everyone_said_yes_to += total_agreeances(group)

print(f'Part 1: {combined_yes_responses} yes responses')
print(f'Part 2: {questions_everyone_said_yes_to} questions were answered yes by everyone')