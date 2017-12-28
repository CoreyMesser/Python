import unittest
from bunny_def import answer


class KnownXYValues(unittest.TestCase):
    known_values = ((1, 4, 7),
                    (2, 3, 8),
                    (4, 2, 14),
                    (6, 1, 21),
                    (5, 10, 96),
                    (8, 1, 36),
                    (10, 20, 416),
                    (24, 32, 1509),
                    (44, 64, 5715),
                    (73, 97, 14269),
                    (123, 213, 56068),
                    (1, 213, 22579))

    def test_x_y_values(self):
        '''to_bunny should give known reults'''
        for x, y, z in self.known_values:
            result = answer(x, y)
            self.assertEqual(result, z)

if __name__ == '__main__':
    unittest.main()
