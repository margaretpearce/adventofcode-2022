from typing import Dict, Tuple

PLAY_TO_SC0RE: Dict[str, int] = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}


def read_play(play: str) -> str:
    if play == "A":
        return "Rock"
    if play == "B":
        return "Paper"
    if play == "C":
        return "Scissors"
    raise ValueError(f"Unknown play {play}")


def read_response(play: str) -> str:
    if play == "X":
        return "Rock"
    if play == "Y":
        return "Paper"
    if play == "Z":
        return "Scissors"
    raise ValueError(f"Unknown play {play}")


def get_winning_move(play: str):
    if play == "Rock":
        return "Paper"
    elif play == "Paper":
        return "Scissors"
    elif play == "Scissors":
        return "Rock"


def determine_play_based_on_outcome(opponent_play: str, outcome: str) -> str:
    if outcome == "X":
        # You need to lose
        if opponent_play == "Rock":
            return "Scissors"
        elif opponent_play == "Paper":
            return "Rock"
        elif opponent_play == "Scissors":
            return "Paper"
    elif outcome == "Y":
        # Tie
        return opponent_play
    elif outcome == "Z":
        # You need to win
        return get_winning_move(opponent_play)


def determine_winner(opponent_play, your_play) -> bool:
    return your_play == get_winning_move(opponent_play)


def score_round(opponent_play, your_play) -> Tuple[int, int]:
    """
    Your total score is the sum of your scores for each round. The score for a single round is the score for the shape
    you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you
    lost, 3 if the round was a draw, and 6 if you won).
    """
    opponent_score = PLAY_TO_SC0RE[opponent_play]
    your_score = PLAY_TO_SC0RE[your_play]

    if opponent_score == your_score:
        # Tie
        opponent_score += 3
        your_score += 3
    else:
        you_won = determine_winner(opponent_play, your_play)
        if you_won:
            your_score += 6
        else:
            opponent_score += 6

    return opponent_score, your_score


def puzzle(input_filename: str, is_part_two: bool = False):
    opponent_total: int = 0
    your_total: int = 0

    with open(f"input/day2/{input_filename}", "r") as input_data:
        for play_round in input_data:
            opponent_play = read_play(play_round[0])
            if is_part_two:
                your_play = determine_play_based_on_outcome(opponent_play, play_round[2])
            else:
                your_play = read_response(play_round[2])

            opponent_score, your_score = score_round(opponent_play, your_play)
            opponent_total += opponent_score
            your_total += your_score

    return your_total


def main():
    example_part_1 = puzzle("example.txt")
    print(f"Part 1 (example): {example_part_1}")

    part_1 = puzzle("input.txt")
    print(f"Part 1: {part_1}")

    example_part_2 = puzzle("example.txt", is_part_two=True)
    print(f"Part 2 (example): {example_part_2}")

    part_2 = puzzle("input.txt", is_part_two=True)
    print(f"Part 2: {part_2}")


if __name__ == '__main__':
    main()
