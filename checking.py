def other_characters(city):
    if city[0].islower() is True:
        return True
    for c in city:
        if c!=' ' and c.isalpha() is False:
            return True
    return False