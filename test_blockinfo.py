import math
import pytest
from blockinfo import BlockInfo

@pytest.fixture
def single_tx_block():
    hash_value = '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f'
    return BlockInfo(hash_value)

@pytest.fixture
def multiple_tx_block():
    hash_value = '0000000000000e102232eeb35175920438b8d8de12cab20f3e4d5b6e56dbca95'
    return BlockInfo(hash_value)

def test_get_api_url(single_tx_block):
    assert single_tx_block.api_url == 'https://blockchain.info/block/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f?format=json'

def test_n_tx(single_tx_block, multiple_tx_block):
    assert single_tx_block.n_tx == 1
    assert multiple_tx_block.n_tx == 9

def test_avg_tx_value(single_tx_block, multiple_tx_block):
    assert math.isclose(single_tx_block.avg_tx_value, 50, rel_tol=1e-8)
    assert math.isclose(multiple_tx_block.avg_tx_value, 39.65358258, rel_tol=1e-8)
