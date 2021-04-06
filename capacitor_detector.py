from functions import Preprocessing, Cleaner
import cv2


class CapacitorDetector:

    def detect(self, _board_image):
        """
        Funcion para la detección de circulos y posterior limpieza para dejar solo condensadores
        :param _board_image: numpy matrix (n,m)
        :return: array con la posición de los condensadores reconocidos
        """
        preproces = Preprocessing()
        _img = preproces.preprocessing(_board_image)
        _circles = cv2.HoughCircles(_img, cv2.HOUGH_GRADIENT, 1, 0.5, param1=65, param2=30, minRadius=15, maxRadius=50)
        cleaner = Cleaner()
        _capacitors = cleaner.clean_circles(_img, _circles)
        return _capacitors
