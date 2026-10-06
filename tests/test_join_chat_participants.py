from lib.join_chat_participants import *

def test_no_participants():
    result = join_chat_participants([])
    assert result == ""

def test_one_participant():
    result = join_chat_participants(["Bart"])
    assert result == "Bart"

def test_two_participants():
    result = join_chat_participants(["Bart", "Lisa"])
    assert result == "Bart & Lisa"

def test_more_than_two():
    result = join_chat_participants(["Bart", "Lisa", "Maggie"])
    assert result == "Bart, Lisa & Maggie"