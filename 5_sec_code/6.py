# x = 1
# assert x == 2, "xは2である必要があります"

class ScoreBoard():
    def __init__(self):
        self._scores = []

    def add_score(self, score: int):
        assert isinstance(
            score, int
        ), "scoreはintにする必要があります"
        self._scores.append(score)