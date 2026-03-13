import cv2
import mediapipe.python.solutions.holistic as mp_holistic
import mediapipe.python.solutions.drawing_utils as mp_drawing

from binary_counter.adapters import MediaPipeHandAdapter
from binary_counter.components.extension_detector import (
    AbsoluteDistanceExtensionDetector,
)
from binary_counter.engine import BinaryCounterEngine


def nothing(x):
    pass


holistic_model = mp_holistic.Holistic(
    min_detection_confidence=0.5, min_tracking_confidence=0.5
)

RED_COLOR = (0, 0, 255)
capture = cv2.VideoCapture(0)

adapter = MediaPipeHandAdapter()

# Initial detector value
initial_threshold = 0.18
detector = AbsoluteDistanceExtensionDetector(initial_threshold)
engine = BinaryCounterEngine(adapter, detector)

cv2.namedWindow("Hand Binary Counter")
cv2.createTrackbar(
    "Threshold", "Hand Binary Counter", int(initial_threshold * 100), 100, nothing
)

while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        break

    # Get slider value
    threshold = cv2.getTrackbarPos("Threshold", "Hand Binary Counter") / 100.0

    # Recreate detector with the updated threshold
    engine.detector = AbsoluteDistanceExtensionDetector(threshold)

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    image.flags.writeable = False
    results = holistic_model.process(image)
    image.flags.writeable = True

    result = engine.detect(results)

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    mp_drawing.draw_landmarks(
        image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS
    )

    mp_drawing.draw_landmarks(
        image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS
    )

    cv2.putText(
        image,
        f"Counted: {result}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        RED_COLOR,
        2,
    )

    cv2.putText(
        image,
        f"Threshold: {threshold:.2f}",
        (10, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        RED_COLOR,
        2,
    )

    cv2.imshow("Hand Binary Counter", image)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()
