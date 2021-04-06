import unittest
import cv2
from capacitor_detector import CapacitorDetector


class TestCapacitorDetector(unittest.TestCase):
    def test_capacitor_detector_1(self):
        board_image = cv2.imread("./img/test/rec1-3.jpg")
        detector = CapacitorDetector()
        result = detector.detect(board_image)
        self.assertEqual([[3052, 2186, 34], [2530, 2200, 34], [3390, 2004, 31], [3446, 2682, 30], [1968, 1292, 48],
                          [2266, 2762, 25], [3194, 2192, 36], [3074, 2858, 34], [3316, 2400, 31], [3160, 1996, 26],
                          [3408, 2394, 46], [3192, 2108, 36], [3204, 2320, 34], [2064, 1282, 31], [2294, 1312, 25],
                          [2548, 2874, 34], [3202, 2476, 35], [2328, 1436, 38], [1826, 2872, 39], [2008, 1518, 37],
                          [2068, 580, 38], [1840, 2804, 29], [3204, 2408, 37], [3218, 2568, 40], [3218, 2834, 44],
                          [3210, 2758, 36], [1798, 1564, 29], [2408, 1432, 24], [2930, 1932, 29], [2004, 1582, 28],
                          [3008, 1662, 27], [3200, 2664, 27], [2584, 1266, 25], [2248, 1438, 39], [2316, 460, 24],
                          [2656, 1266, 22], [1870, 1376, 22]],
                         result)

    def test_capacitor_detector_2(self):
        board_image = cv2.imread("./img/test/rec10-1.jpg")
        detector = CapacitorDetector()
        result = detector.detect(board_image)
        self.assertEqual([[2874, 2220, 43], [2724, 1310, 45], [3042, 1974, 42], [2648, 1864, 43], [2960, 1646, 44],
                          [2724, 1442, 43], [3186, 1362, 37], [2726, 1678, 44], [1980, 786, 19], [2604, 1950, 16]],
                         result)

    def test_capacitor_detector_3(self):
        board_image = cv2.imread("./img/test/rec11-1.jpg")
        detector = CapacitorDetector()
        result = detector.detect(board_image)
        self.assertEqual([], result)
    """
    def test_capacitor_electrolytic(self):
        board_image = cv2.imread("./img/test/rec1-3.jpg")
        detector = CapacitorDetector()
        result = detector.recognise_electrolytic(board_image)
        self.assertEqual(result, ((20, 25), (25, 30)))

    def test_capacitor_SMD(self):
        board_image = cv2.imread("./img/test/rec1-3.jpg")
        detector = CapacitorDetector()
        result = detector.recognise_SMD(board_image)
        self.assertEqual(result, ((50, 10), (55, 100), (100, 20)))"""


if __name__ == "__main__":
    unittest.main()
