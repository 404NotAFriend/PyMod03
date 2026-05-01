#!/usr/bin/env python3
import sys


def ft_score_analytics() -> None:

    print("=== Player Score Analytics ===")
    if len(sys.argv) < 2:
        print("No scores provided. "
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    arguments = sys.argv[1:]

    valid_scores = []
    for arg in arguments:
        try:
            score = int(arg)
            valid_scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
            continue

    if len(valid_scores) == 0:
        print("No scores provided. "
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    total_players = len(valid_scores)
    total_score = sum(valid_scores)
    average_score = sum(valid_scores) / total_players
    highest_score = max(valid_scores)
    lowest_score = min(valid_scores)
    score_range = max(valid_scores) - min(valid_scores)

    print(f"Scores processed: {valid_scores}")
    print(f"Total Players: {total_players}")
    print(f"Total Score: {total_score}")
    print(f"Average Score: {average_score}")
    print(f"Highest Score: {highest_score}")
    print(f"Lowest Score: {lowest_score}")
    print(f"Score Range: {score_range}")


if __name__ == "__main__":
    ft_score_analytics()
