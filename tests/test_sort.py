
from hypothesis import given, settings, unlimited
import hypothesis.strategies as st

import l1p1

def is_sorted(l):
  if(len(l) < 2):
      return True
  else:
    return all([x<=y for x,y in zip(l[:-1],l[1:])])

def test_simple_sort():
  l = [3, 6, 1, 4]
  l_sorted = [1, 3, 4, 6]
  assert l1p1.sort_list(l) == l_sorted

def test_already_sorted():
  l = [1, 2, 3, 4, 5]
  assert l1p1.sort_list(l) == l

def test_reverse_sorted():
  l = [5, 4, 3, 2, 1]
  assert l1p1.sort_list(l) == reversed(l)

@given(st.lists(st.integers()))
def test_random_lists(l):
  assert is_sorted(l1p1.sort_list(l))

