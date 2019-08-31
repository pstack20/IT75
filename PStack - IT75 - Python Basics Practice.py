# Patrick Stack - IT75 - Python Basics Practice

# Question 1 - Store message in variable, print, change print
message = 'Message #1'
print('What message is this? This is '+message)
message = 'Message #2'
print('What message is this? This is '+message)


# Question 2 - Print famous quote reformatting the output
message = 'Nobody expects the Spanish Inquisition!?'
print('Monty Python was known to exclaim: "' + message + '"')


# Question 3 - Favorite number in variable
favoriteNumber = str(20)
message = 'My favorite number is: '
print(message + favoriteNumber)


# Question 4 - Number of characters in a string to variable
rv1 = 'Once upon a midnight dreary, while I pondered, weak and weary,'
rv2 = 'Over many a quaint and curious volume of forgotten lore,'
rv3 = 'While I nodded, nearly napping, suddenly there came a tapping,'
rv4 = 'As of some one gently rapping, rapping at my chamber door.'
rv5 = 'Tis some visitor, I muttered, tapping at my chamber door;'
rv6 = 'Only this and nothing more.'
# cheating by working around the reserved character in 'Tis
rv = len(rv1) + len(rv2) + len(rv3) + len(rv4) + len(rv5) + 1 + len(rv6)
print('The length of the phrase is: ' + str(rv))


