def hey(phrase):
	if silence(phrase):
		return "Fine. Be that way!"
	elif forceful_question(phrase):
		return "Calm down, I know what I'm doing!"
	elif question(phrase):
		return "Sure."
	elif shout(phrase):
		return "Whoa, chill out!"
	else:
		return "Whatever."

#function to seek if string is question by looikng at last index, using rstrip to pass tests with whitespaces at the end
def question(phrase):
	return phrase.rstrip()[-1] == "?"


#function to test if string is empty also used rstrip to delete all whitespaces
def silence(phrase):
	return len(phrase.rstrip()) == 0


#function to check if string have any uppercases
def shout(phrase):
	return phrase.isupper()

#function checking if string have both functions of shout and question
def forceful_question(phrase):
	if (shout(phrase) == True) and (question(phrase) == True):
		return True