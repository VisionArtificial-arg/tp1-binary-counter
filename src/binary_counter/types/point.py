from dataclasses import dataclass
import math


@dataclass(frozen=True)
class Point:
    x: float
    y: float

    def distance_to(self, other: "Point") -> float:
        dx: float = self.x - other.x
        dy: float = self.y - other.y
        return math.hypot(dx, dy)
