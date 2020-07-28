"""Utility functions for the party app."""
import re

def is_mel(name, email):
    """Return True if name and email are related to Mel.
    >>> is_mel("Mel Melitpolski", "mel@ubermelon.com")
    True
    >>> is_mel("Jane", "Jane@email.com")
    False
    >>> is_mel("Mel Melitpolski", "mel@gmail.com")
    True
    >>> is_mel("Sam", "mel@ubermelon.com")
    True
    >>> is_mel("MEL", "someone@gmail.com")
    True
    >>> is_mel("Notmel", "mel@gmail.com")
    True
    >>> is_mel("someone", "mel@ubermelon.com")
    True
    >>> is_mel("someone", "someone@ubermelon.com")
    False
    """
    email_handle = re.findall(r"(^.+)@", email)
    if email_handle[0]:
        email_handle = email_handle[0]
    else: 
        return False
    return 'mel' in name.lower() or 'mel' in email_handle.lower()


def most_and_least_common_type(treats):
    """Given list of treats, return most and least common treat types.

    Return most and least common treat types in tuple of format
    (most, least). If there's a tie, the dessert that appears
    first in alphabetical order should win.
    
    >>> most_and_least_common_type([{'type':'dessert'}, {'type':'dessert'}])
    ('dessert', 'dessert')
    >>> most_and_least_common_type([{'type':'dessert'}, {'type':'dessert'},{'type':'appetizer'}])
    ('dessert', 'appetizer')
    >>> most_and_least_common_type([{'type':'dessert'}, {'type':'dessert'},{'type':'appetizer'},{'type':'appetizer'}, {'type':'drink'}]) 
    ('appetizer', 'drink')
    >>> most_and_least_common_type([{'type':'dessert'}, {'type':'dessert'},{'type':'appetizer'},{'type':'appetizer'}, {'type':'drink'}, {'type':'dessert'}]) 
    ('dessert', 'drink')
    >>> most_and_least_common_type([])
    (None, None)
    """

    if not treats:
        return (None, None)

    types = {}

    # Count number of each type
    for treat in treats:
        types[treat['type']] = types.get(treat['type'], 0) + 1

    # Get tuples of (treat type, count) in alphabetical order
    types = sorted(types.items())

    # Find the min & max using the count of each tuple (which
    # is stored at index 1)
    most_type, _ = max(types, key=lambda treat_type: treat_type[1])
    least_type, _ = min(types, key=lambda treat_type: treat_type[1])

    return (most_type, least_type)
