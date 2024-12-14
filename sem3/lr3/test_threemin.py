from main import threemin
import pytest

# юнит-тестирование с помощью pytest и hypothesis


@pytest.mark.parametrize("inp_lst, expected", [([1, 2, 3, 4, 5], 6),
                                               ([1, 0, 1, 2], 0),
                                               ([-1, 10, 100, -3], -3000),
                                              ([-10, -2, 5, 7, 8], -560)])
def test_simple_hypo(inp_lst, expected):
    assert threemin(inp_lst) == expected