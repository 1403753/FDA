
import numpy as np

import l1p1

def test_case_1():
  x = np.array([1, 2, 3, 4])
  A = np.array([[1, 2, 3, 4], 
                [5, 6, 7, 8], 
                [9, 10, 11, 12], 
                [13, 14, 15, 16]])
  assert l1p1.cubic(x, A) == 742

