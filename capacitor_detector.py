class CapacitorDetector:

    def detect(self, board_image):
        """

        :param board_image: numpy matrix (n,m)
        :return: tupla con la posición de los condensadores reconocidos
        """
        capacitors = ((10, 50), (15, 50))
        return capacitors

    def recognise_electrolytic(self, board_image):
        """

        :param board_image: numpy matrix (n,m)
        :return: tupla con la posición de los condensadores electrolíticos reconocidos
        """
        capacitors = ((20, 25), (25, 30))
        return capacitors

    def recognise_SMD(self, board_image):
        """

        :param board_image: numpy matrix (n,m)
        :return: tupla con la posición de los condensadores SMD reconocidos
        """
        capacitors = ((50, 100), (55, 100), (100, 20))
        return capacitors