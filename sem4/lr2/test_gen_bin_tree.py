from main import gen_bin_tree
import pytest

def test_gen_bin_tree_smallest():
    assert gen_bin_tree(height=0, root=3) == {"3": []}


def test_gen_bin_tree_small():
    assert gen_bin_tree(height=1, root=3) == {"3": [{"5": []}, {"9": []}]}


def test_gen_bin_tree_mid():
    assert gen_bin_tree(height=2, root=3) == {
        "3": [{
            "5": [{
                "7": []
            }, {
                "15": []
            }]
        }, {
            "9": [{
                "11": []
            }, {
                "27": []
            }]
        }]
    }

def test_gen_bin_tree_large_3():
    assert gen_bin_tree(height=3, root=3) == {'3': [{'5': [{'7': [{'9': []}, {'21': []}]}, {'15': [{'17': []}, {'45': []}]}]}, {'9': [{'11': [{'13': []}, {'33': []}]}, {'27': [{'29': []}, {'81': []}]}]}]}

def test_gen_bin_tree_large_4():
    assert gen_bin_tree(height=4, root=3) == {'3': [{'5': [{'7': [{'9': [{'11': []}, {'27': []}]}, {'21': [{'23': []}, {'63': []}]}]}, {'15': [{'17': [{'19': []}, {'51': []}]}, {'45': [{'47': []}, {'135': []}]}]}]}, {'9': [{'11': [{'13': [{'15': []}, {'39': []}]}, {'33': [{'35': []}, {'99': []}]}]}, {'27': [{'29': [{'31': []}, {'87': []}]}, {'81': [{'83': []}, {'243': []}]}]}]}]}


def test_gen_bin_tree_ValueError():
  with pytest.raises(ValueError):
    gen_bin_tree(height= -4, root = 3)

def test_gen_bin_tree_TypeError():
  with pytest.raises(TypeError):
    gen_bin_tree(height= -4, root = '3')