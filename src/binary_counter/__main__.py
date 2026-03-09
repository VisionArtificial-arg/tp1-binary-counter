import cv2
import mediapipe.python.solutions.holistic as mp_holistic
import mediapipe.python.solutions.drawing_utils as mp_drawing

from binary_counter.adapters import MediaPipeHandAdapter
from binary_counter.components.extension_detector import ExtensionDetector
from binary_counter.engine import BinaryCounterEngine


holistic_model = mp_holistic.Holistic(
    min_detection_confidence=0.5, min_tracking_confidence=0.5
)

RED_COLOR = (0, 0, 255)
capture = cv2.VideoCapture(0)

adapter = MediaPipeHandAdapter()
detector = ExtensionDetector(0.10)
engine = BinaryCounterEngine(adapter, detector)


while capture.isOpened():
    ret, frame = capture.read()

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    image.flags.writeable = False
    results = holistic_model.process(image)
    image.flags.writeable = True

    result = engine.detect(results)

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Drawing Right hand Land Marks
    mp_drawing.draw_landmarks(
        image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS
    )

    # Drawing Left hand Land Marks
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

    cv2.imshow("Hand Binary Counter", image)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
