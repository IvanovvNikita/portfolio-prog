import os
import pytest
from datetime import datetime
from decimal import Decimal
from unittest.mock import patch
from currencies import CurrenciesLst


@pytest.fixture
def currencies_lst():
    return CurrenciesLst()

def test_singleton_instance():
    instance1 = CurrenciesLst()
    instance2 = CurrenciesLst()
    assert instance1 is instance2

def test_select_valute(currencies_lst):
    currencies_lst.select_valute("R01235")

    currencies_ids = currencies_lst.get_currencies_ids_lst()
    assert "USD" in currencies_ids

def test_get_last_update(currencies_lst):
    update_time_before = currencies_lst.get_last_update()

    currencies_lst.get_currencies()
    update_time_after = currencies_lst.get_last_update()

    assert isinstance(update_time_before, datetime)
    assert isinstance(update_time_after, datetime)
    assert update_time_before < update_time_after

def test_visualize_currencies(currencies_lst):
    currencies_lst.visualize_currencies()
    assert os.path.exists('currencies.jpg')

def test_del_method(currencies_lst):
    del currencies_lst