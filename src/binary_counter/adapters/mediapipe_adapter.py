import mediapipe.python.solutions.holistic as mp_holistic
from binary_counter.types.hand_fingers_position import HandLandMarks
from binary_counter.types.point import Point


class MediaPipeHandAdapter:
    def to_hand_landmarks(self, mp_hand):

        return HandLandMarks(
            thumb_tip=self._point(mp_hand, mp_holistic.HandLandmark.THUMB_TIP),
            index_tip=self._point(mp_hand, mp_holistic.HandLandmark.INDEX_FINGER_TIP),
            middle_tip=self._point(mp_hand, mp_holistic.HandLandmark.MIDDLE_FINGER_TIP),
            ring_tip=self._point(mp_hand, mp_holistic.HandLandmark.RING_FINGER_TIP),
            pinky_tip=self._point(mp_hand, mp_holistic.HandLandmark.PINKY_TIP),
            wrist=self._point(mp_hand, mp_holistic.HandLandmark.WRIST),
        )

    def _point(self, hand, landmark):
        p = hand.landmark[landmark]
        return Point(p.x, p.y)
