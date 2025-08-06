import unittest
from app.optimizer import optimize_route

class TestOptimizer(unittest.TestCase):
    def test_optimize_route(self):
        matrix = [
            [0, 2, 9],
            [1, 0, 6],
            [15, 7, 0]
        ]
        route = optimize_route(matrix)
        self.assertEqual(route[0], 0)
        self.assertEqual(len(route), 3)

if __name__ == '__main__':
    unittest.main()
