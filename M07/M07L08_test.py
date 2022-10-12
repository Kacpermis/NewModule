from M07L08_subcommands import next_id, add_new, TodoItem, read_or_exit, save_db, DB_FILENAME

def test_empty_list():
    todos = []
    got = next_id(todos)
    assert got == 1

def test_single_todo_with_id_1():
    todos = [TodoItem(id=1, description='', done=False)]
    got = next_id(todos)
    assert got == 2

def test_single_todo_with_id_2():
    todos = [TodoItem(id=2, description='', done=False)]
    got = next_id(todos)
    assert got == 1

def test_multiple_todoitems():
    todos = [
        TodoItem(id=4, description='', done=False),
        TodoItem(id=2, description='', done=False),
        TodoItem(id=1, description='', done=False),
    ]
    got = next_id(todos)
    assert got == 3

def test_add_todo():
    todos = [
        TodoItem(id=4, description='', done=False),
        TodoItem(id=2, description='', done=False),
        TodoItem(id=1, description='', done=False),
    ]
    add_new('desc', todos)
    assert todos ==  [
        TodoItem(id=4, description='', done=False),
        TodoItem(id=2, description='', done=False),
        TodoItem(id=1, description='', done=False),
        TodoItem(id=3, description='desc', done=False),
    ]

def test_persistance(tmpdir):
    with tmpdir.as_cwd():
        todos = [
        TodoItem(id=4, description='', done=False),
        TodoItem(id=2, description='', done=False),
        TodoItem(id=1, description='', done=False),
    ]
    overwrite = 'wb'
    save_db(todos, overwrite)
    got = read_or_exit()
    assert got == todos