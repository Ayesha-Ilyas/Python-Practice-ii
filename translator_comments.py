def trans(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter in "aeiou":
                translation = translation + "g"
            else:
                translation = translation + "G"
        else:
            translation = translation + letter
    return translation
# hashtag is used  for single line comment. but it is considered std for all commenting. for multiple line
# use multiple hashtags.
'''
this is for multiple line commenting. three single quote marks.
'''

phrase = input("enter a phrase: ")
print(trans(phrase))
