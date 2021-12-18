from app.util.logging import append_to_file


def cmd_write(name, text):
    assert name is not None, 'file name should be specified when using \'-n\' flag'
    assert text is not None, 'input text is mandatory'
    append_to_file(name, text)
