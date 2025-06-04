from dataclasses import dataclass


@dataclass
class Stato:
    StateAbb: str
    CCode: int
    StateNme: str

    def __eq__(self, other):
        return self.StateAbb == other.StateAbb

    def __hash__(self):
        return hash(self.StateAbb)

    def __str__(self):
        return self.StateNme

    def __lt__(self, other):
        return self.StateAbb < other.StateAbb