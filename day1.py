from typing import List

def puzzle_1(input_filename: str):
    elf_to_calories = []
    elf_number = 0

    with open(f"input/day1/{input_filename}", "r") as input_data:
        for line in input_data:
            if line == "" or line == "\n":
                elf_number += 1
            else:
                calories = int(line)
                if len(elf_to_calories) == elf_number:
                    elf_to_calories.append(calories)
                else:
                    elf_to_calories[elf_number] += calories

        return max(elf_to_calories), elf_to_calories


def puzzle_2(part_1_list: List[int]):
    sorted_by_calories = sorted(part_1_list)
    return sorted_by_calories[-1] + sorted_by_calories[-2] + sorted_by_calories[-3]


def main():
    example_part_1, example_part_2_input = puzzle_1("example.txt")
    print(f"Part 1 (example): {example_part_1}")

    part_1, part_2_input = puzzle_1("input.txt")
    print(f"Part 1: {part_1}")

    example_part_2 = puzzle_2(example_part_2_input)
    print(f"Part 2 (example): {example_part_2}")

    part_2 = puzzle_2(part_2_input)
    print(f"Part 2: {part_2}")


if __name__ == '__main__':
    main()
