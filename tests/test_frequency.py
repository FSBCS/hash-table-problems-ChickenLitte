import os, sys
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from p2 import k_most_frequent

def test_basic():
    assert k_most_frequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]

def test_single_element():
    assert k_most_frequent([1], 1) == [1]

def test_empty_list():
    assert k_most_frequent([], 1) == []

def test_k_greater_than_list():
    assert k_most_frequent([1, 2, 3], 5) == [1, 2, 3]

def test_multiple_frequent_elements():
    assert k_most_frequent([1, 1, 2, 2, 3, 3], 2) == [1, 2, 3]
