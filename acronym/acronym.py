def abbreviate(text):
    pr = ''
    abbreviation = ''
    for i in text:
        if pr in " -" or pr.islower() and i.isupper():
            abbreviation += i.upper()
        pr = i
    return abbreviation


#print abbreviate('PHP: Hypertext Preprocessor')
#print abbreviate('Complementary metal-oxide semiconductor')
