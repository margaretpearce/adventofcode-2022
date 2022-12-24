
PRIORITY = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_common_item_priority(input_rucksack: str) -> int:
    midpoint = round(len(input_rucksack) / 2)
    rucksack_1 = set(input_rucksack[0:midpoint])
    rucksack_2 = set(input_rucksack[midpoint:])
    common_item = rucksack_1.intersection(rucksack_2).pop()
    common_item_priority = PRIORITY.index(common_item) + 1
    return common_item_priority


def get_grouped_common_item_priority(input_rucksacks: list[str]) -> int:
    input_rucksack_sets = [set(s) for s in input_rucksacks]
    common_item = input_rucksack_sets[0].intersection(input_rucksacks[1]).intersection(input_rucksacks[2]).pop()
    common_item_priority = PRIORITY.index(common_item) + 1
    return common_item_priority


def puzzle_1(input_filename: str) -> int:
    priority_sum = 0
    with open(f"input/day3/{input_filename}", "r") as input_data:
        for line in input_data:
            common_item_priority = get_common_item_priority(line.strip('\n'))
            priority_sum += common_item_priority
    return priority_sum


def puzzle_2(input_filename: str):
    lines = []
    line_count = 0
    priority_sum = 0

    with open(f"input/day3/{input_filename}", "r") as input_data:
        for line in input_data:
            line_count += 1
            lines.append(line.strip('\n'))

            if line_count == 3:
                common_item_priority = get_grouped_common_item_priority(lines)
                priority_sum += common_item_priority
                lines = []
                line_count = 0
    return priority_sum


def main():
    example_part_1 = puzzle_1("example.txt")
    print(f"Part 1 (example): {example_part_1}")

    part_1 = puzzle_1("input.txt")
    print(f"Part 1: {part_1}")

    example_part_2 = puzzle_2("example.txt")
    print(f"Part 2 (example): {example_part_2}")

    part_2 = puzzle_2("input.txt")
    print(f"Part 2: {part_2}")


if __name__ == '__main__':
    main()
