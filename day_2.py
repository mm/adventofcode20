"""Day 2: Password Philosophy
https://adventofcode.com/2020/day/2
"""

def parse_password_policy(policy: str):
    """Parses a password policy, and returns a tuple with 3 elements
    Example: '1-3 a' --> (1, 3, 'a')
    """
    bounds, policy_letter = policy.split(' ')  # '1-3 a' --> ['1-3', 'a']
    lower_bound, upper_bound = [int(x) for x in bounds.split('-')]
    return (lower_bound, upper_bound, policy_letter)


def is_password_valid(policy: str, password: str) -> bool:
    """Evaluates if a password is valid based on a policy provided.
    Policies take the form of `1-3 a`: which means the letter
    "a" must show up between 1-3 times (inclusive).
    """
    lower_bound, upper_bound, policy_letter = parse_password_policy(policy)

    policy_letter_counter = 0
    # Evaluate the password against the policy
    for char in password:
        if char == policy_letter:
            policy_letter_counter += 1

    return (policy_letter_counter != 0) and (policy_letter_counter >= lower_bound) and (policy_letter_counter <= upper_bound)


def is_password_valid_modified(policy: str, password: str) -> bool:
    """Almost the same rules as `is_password_valid`, except the range given in the policy
    represent positions -- e.g 1-3 a means *exactly one* of the positions *must*
    contain the given letter.
    """
    pos1, pos2, letter = parse_password_policy(policy)

    # This is an exclusive OR (XOR), which we can do with the ^ operator in Python
    return (password[pos1-1] == letter) ^ (password[pos2-1] == letter)
    

def day_two_solution(filepath, password_handler):
    valid_passwords = 0

    with open(filepath, 'r') as in_file:
        for line in in_file:
            policy, password = line.split(':')
            if password_handler(policy, password.strip()):
                valid_passwords += 1
    
    return valid_passwords


print(day_two_solution('inputs/day_2.txt', is_password_valid))
print(day_two_solution('inputs/day_2.txt', is_password_valid_modified))