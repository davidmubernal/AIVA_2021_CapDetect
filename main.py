import cv2
from functions import paint_circles, save_file
from capacitor_detector import CapacitorDetector
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-image", "--input_image", required=True, help="Path where the image resides")
ap.add_argument("-output", "--output_image", required=False, help="Path to save the image")

args =vars(ap.parse_args())

input_path = args['input_image']
output_path = args['output_image']


if __name__ == "__main__":
    directory = input_path  # "../Imagenes/Test/rec11-1.jpg"
    folder_to_save = output_path  # "../Imagenes/resultados/detect"

    img = cv2.imread(directory)
    detector = CapacitorDetector()
    capacitors = detector.detect(img)
    if output_path is not None:
        img = paint_circles(img, capacitors)
        save_file(img, "output_image_1-3", "jpg", folder_to_save)
