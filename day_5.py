"""
Day 5: Binary Boarding
https://adventofcode.com/2020/day/5
"""

from typing import Tuple

def binary_split_characters(characters, lower_bound, upper_bound, lower_char, upper_char):
    lower_wall = lower_bound
    upper_wall = upper_bound

    i = 0
    while i < len(characters):
        midpoint = (upper_wall + lower_wall) // 2

        if characters[i] == lower_char:
            # Keep the lower half:
            upper_wall = midpoint
        elif characters[i] == upper_char:
            # Keep the upper half:
            lower_wall = midpoint + 1
        i += 1
    
    return lower_wall


def boarding_pass_to_id(boarding_pass: str) -> int:
    """Given a boarding pass string, get the boarding
    pass ID.
    """
    
    row = binary_split_characters(boarding_pass[:7], 0, 127, 'F', 'B')
    col = binary_split_characters(boarding_pass[7:], 0, 7, 'L', 'R')

    return row*8 + col


def part_one_solution(filename):
    max_id = -1
    with open(filename) as in_file:
        for boarding_pass in in_file:
            boarding_pass = boarding_pass.strip()
            boarding_id = boarding_pass_to_id(boarding_pass)
            max_id = max(max_id, boarding_id)
    return max_id


def part_two_solution(filename):
    # We'll be checking in this set to find the missing pass:
    boarding_passes = set()

    with open(filename) as in_file:
        for boarding_pass in in_file:
            boarding_passes.add(boarding_pass_to_id(boarding_pass.strip()))

    # Go through the boarding passes, starting at the first boarding pass you see.
    starting_seat = min(boarding_passes)
    for seat in boarding_passes:
        # Our missing seat *has* seats on either side filled, so check for a
        # seat that's supposed to be there and isn't, but has filled seats
        # on either side.
        if starting_seat not in boarding_passes:
            # So this seat isn't filled. What about the seats surrounding it?
            if (starting_seat + 1 in boarding_passes) and (starting_seat - 1 in boarding_passes):
                return starting_seat
        # Try the next possible seat
        starting_seat += 1

print(part_one_solution('inputs/day_5.txt'))

print(part_two_solution('inputs/day_5.txt'))