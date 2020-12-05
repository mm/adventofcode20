"""Day 3: Toboggan Trajectory
"""

def trees_encountered(slope_run, slope_fall, tree_grid):
    """Determines the amount of trees
    a toboggan would encounter moving with a certain
    slope (slope run, slope fall) down a tree grid defined
    like:
    ..##.......
    #...#...#..
    .#....#..#.
    ..#.#...#.#
    .#...##..#.
    ..#.##.....
    .#.#.#....#
    .#........#
    #.##...#...
    #...##....#
    .#..#...#.#
    """
    num_trees = 0
    x = slope_run
    y = slope_fall

    while y < len(tree_grid):  # len(tree_grid) == number of rows
        if x > len(tree_grid[y]) - 1:
            # If we reach the end of a row, reset our
            # horizontal position since the row repeats!
            # (But you want a modulo here -- imagine you need
            # to go 3 spaces but after only going 1 space you hit
            # the end: you want to make those other 2 spaces count too)
            x = x % len(tree_grid[y])
        if tree_grid[y][x] == '#':
            # We've hit a tree! Log it:
            num_trees += 1
        
        x += slope_run
        y += slope_fall
    return num_trees


def solve_part_one(filename):
    with open(filename) as input_trees:
        tree_grid = []
        for line in input_trees:
            tree_grid.append(list(line.strip()))
        print(trees_encountered(3, 1, tree_grid))


def solve_part_two(filename):
    toboggans = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    total_trees = 1
    tree_grid = []
    with open(filename) as input_trees:
        for line in input_trees:
            tree_grid.append(list(line.strip()))
    for toboggan in toboggans:
        num_trees = trees_encountered(toboggan[0], toboggan[1], tree_grid)
        total_trees *= num_trees
        print(f'Toboggan arrangement: {toboggan} --> {num_trees} trees')
    print(f'Product of all trees: {total_trees}')

print("Part 1:")
solve_part_one('inputs/day_3.txt')

print("Part 2:")
solve_part_two('inputs/day_3.txt')