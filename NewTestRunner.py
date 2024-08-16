import unittest

import NewNewRunner
from unittest import TestCase
import logging
logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_test.log', encoding='UTF-8',
                        format= '%(asctime)s | %(levelname)s | %(message)s')

class RunnerTest(TestCase):

    def test_walk(self):
        try:
            logging.info('test_walk выполнен успешно')
            self.sport = NewNewRunner.Runner('Ed', -200)
            for i in range(10):
                self.sport.walk()
            self.assertEqual(self.sport.distance, 50)
        except ValueError as er:
            print('Скорость не может быть отрицательной')
            logging.warning('Неверная скорость для Runner')

    def test_run(self):
        try:
            logging.info('test_run выполнен успешно')
            self.sport = NewNewRunner.Runner(129, 50)
            for i in range(10):
                self.sport.run()
            self.assertEqual(self.sport.distance, 100)
        except TypeError as er:
            print('Имя может быть только str')
            logging.warning('Неверный тип данных для объекта Runner')

    def test_challenge(self):
        self.sport1 = NewNewRunner.Runner('Max')
        self.sport2 = NewNewRunner.Runner('Vic')
        for i in range(10):
            self.sport1.run()
            self.sport2.walk()
        self.assertNotEqual(self.sport1.distance, self.sport2.distance)



if __name__ == 'main':
    unittest.main()
