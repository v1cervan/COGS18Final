"""Test for my functions.

Note: here we just test that the functions remove_punctuation and respond_echo execute as expected.
"""

from functions import remove_punctuation, respond_echo


def test_remove_punctuation():

    assert callable(test_remove_punctuation)
    assert isinstance(test_remove_punctuation('a'), str)
    assert test_remove_punctuation("Wow! I'm using way too many exclamation marks!!!") == "Wow Im using way too many exclamation marks"

    assert callable(test_remove_punctuation)


def test_respond_echo():

    assert callable(test_respond_echo)
    assert isinstance(test_respond_echo('ha', 2, ' '), str)
    assert test_respond_echo('yo', 3, ' ') == 'yo yo yo '
    assert test_respond_echo(None, 2, '') == None
    
    assert callable(test_respond_echo)