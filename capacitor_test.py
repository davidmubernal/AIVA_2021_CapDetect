import unittest
import cv2
from capacitor_detector import CapacitorDetector


class TestCapacitorDetector(unittest.TestCase):
    def test_capacitor_detector(self):
        board_image = cv2.imread("./../Imagenes/Test/rec1-3.jpg")
        detector = CapacitorDetector()
        result = detector.detect(board_image)
        self.assertEqual(result, ((10, 50), (15, 50)))

    def test_capacitor_electrolytic(self):
        board_image = cv2.imread("./../Imagenes/Test/rec1-3.jpg")
        detector = CapacitorDetector()
        result = detector.recognise_electrolytic(board_image)
        self.assertEqual(result, ((20, 25), (25, 30)))

    def test_capacitor_SMD(self):
        board_image = cv2.imread("./../Imagenes/Test/rec1-3.jpg")
        detector = CapacitorDetector()
        result = detector.recognise_SMD(board_image)
        self.assertEqual(result, ((50, 10), (55, 100), (100, 20)))


if __name__ == "__main__":
    unittest.main()
