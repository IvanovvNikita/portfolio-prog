from decimal import Decimal

import pytest

from currencies import CurrenciesLst



@pytest.fixture
def currencies_lst():
    return CurrenciesLst()
     


def test_get_currencies(currencies_lst):
    currencies = currencies_lst.get_currencies()
    assert len(currencies) == 0

def test_get_valute(currencies_lst):
    currencies_lst.select_valute("R01235")
    valute = currencies_lst["USD"]
    assert isinstance(valute, dict)
    assert "USD" in valute

def test_get_valute_invalid_id(currencies_lst):
    valute = currencies_lst["INVALID"]
    assert isinstance(valute, dict)
    assert "INVALID" in valute
    assert valute["INVALID"] is None

def test_select_valute(currencies_lst):
    currencies_ids_lst = currencies_lst.get_currencies_ids_lst()
    assert len(currencies_ids_lst) == 1

    currencies_lst.select_valute("USD")
    currencies_ids_lst = currencies_lst.get_currencies_ids_lst()
    assert len(currencies_ids_lst) == 2
    assert "USD" in currencies_ids_lst

def test_visualize_currencies(currencies_lst):
    currencies_lst.visualize_currencies()