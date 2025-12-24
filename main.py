import random
from typing import Sequence


def pick_winner(candidates: Sequence[str]) -> str:
    """从候选人序列中随机选择一个获胜者。"""
    if not candidates:
        raise ValueError("no candidates provided")
    return random.choice(list(candidates))


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        candidates = sys.argv[1:]
    else:
        candidates = ["Alice", "Bob", "Carol"]

    print(pick_winner(candidates))
