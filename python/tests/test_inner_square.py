"""
Simple tests that we are calculating inner squares properly
"""
from sudoku_solver.validator import get_inner_square


def test_get_inner_square():
    """Test inner square is correct for a few scenarios"""
    assert get_inner_square({'row': '0', 'col': '0'}) == 0
    assert get_inner_square({'row': '3', 'col': '0'}) == 3
    assert get_inner_square({'row': '3', 'col': '3'}) == 4
    assert get_inner_square({'row': '3', 'col': '7'}) == 5
    assert get_inner_square({'row': '7', 'col': '8'}) == 8
    assert get_inner_square({'row': '6', 'col': '6'}) == 8
