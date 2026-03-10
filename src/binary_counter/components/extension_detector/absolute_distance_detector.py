from binary_counter.components.extension_detector import ExtensionDetector
from binary_counter.types import Point


class AbsoluteDistanceExtensionDetector(ExtensionDetector):
    extension_threshold: float

    def __init__(self, extension_threshold: float) -> None:
        self.extension_threshold = extension_threshold

    def is_extended(self, wrist: Point, finger_tip: Point) -> bool:
        return wrist.distance_to(finger_tip) > self.extension_threshold
