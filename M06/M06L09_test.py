from M06L09_eq import collect_operation, RenameOperation

def test_collect_operation_normal_file():
    got = collect_operation('file.txt')
    expected = RenameOperation('file.txt', 'file.bak')
    assert got == expected

def test_collect_operation_missing_extension():
    got = collect_operation('file')
    expected = RenameOperation('file', 'file.bak')
    assert got == expected

def test_collect_operation_multiple_dots():
    got = collect_operation('long.name.txt')
    expected = RenameOperation('long.name.txt', 'long.name.bak')
    assert got == expected

def test_collect_operation_empty_extension():
    got = collect_operation('file.')
    expected = RenameOperation('file.', 'file.bak')
    assert got == expected

def test_collect_operation_paths():
    got = collect_operation('directory.with.dots/file.txt')
    expected = RenameOperation('directory.with.dots/file.txt', 'directory.with.dots/file.bak')
    assert got == expected