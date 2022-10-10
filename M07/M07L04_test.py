from M07L04_break import generate_name

def test_generate_name_when_no_file(tmpdir):
    with tmpdir.as_cwd():
        filename = 'file.txt'
        got = generate_name(filename)
        assert got == filename

def test_generate_name_when_file_exists(tmpdir):
    with tmpdir.as_cwd():
        open('file.txt', 'w').close()
        open('file-2.txt', 'w').close()
        got = generate_name('file.txt')
        expected = 'file-3.txt'
        assert got == expected