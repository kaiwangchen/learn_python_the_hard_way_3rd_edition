from nose.tools import *
from ex49 import parser
from ex48 import lexicon

def test_1():
    sentence = parser.parse_sentence(lexicon.scan("eat the bear"))
    assert_equal(sentence.subject, 'player')
    assert_equal(sentence.verb, 'eat')
    assert_equal(sentence.object, 'bear')

def test_2():
    sentence = parser.parse_sentence(lexicon.scan("bear go west"))
    assert_equal(sentence.subject, 'bear')
    assert_equal(sentence.verb, 'go')
    assert_equal(sentence.object, 'west')

def test_error():
    words_list = lexicon.scan("open the door and smack the bear in the nose")
    assert_raises(parser.ParserError, parser.parse_sentence, words_list)
