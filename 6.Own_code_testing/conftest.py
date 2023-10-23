import pytest
from Own_code_testing.code_for_testing import Pictures, Sculptures


@pytest.fixture
def set_pic_params_and_desc():
    set_pic_params_and_desc = Pictures()
    yield set_pic_params_and_desc


@pytest.fixture
def set_sculp_params_and_desc():
    set_sculp_params_and_desc = Sculptures()
    yield set_sculp_params_and_desc


@pytest.fixture
def modify_pic_params():
    modify_pic_params = Pictures('The Beast Goes for a Walk', 1971, 'Maria Prymachenko', True)
    yield modify_pic_params


@pytest.fixture
def modify_sculp_params():
    modify_sculp_params = Sculptures('Violinist on the roof', 2003, 'Seyfaddin Gurbanov', False)
    yield modify_sculp_params
