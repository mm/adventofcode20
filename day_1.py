"""AoC Challenge Day 1
Find the two entries, in a list of integers, that sum to 2020
https://adventofcode.com/2020/day/1
"""

def find_entries_and_multiply(in_list, target):
    """Finds two entries in a list of integers that sum to a
    given target (also an integer), and then multiply those afterwards.
    """

    two_numbers = None

    # We can use the idea of "complements" here. First, we'll start
    # an indices dict, which will have key = the number itself, and the
    # value equal to its index.
    indices = {}

    for i in range(0, len(in_list)):

        # Get the "complement" -- for this current value, what is the
        # extra value I need to add up to my target?
        complement = target - in_list[i]  # e.g if in_list[i] = 1995, target = 2020, => complement = 25

        # Does this value exist in my list? This is where the indices dict
        # comes in handy!
        if complement in indices:
            # Return the two numbers!
            two_numbers = (in_list[i], in_list[indices[complement]])
        else:
            # Otherwise, add it to our indices list. It might match
            # up well with another number!
            indices[in_list[i]] = i

    if two_numbers:
        print(f"Two numbers found which add up to {target}: {two_numbers}")
        return two_numbers[0]*two_numbers[1]
    else:
        return None


def find_three_entries_for_target(in_list, target):
    """Finds three integers which add up to a given target (also an integer),
    and multiply them afterwards.
    """

    three_numbers = None

    # What we can do (sort of brute-force-y) is fix a number as we go through the
    # list, set a new target and then run the *two-integer* version of this problem
    # on the rest of the list.
    for i in range(0, len(in_list)):

        new_target = target - in_list[i]
        # Now, perform the two-integer solution on the *rest* of the list
        # (pretend this number isn't even there)
        two_number_product = find_entries_and_multiply(in_list[i+1:], new_target)
        if two_number_product:
            return in_list[i] * two_number_product


def input_file_to_list(filepath):
    num_list = []
    with open(filepath, 'r') as in_file:
        for line in in_file:
            num_list.append(int(line.strip()))
    return num_list


in_numbers = input_file_to_list('inputs/day_1.txt')

print(find_three_entries_for_target(in_numbers, 2020))
