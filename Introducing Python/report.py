def get_description():
    """Return random weather, just like the pros."""
    from random import choice
    
    possibilities = ['Rain', 'Snow', 'Sleet', 'Fog', 'Who knows?']
    
    return choice(possibilities)