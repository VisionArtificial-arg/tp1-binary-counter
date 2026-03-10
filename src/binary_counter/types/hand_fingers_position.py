from dataclasses import dataclass
from typing import Iterator

from binary_counter.components.extension_detector.base import ExtensionDetector
from binary_counter.types import Point


@dataclass(frozen=True)
class HandLandMarks:
    thumb_tip: Point
    index_tip: Point
    middle_tip: Point
    ring_tip: Point
    pinky_tip: Point
    wrist: Point

    def __iter__(self) -> Iterator[Point]:
        yield self.thumb_tip
        yield self.index_tip
        yield self.middle_tip
        yield self.ring_tip
        yield self.pinky_tip

    def binary_value(
        self,
        extension_detector: ExtensionDetector,
    ) -> int:
        return sum(
            1 << i
            for i, finger in enumerate(self)
            if extension_detector.is_extended(self.wrist, finger)
        )
