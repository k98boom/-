from main import pick_winner


def test_pick_winner_single():
    assert pick_winner(["A"]) == "A"


def test_pick_winner_in_candidates():
    candidates = ["A", "B", "C"]
    winner = pick_winner(candidates)
    assert winner in candidates
