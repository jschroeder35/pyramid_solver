import unittest
import pyramid_solver


class TestPyramidSolver(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(pyramid_solver.solve_pyramid(2, [[2]]), '', "Should be \'\'")

    def test_case2(self):
        self.assertEqual(pyramid_solver.solve_pyramid(2, [[1],
                                                          [2, 3],
                                                          [4, 1, 1]]),
                         'LR', "Should be \'LR\'")

    def test_case3(self):
        self.assertEqual(pyramid_solver.solve_pyramid(720, [[2],
                                                            [4, 3],
                                                            [3, 2, 6],
                                                            [2, 9, 5, 2],
                                                            [10, 5, 2, 15, 5]]),
                         'LRLL', "Should be \'LRLL\'")

    def test_case4(self):
        self.assertEqual(pyramid_solver.solve_pyramid(2700, [[2],
                                                             [4, 3],
                                                             [3, 2, 6],
                                                             [2, 9, 5, 2],
                                                             [10, 5, 2, 15, 5]]),
                         'RRLR', "Should be \'RRLR\'")

    def test_case5(self):
        self.assertEqual(pyramid_solver.solve_pyramid(13, [[1],
                                                           [2, 3],
                                                           [4, 5, 6]]),
                         'no solution', "Should be \'no solution\'")


if __name__ == '__main__':
    unittest.main()
