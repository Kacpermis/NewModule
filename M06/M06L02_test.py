from M06L02_list_comprehension_1 import txt_search

def test_txt_search():
    got = txt_search(['a.zip', 'b.txt', 'txt'])
    assert got == ['b.txt']