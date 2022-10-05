from M06L09_eq import ext_changing, RenameOperation

def test_ext_changing_normal_file():
    got = ext_changing('file.txt')
    expected = RenameOperation('file.txt', 'file.bak')
    assert got == expected

def test_ext_changing_missing_extension():
    got = ext_changing('file')
    expected = RenameOperation('file', 'file.bak')
    assert got == expected