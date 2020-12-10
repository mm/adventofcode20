"""Day 8: Handheld Halting
https://adventofcode.com/2020/day/8
"""

def read_boot_code_input(in_file):
    """Reads in a file containing the boot code instructions.
    This will return a tuple containing:
    - A list of commands (unparsed)
    - A dictionary, with the line numbers from the commands as
      keys and the number of times that line was called as the
      value (0 initially)
    """

    list_of_commands = []
    command_calls = {}
    with open(in_file) as file:
        i = 0
        for line in file:
            list_of_commands.append(line.strip())
            command_calls[i] = 0
            i += 1
    
    return (list_of_commands, command_calls)


def execute_boot_code_one(list_of_commands, command_calls):

    booting = True
    infinite_loop_detected = False
    accumulator = 0
    current_command_number = 0
    
    call_tracker = command_calls

    while booting:
        current_command = list_of_commands[current_command_number]
        command, modifier = current_command.split(' ')

        if current_command_number == len(list_of_commands) - 1:
            if command == 'acc':
                accumulator += int(modifier)
            print(f"End reached: Accumulator {accumulator}")
            break

        # Look up -- has this instruction been called before?
        if call_tracker[current_command_number] >= 1:
            booting = False
            print("Stopped boot")
            print(f'Accumulator value: {accumulator}')
            infinite_loop_detected = True
        else:
            call_tracker[current_command_number] += 1
            if command == 'acc':
                accumulator += int(modifier)
                current_command_number += 1
            elif command == 'nop':
                current_command_number += 1
            elif command == 'jmp':
                current_command_number += int(modifier)

    return (infinite_loop_detected, accumulator)


def execute_boot_code_two(list_of_commands, command_calls):
    """The least efficient solution ever possibly: we're gonna
    just try mutating everything that's not an acc call, test
    it using part (1)'s solution and see what happens.

    Returns the accumulator value when booting is complete, or None
    if no mutation is possible that can fix the boot loop.
    """

    for i, current_command in enumerate(list_of_commands):
        command, modifier = current_command.split(' ')
        new_commands = list.copy(list_of_commands)
        new_command_calls = dict.copy(command_calls)

        if command == 'nop':
            print(f"Attempting to shift nop at line {i} to a jmp...")
            new_commands[i] = ' '.join(['jmp', modifier])
            infinite_loop_found, accumulator = execute_boot_code_one(new_commands, new_command_calls)
            if not infinite_loop_found:
                print("Mutation succeeded")
                return accumulator
        elif command == 'jmp':
            print(f"Attempting to shift jmp at line {i} to a nop...")
            new_commands[i] = ' '.join(['nop', modifier])
            infinite_loop_found, accumulator = execute_boot_code_one(new_commands, new_command_calls)
            if not infinite_loop_found:
                print("Mutation succeeded")
                return accumulator

    return None


commands, call_tracker = read_boot_code_input('inputs/day_8.txt')

final_val = execute_boot_code_two(commands, call_tracker)

print(final_val)