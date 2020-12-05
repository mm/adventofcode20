"""Day 4: Passport Processing
"""

import re

DEBUG = False

class PassportValidator(object):
    """Responsible for consuming a passport dict and validating it
    according to rules in the challenge.
    """

    def __init__(self, passport:dict):
        self.passport = passport

    def _validate_required_fields(self) -> bool:
        """Validates that the passport contains
        the correct amount of keys ('cid' is optional)
        """
        is_valid = (len(self.passport) == 8) or (len(self.passport) == 7 and 'cid' not in self.passport)
        if not is_valid and DEBUG:
            print("Failed required fields check")
        return is_valid

    def _validate_birth_year(self) -> bool:
        """Is the birth year between 1920 and 2002?"""
        is_valid = (self.passport.get('byr')) and (int(self.passport['byr']) >= 1920) and (int(self.passport['byr']) <= 2002)
        if not is_valid and DEBUG:
            print("Failed birth year check")
        return is_valid
    
    def _validate_issue_year(self) -> bool:
        """Is the issue year between 2010 and 2020?"""
        is_valid = (self.passport.get('iyr')) and (int(self.passport['iyr']) >= 2010) and (int(self.passport['iyr']) <= 2020)
        if not is_valid and DEBUG:
            print("Failed issue year check")
        return is_valid

    def _validate_expiration_year(self) -> bool:
        """Is the expiration year between 2020 and 2030?"""
        is_valid = (self.passport.get('eyr')) and (int(self.passport['eyr']) >= 2020) and (int(self.passport['eyr']) <= 2030)
        if not is_valid and DEBUG:
            print("Failed exp year check")
        return is_valid
    
    def _validate_height(self) -> bool:
        """hgt (Height) - a number followed by either cm or in:
            If cm, the number must be at least 150 and at most 193.
            If in, the number must be at least 59 and at most 76
        """
        is_valid = False
        # Breaks up 160cm --> ['', '160', 'cm']
        parsed = re.split('(\d+)', self.passport['hgt'])
        if len(parsed) == 3:
            if parsed[2] == 'cm':
                is_valid = (int(parsed[1]) >= 150) and (int(parsed[1]) <= 193)
            elif parsed[2] == 'in':
                is_valid = (int(parsed[1]) >= 59) and (int(parsed[1]) <= 76)
        
        if not is_valid and DEBUG:
            print("Failed height check")
        
        return is_valid

    def _validate_hair_colour(self) -> bool:
        """a # followed by exactly six characters 0-9 or a-f"""
        hex_pattern = re.compile("^#(?:[0-9a-fA-F]{6})$")
        is_valid = hex_pattern.match(self.passport.get('hcl'))
        if not is_valid and DEBUG:
            print("Failed hcl check")
        return is_valid

    def _validate_eye_colour(self) -> bool:
        """exactly one of: amb blu brn gry grn hzl oth"""
        is_valid = (self.passport.get('ecl')) and (self.passport['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'))
        if not is_valid and DEBUG:
            print("Failed ecl check")
        return is_valid

    def _valid_passport_id(self) -> bool:
        """a nine-digit number, including leading zeroes"""
        passport_pattern = re.compile("([0-9]{9})$")
        is_valid = passport_pattern.match(self.passport.get('pid'))
        if not is_valid and DEBUG:
            print("Failed PID check")
        return is_valid


    def valid_part_one(self) -> bool:
        """Returns True if the passport satisfies part #1 criteria.
        """
        return self._validate_required_fields()

    
    def valid(self) -> bool:
        """Returns True if the passport satisfies all criteria.
        """
        return (
            (self.valid_part_one()) and
            (self._validate_birth_year()) and 
            (self._validate_issue_year()) and 
            (self._validate_expiration_year()) and 
            (self._validate_height()) and
            (self._validate_hair_colour()) and
            (self._validate_eye_colour()) and
            (self._valid_passport_id())
        )


def passports_in_file(filepath):
    with open(filepath, 'r') as in_file:
        current_passport = {}

        # Walk through the input file. Build up a dict
        # representing a passport until we hit a newline (which
        # separates passports in the batch file)
        for line in in_file:
            if line != '\n':
                # eyr:2021 hgt:168cm --> [['eyr', '2021'], ['hgt', '168cm']]
                list_of_fields = [x.split(":") for x in line.rstrip().split(" ")]
                for field in list_of_fields:
                    # Add these to our dictionary
                    current_passport[field[0]] = field[1]
            else:
                yield current_passport
                current_passport = {}
        # At the end of this file, we still have one more passport to process!
        # (Because we haven't hit a newline character yet)
        yield current_passport


def part_one_solution(input_file):
    valid_passports = 0
    for passport in passports_in_file(input_file):
        if PassportValidator(passport).valid_part_one():
            valid_passports += 1
    return valid_passports


def part_two_solution(input_file):
    valid_passports = 0
    for passport in passports_in_file(input_file):
        if PassportValidator(passport).valid():
            valid_passports += 1
    return valid_passports

print(f'Valid passports in Part 1: {part_one_solution("inputs/day_4.txt")}')
print(f'Valid passports in Part 2: {part_two_solution("inputs/day_4.txt")}')