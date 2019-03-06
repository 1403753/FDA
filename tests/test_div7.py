
from hypothesis import given, settings, unlimited
import hypothesis.strategies as st

import l1p1

def test_case_1():
  v = l1p1.div7(123, 4)
  assert (v%7) == 0
  assert v == 4123

def test_case_2():
  v = l1p1.div7(39, 2)
  assert (v%7) == 0
  assert v == 329

@given(st.integers(min_value=10), st.integers(min_value=0, max_value=9))
def test_digit_order(n, i):
  assert i < n

@given(st.integers(min_value=10), st.integers(min_value=0, max_value=9))
def test_div_by_7(n, i):
  # don't worry about errors
  try:
    assert l1p1.div(n, i) % 7 == 0
  except Exception as e:
    assert str(e) == "not possible"


