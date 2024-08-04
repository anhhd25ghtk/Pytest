import os
from mock_examples.file_handler import create_file,remove_file


def test_create_file(mocker):
    filename = 'delete.txt'
    mock_file = mocker.mock_open()
    mocker.patch("builtins.open", mock_file)

    create_file(filename=filename)
    mock_file.assert_called_once_with(filename,'w')
    mock_file().write.assert_called_once_with('hello')

def test_delete_file(mocker):
    filename = 'delete.txt'
    mocker_remove = mocker.patch("os.remove")
    