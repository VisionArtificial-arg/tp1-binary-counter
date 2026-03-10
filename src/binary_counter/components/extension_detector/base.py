from abc import ABC, abstractmethod

from binary_counter.types import Point


class ExtensionDetector(ABC):
    @abstractmethod
    def is_extended(self, wrist: Point, finger_tip: Point) -> bool:
        pass
