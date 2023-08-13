"""File contains classes for game lights out."""

import numpy
import math
import pygame
import random


class OneLight:
    def __init__(self, state, x, y):
        """Initialization of OneLight object.

        :param bool state: Beginning state of light True if turned on, False otherwise.
        :param int x: X coordinate of object on board.
        :param int y: Y coordinate of object on board.
        """
        self.__state = state
        self.x = x
        self.y = y
        self.r = 50
        self.color = (250, 234, 10) if state else (0, 0, 0)

    @property
    def state(self):
        """Return state property."""
        return self.__state

    def is_point_in(self, click_coordinates):
        """Check if light was clicked within its borders.

        :param tuple(int, int) click_coordinates: Point of click.
        """
        dx = click_coordinates[0] - self.x
        dy = click_coordinates[1] - self.y
        return math.hypot(dx, dy) <= self.r

    def set_color(self):
        """Set color based on state of the light."""
        self.color = (250, 234, 10) if self.__state else (0, 0, 0)

    def draw(self, screen):
        """Draw circle on selected screen.

        :param pygame.surface.Surface screen: Game window.
        """
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r, 0)

    def switch_state(self):
        """Change state of the light to the opposite one and update color.

        for example: If light was turned off, then it turns it on by switching state from False to True.
        """
        self.__state = not self.__state
        self.set_color()


class Board:
    def __init__(self, size_of_board):
        """Initialization of Board which consists of OneLight objects.

        :param int size_of_board: Size of the board. Given size 5 will result in board of size 5x5.
        """
        self.__size_of_board = size_of_board
        self.__list_of_lights = []
        self.__get_solvable_board()

    def __get_solvable_board(self):
        """Create random solvable board."""
        rows = []
        list_of_states = []
        possible_lights_on = self.__get_list_of_even_numbers()
        while sum(rows) < 10:
            rows = []
            for i in range(5):
                rows.append(random.choice(possible_lights_on))
            print(sum(rows))
            print(rows)

        for one_row in rows:
            tmp = [False for _ in range(5)]
            for one_val in range(one_row):
                tmp[one_val] |= True
            numpy.random.shuffle(tmp)
            list_of_states.extend(tmp)

        for i in range(1, self.__size_of_board+1):
            for j in range(1, self.__size_of_board+1):
                self.__list_of_lights.append(OneLight(list_of_states[i+j-2], j * 120, i * 120))

    def __get_list_of_even_numbers(self):
        """Get list of even numbers out of board's size.

        :return List of all even numbers out of board size.
        :rtype List[int]
        """
        list_of_rows = [i for i in range(self.__size_of_board)]
        for i in list_of_rows:
            if i % 2 != 0:
                list_of_rows.remove(i)
        return list_of_rows

    @property
    def list_of_lights(self):
        """Returns list of lights objects."""
        return self.__list_of_lights

    def switch_light(self, idx):
        """Switch state of selected light on specific coordinates and its neighbour light states.

        :param int idx: Index of the selected light to be switched on/off.
        """
        self.__list_of_lights[idx].switch_state()
        # switch lights for all neighbour lights
        if idx - 5 >= 0:  # upper light
            self.__list_of_lights[idx - 5].switch_state()

        if idx + 5 < len(self.__list_of_lights):  # lower light
            self.__list_of_lights[idx + 5].switch_state()

        if idx - 1 >= 0 and idx % self.__size_of_board != 0:  # left light
            self.__list_of_lights[idx - 1].switch_state()

        if idx + 1 < len(self.__list_of_lights) and (idx + 1) % self.__size_of_board != 0:  # right light
            self.__list_of_lights[idx + 1].switch_state()

    def show_board(self):
        """Prints current state of board."""
        for i in range(0, self.__size_of_board):
            for j in range(0, self.__size_of_board):
                print(f"{1 if self.__list_of_lights[i+j].state else 0} ", end="")
            print("\n", end="")
