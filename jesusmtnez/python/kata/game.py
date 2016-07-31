class Game():
    def __init__(self):
        self._rolls = [0] * 23
        self._current_roll = 0

    def roll(self, pins):
        self._rolls[self._current_roll] += pins
        self._current_roll += 1 if pins < 10 else 2

    def score(self):
        score = 0
        for frame in range(0, 20, 2):
            if self._is_strike(frame):
                score += 10 + self._rolls[frame + 2]
                score += self._rolls[frame + 4] if self._is_strike(frame + 2) else self._rolls[frame + 3]
            elif self._is_spare(frame):
                score += 10 + self._rolls[frame + 2]
            else:
                score += self._frame_score(frame)
        return score

    def _is_spare(self, frame):
        return self._rolls[frame] + self._rolls[frame + 1] == 10

    def _is_strike(self, frame):
        return self._rolls[frame] == 10

    def _frame_score(self, frame):
        return self._rolls[frame] + self._rolls[frame + 1]
