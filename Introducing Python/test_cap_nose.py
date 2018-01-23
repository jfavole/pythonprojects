"""
Small program for use learning nose.
"""

import cap
from nose.tools import eq_

def test_one_word(self):
    """
    Should capitalize test word 'duck'
    and return capitalized word, 'Duck'.
    """
    text = 'duck'
    result = cap.just_do_it(text)
    self.assertEqual(result, 'Duck') # Expected result should match 'Duck'.
        
def test_multiple_words(self):
    """
    Should capitalize test phrase 
    'a veritable flock of ducks' and 
    return capitalized phrase
    'A Veritable Flock Of Ducks'.
    """
    text = 'a veritable flock of ducks'
    result = cap.just_do_it(text)
    self.assertEqual(result, 'A Veritable Flock Of Ducks')
    
def test_words_with_apostrophes(self):
    """
    Should capitalize test phrase 
    'I'm fresh out of ideas' and 
    return capitalized phrase
    'I'M FRESH OUT OF IDEAS.'
    """
    text = "I'm fresh out of ideas"
    result = cap.just_do_it(text)
    self.assertEqual(result, "I'm Fresh Out Of Ideas")
    
def test_words_with_quotes(self):
    """
    Edge case that will break capitalization with first double quote.
    """
    text = "\"You're despicable,\" said Daffy Duck"
    result = cap.just_do_it(text)
    self.assertEqual(result, "\"You're Despicable,\" Said Daffy Duck")

