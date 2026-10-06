from lib.join_chat_participants import *

def test_no_participants():
    result = join_chat_participants([])
    assert result == ""

def test_one_participant():
    result = join_chat_participants(["Bart"])
    assert result == "Bart"

