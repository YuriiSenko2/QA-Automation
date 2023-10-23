import pytest
from Own_code_testing.code_for_testing import Pictures, Sculptures


@pytest.mark.smoke
@pytest.mark.parametrize('value', [('\nName: The Beast Goes for a Walk', '\nYear of creation: 1971',
                                    '\nAuthor: Maria Prymachenko', '\nSale status: for sale',
                                    'The Beast goes for a Walk is a colourful painting of a fantastical guard '
                                    'lion against a bright yellow background.')])
def test_pic_params_and_desc_setting(set_pic_params_and_desc, value):
    set_pic_params_and_desc.name = 'The Beast Goes for a Walk'
    set_pic_params_and_desc.creation_year = 1971
    set_pic_params_and_desc.author = 'Maria Prymachenko'
    set_pic_params_and_desc.sale = True
    set_pic_params_and_desc.brief_overview = 'The Beast goes for a Walk is a colourful painting of a ' \
                                                        'fantastical guard lion against a bright yellow background.'
    result = set_pic_params_and_desc.name, set_pic_params_and_desc.creation_year, set_pic_params_and_desc.author, \
             set_pic_params_and_desc.sale, set_pic_params_and_desc.brief_overview
    assert result == value


@pytest.mark.smoke
@pytest.mark.parametrize('value', [('\nName: Violinist on the roof', '\nYear of creation: 2003',
                                    '\nAuthor: Seyfaddin Gurbanov', '\nSale status: not for sale',
                                    'It is a monument to talent, sincerity, disinterested service to art '
                                    'and to the city of Kharkiv')])
def test_sculp_params_and_desc_setting(set_sculp_params_and_desc, value):
    set_sculp_params_and_desc.name = 'Violinist on the roof'
    set_sculp_params_and_desc.creation_year = 2003
    set_sculp_params_and_desc.author = 'Seyfaddin Gurbanov'
    set_sculp_params_and_desc.sale = False
    set_sculp_params_and_desc.brief_overview = 'It is a monument to talent, sincerity, ' \
                                                          'disinterested service to art and to the city of Kharkiv'
    result = set_sculp_params_and_desc.name, set_sculp_params_and_desc.creation_year, set_sculp_params_and_desc.author,\
             set_sculp_params_and_desc.sale, set_sculp_params_and_desc.brief_overview
    assert result == value


@pytest.mark.regression
@pytest.mark.parametrize('value', [('\nName: The Beast Goes for a Walk', '\nYear of creation: 1971',
                                    '\nAuthor: Mary Prymachenko', '\nSale status: for sale')])
def test_pic_params_modification(modify_pic_params, value):
    modify_pic_params.author = 'Mary Prymachenko'
    result = modify_pic_params.name, modify_pic_params.creation_year, modify_pic_params.author, modify_pic_params.sale
    assert result == value


@pytest.mark.regression
@pytest.mark.parametrize('value', [('\nName: Violinist on the rooftop', '\nYear of creation: 2003',
                                    '\nAuthor: Seyfaddin Gurbanov', '\nSale status: not for sale')])
def test_sculp_params_modification(modify_sculp_params, value):
    modify_sculp_params.name = 'Violinist on the rooftop'
    result = modify_sculp_params.name, modify_sculp_params.creation_year, modify_sculp_params.author, \
             modify_sculp_params.sale
    assert result == value


@pytest.mark.regression
@pytest.mark.parametrize(
    "new_status,expected_status", [(False, '\nSale status: not for sale')], ids=['Not for sale now']
)
def test_pic_status_change(modify_pic_params, new_status, expected_status):
    modify_pic_params.change_sale_status(new_status)
    assert modify_pic_params.sale == expected_status


@pytest.mark.regression
@pytest.mark.parametrize(
    "new_status,expected_status", [(True, '\nSale status: for sale')], ids=['For sale now']
)
def test_sculp_status_change(modify_sculp_params, new_status, expected_status):
    modify_sculp_params.change_sale_status(new_status)
    assert modify_sculp_params.sale == expected_status


@pytest.mark.rights
def test_info_in_pics():
    info = Pictures()
    check = info.info_for_qa()
    rights = 'Only an administrator can adjust the "Pictures category"'
    assert rights in check


@pytest.mark.rights
def test_info_in_sculps():
    info = Sculptures()
    check = info.info_for_qa()
    rights = 'Only an administrator can adjust the "Sculptures category"'
    assert rights in check