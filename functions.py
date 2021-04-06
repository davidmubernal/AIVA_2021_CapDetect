import cv2
import os
import numpy as np


class Preprocessing:
    def preprocessing(self, _img):
        """
        Recibe una imagen que preprocesa para favorecer la detección de círculos
        :param _img: imagen a preprocesar
        :return: imagen en blanco y negro con limpieza de ruido y aumento de contraste
        """
        # Imagen a gris
        _img = cv2.cvtColor(_img, cv2.COLOR_BGR2GRAY)
        # Limpieza del ruido de la imagen
        kernel = np.ones((3, 3), np.uint8)
        cv2.GaussianBlur(_img, (7, 7), 1.5, _img, 1.5)
        cv2.erode(src=_img, dst=_img, kernel=kernel, iterations=5)
        cv2.dilate(src=_img, dst=_img, kernel=kernel, iterations=5)
        # Aumento del contraste
        _img = cv2.addWeighted(_img, 1.25, np.zeros(_img.shape, _img.dtype), 0, 0)
        # Prube de realizar una primera detección de bordes
        #_img = cv2.Canny(_img, 100, 150)
        return _img


class Cleaner:
    def clean_circles(self, _img, _circles):
        """
        Aplica las condiciones necesarias para que los círculos detectados sean condensadores
        :param _circles: vector de circulos detectados
        :param _img: imagen de la que se han obtenido los ciruclos
        :result: circulos detectados que son condensadores potenciales
        """
        _capacitors = []
        if _circles is not None:
            _circles = np.uint16(np.around(_circles))
            for idx, i in enumerate(_circles[0, :]):
                for j in _circles[0, idx+1::]:
                    if [abs(i[0] - j[0]), abs(i[1] - j[1])] < [1, 1]:
                        if self.check_color(_img, i):  # Eliminar los agujeros de las placas
                            if not self.is_nearest(_capacitors, [i[0], i[1]]):  # Evitar repetición
                                _capacitors.append([i[0], i[1], i[2]])
        return _capacitors

    def check_color(self, _img, _point):
        """
        Detecta si existe un color cercano al negro cercano al punto central del círculo detectado.
        Si se detecta se supone que es un orificio en la placa.
        Se comprueban todos valores en horizontal, vertical y diagonales a 5 píxeles del centro.
        :param _img: imagen en escala de grises
        :param _point: punto a mirar
        :return: booleano
        """
        _value = 100
        _cond = True if _img[_point[1], _point[0]] > _value else False
        _cond = _cond * True if _img[_point[1]+5, _point[0]] > _value else False
        _cond = _cond * True if _img[_point[1], _point[0]+5] > _value else False
        _cond = _cond * True if _img[_point[1]+5, _point[0]+5] > _value else False
        _cond = _cond * True if _img[_point[1]-5, _point[0]] > _value else False
        _cond = _cond * True if _img[_point[1], _point[0]-5] > _value else False
        _cond = _cond * True if _img[_point[1]-5, _point[0]-5] > _value else False
        _cond = _cond * True if _img[_point[1]+5, _point[0]-5] > _value else False
        _cond = _cond * True if _img[_point[1]-5, _point[0]+5] > _value else False

        return _cond

    def is_nearest(self, _vector, _point):
        """
        Detectamos si existe un punto cercano ya guardado en el vector, de esta forma se evita tener múltiples
        condensadores detectados donde solo hay uno.
        :param _vector: vector donde mirar si extiste un punto cercano
        :param _point: punto a consultar
        :return: boolean
        """
        for _v in _vector:
            _diff = [abs(int(_v[0]) - int(_point[0])), abs(int(_v[1]) - int(_point[1]))]
            if _diff[0] < 50 and _diff[1] < 50:
                return True

        return False


def paint_circles(_img, _circles):
    """
    Pinta los circulos sobre una imagen dada. Esta función sólo sirve con intención de guardar la imagen a posteriori.
    :param _img: imagen sobre la que pintar
    :param _circles: vectores de círculos que pintar
    :return: imagen con ciruclos pintados
    """
    for i in _circles:
        # dibujar circulo 
        cv2.circle(_img, (i[0], i[1]), i[2], (0, 0, 255), 5)
        # dibujar centro
        cv2.circle(_img, (i[0], i[1]), 2, (0, 0, 255), 5)
    return _img

def get_file(_dir):
    """
    Función par la obtención de todos los archivos en el directorio deseado.

    :param _dir: dir will the files to look at
    :return: lista de tuplas con (dirección completa al archivo, nombre del archivo, extensión del archivo)
    """
    if os.path.isdir(_dir):
        _files = []
        for _r, _d, _f in os.walk(_dir):
            for _file in _f:
                _name, _ext = _file.split('.')
                _full_path = os.path.join(_r, _file)
                _files.append([_full_path, _name, _ext])
        return _files
    else:
        return


def save_file(_image, _name, _ext, _folder=None):
    """
    Función para guardar la imagen dado un directorio.
    :param _image: imagen que guardar
    :param _name: nombre de la imagen
    :param _ext: formato en que se guardará la imagen.
    :param _folder: carpeta donde se almacenar la imagen.
    :return:
    """
    if _folder is None:
        cv2.imwrite("{}.{}".format(_name, _ext), _image)
    else:
        if os.path.isdir(_folder):
            pass
        else:
            os.mkdir(_folder)
        cv2.imwrite("{}/{}.{}".format(_folder, _name, _ext), _image)
