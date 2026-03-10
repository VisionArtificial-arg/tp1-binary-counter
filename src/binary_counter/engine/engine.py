from binary_counter.adapters import MediaPipeHandAdapter
from binary_counter.components.extension_detector import ExtensionDetector


class BinaryCounterEngine:
    adapter: MediaPipeHandAdapter
    detector: ExtensionDetector

    def __init__(
        self, adapter: MediaPipeHandAdapter, detector: ExtensionDetector
    ) -> None:
        self.adapter = adapter
        self.detector = detector

    def detect(self, results) -> int:
        right_result = 0
        left_result = 0

        if results.right_hand_landmarks:
            hand = self.adapter.to_hand_landmarks(results.right_hand_landmarks)
            right_result = hand.binary_value(self.detector)

        if results.left_hand_landmarks:
            hand = self.adapter.to_hand_landmarks(results.left_hand_landmarks)
            left_result = hand.binary_value(self.detector)

        return right_result + (left_result * 32)
