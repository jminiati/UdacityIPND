"""IPND Stage 2 Create a Quiz Project, by John T. Miniati

This program presents the user with a quiz string, "quiz", which has numbered questions in line, such as "___1___".
For each numbered question, the user provides a response, which is compared against the proper answer. 
There are three different quizes, "easy", "medium" and "hard", and the user is asked to select which one to run.
So, each quiz is defined by the quiz string ("easy_quiz") and 3 lists: the question numbers list ("easy_qnum"), the answers list ("easy_a"), 
and the responses list ("easy_responses").  
"""

"""Initialize three quizes, one for each level of difficulty."""  
easy_qnum = ["___1___", "___2___", "___3___", "___4___"]
easy_a = ["bug", "test", "cases", "tracebacks"]
assert len(easy_qnum) == len(easy_a)
easy_responses = ["", "", "", ""]
assert len(easy_responses) == len(easy_qnum)
easy_quiz = """It is improbable that you will write any significant code without a single ___1___ on the first pass.  
A few good ways to reduce the number of  ___1___s is to: 1) break down the problem, 
2) consider inputs and outputs, and 3) define  ___2___  ___3___up front.  
When you run into problems, the last line of Python ___4___ will tell you what went wrong."""

med_qnum = ["___1___", "___2___", "___3___", "___4___"]
med_a = ["function", "parameters", "None", "list"]
assert len(med_qnum) == len(med_a)
med_responses = ["", "", "", ""]
assert len(med_responses) == len(med_qnum)
med_quiz = """A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes 
by adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ 
if you don't specify the value to return. ___2___ can be standard data types such as string, number, 
dictionary, tuple, and ___4___ or can be more complicated such as objects and 
lambda functions. """ 

hard_qnum = ["___1___", "___2___", "___3___", "___4___", "___5___"]
hard_a = ["global", "docstrings", "lower", "function", "return"]
assert len(hard_qnum) == len(hard_a)
hard_responses = ["", "", "", "", ""]
assert len(hard_responses) == len(hard_qnum)
hard_quiz = """Here are a few python best-practices I learned doing this project:
Avoid ___1___ variables, as they are "so notoriously problematic, that some programmers call them evil".
In writing comments, it's best to use ___2___, which allows users to call your function comments using help().  
To avoid data input errors from the user entering "Easy" or "EASY" (vs. the correct "easy"), use python's ___3___() method.  
We use ___4___s to break a program into logical, manageable chunks.  
A ___5___ statement ends a ___4___ right away."""

""" Initialize list of lists for the quiz.

The program uses a list of lists for the quiz, one of which will be active, based on the user's selection.  
For example, if the user types in "easy", level_index = 0 and quiz[0] will be the active quiz.
"""
qnums = [easy_qnum, med_qnum, hard_qnum]
answers = [easy_a, med_a, hard_a]
responses = [easy_responses, med_responses, hard_responses]
quiz = [easy_quiz, med_quiz, hard_quiz]
	
def check_level(level, level_options):
	"""Check if an input level is valid (easy, medium or hard)

	Input: level (string entered by user), and level_options (valid entries)
	Return: level (if a valid entry) or None (if not)
	"""
	for options in level_options:
		if level == options:
			return level
	return None
	
def input_level():
	"""Asks user to enter level of difficulty.

	No input
	Returns level_index, which is an index for the selected level of difficulty, and will define which quiz to use.
	"""
	level_instructions = "\n" + "Please select a game difficulty by typing it in!" + "\n"
	level_options = ["easy", "medium", "hard"]
	error_level = "\n" + "That's not an option! " + "\n"
	level = "" 
	print level_instructions
	level = raw_input('Possible choices include: easy, medium, or hard: ')
	level = level.lower()
	while check_level(level, level_options) == None:
		print "\n" + error_level + "\n"
		print "\n" + level_instructions + "\n"
		level = raw_input('Possible choices include: easy, medium, or hard: ')
		check_level(level, level_options)
	print "\n" + "You've chosen %s!" % level
	level_index = level_options.index(level)
	return level_index
	
def set_quiz_level(level_index, quiz, qnums, answers, responses):
	"""Sets the level of the quiz to be run, based on user's typed input from valid choices (easy, medium, hard)

	Input: level_index (index for level of difficulty input by user) and the superset of quiz information
	Return: the specific quiz information for the level: active_quiz, active_qnums, active_answers, active_responses
	"""
	active_quiz = quiz[level_index]
	active_qnums = qnums[level_index]
	active_answers = answers[level_index]
	active_responses = responses[level_index]
	return active_quiz, active_qnums, active_answers, active_responses
	
def max_guesses():
	"""Asks user to enter max_guesses, the maximum guesses allowed per question.

	No input
	Returns max_guesses
	Note: in lieu of coding for all the corner cases, as I did in my original version, my reviewer suggested http://stackoverflow.com/questions/16488278/how-to-check-if-a-variable-is-an-integer-or-a-string
	I took his suggested, and also used this code as reference: http://stackoverflow.com/questions/26198131/check-if-input-is-positive-integer
	"""
	print "\n" + "How many guesses would you like per problem?" + "\n"
	max_guesses = None
	while max_guesses is None:
		try:
			max_input = int(raw_input('Please enter a positive integer number: '))
			if max_input < 1:
				print "\n" + "You need at least one guess!" + "\n"
			else:
				max_guesses = max_input
				print "\n" + "OK, you'll have %d try(ies) for each question.  Good luck!" % max_guesses
				return max_guesses
			# else:
			# 	print "\n" + "You need at least one guess!" + "\n"
		except ValueError:
			print "\n" + "You entered a non-integer. Please enter a positive integer." + "\n"

	
def qnum_in_quiz(word, qnum_list):
	"""Evaluate to see if a string is a subset of a list item

	More specifically, If word is a subset of an item in qnum_list, return qnum.  Otherwise, return None
	Input: word and qnum_list
	Return: qnum, an item in qnum_list
	"""
	for qnum in qnum_list:
		if qnum in word:
			return qnum
	return None

	
def updated_quiz(quiz_needs_update, qnum_to_replace, correct_response, qnum_list):
	"""Replace correct response for current qnum in active_quiz string, to create new_quiz_str.

	Input quiz_needs_update, qnum_to_replace, correct_response, qnum_list
	Return new_quiz_str
	"""
	new_quiz = []
	new_quiz_str = ""
	replace_word = ""
	quiz_list = quiz_needs_update.split()
	word_qnum = ""
	for word in quiz_list:
		if qnum_in_quiz(word, qnum_list) == qnum_to_replace:
			word_qnum = qnum_in_quiz(word, qnum_list)
			replace_word = word.replace(word_qnum, correct_response)
			new_quiz.append(replace_word)
		else:
			new_quiz.append(word)
	new_quiz_str = ' '.join(map(str,new_quiz))
	return new_quiz_str


def correct_response(active_quiz, i_qnum, current_response, active_qnums, num_guesses_left, max_num_guesses, win):
	""" Process correct_response.  Print appropriate messages and check if user has won.

	Input active_quiz, i_qnum, current_response, active_qnums, num_guesses_left, win
	Return active_quiz, i_qnum, num_guesses_left, win
	"""
	print "\n" + "Correct!" + "\n"
	active_quiz = updated_quiz(active_quiz, active_qnums[i_qnum], current_response, active_qnums)
	print "\n" + "The current paragraph reads as such: " + "\n" +  active_quiz + "\n"
	if i_qnum == len(active_qnums) - 1:
		win = True
		return active_quiz, i_qnum, num_guesses_left, win
	else:
		num_guesses_left = max_num_guesses
		i_qnum += 1
		win = None
		# print "num guesses left is: %d " % num_guesses_left
		return active_quiz, i_qnum, num_guesses_left, win


def incorrect_response(active_quiz, num_guesses_left, win):
	""" Process incorrect_response.  Print appropriate messages and check if user has lost.

	Input active_quiz, num_guesses_left, win
	Return num_guesses_left, win
	"""
	num_guesses_left += -1
	if num_guesses_left < 1:
		win = False
		print "\n" + "Oh No!! That isn't the correct answer, and you're out of guesses!" + "\n"
		return num_guesses_left, win
	else:
		print "\n" + "That isn't the correct answer! " + "\n" + "Let's try again! You have %d try(ies) left." % num_guesses_left
		print "\n" + "The current paragraph reads as such: " + "\n" +  active_quiz + "\n"
	return num_guesses_left, win

	
def play_game(active_quiz, active_qnums, active_answers, active_responses, max_num_guesses):
	""" Execute the Quiz game, by iteratively asking for user input and checking responses vs. answers.

	Input active_quiz, active_qnums, active_answers, active_responses, based on user chosen level of difficulty
	Return conclude_message
	"""
	num_guesses_left = max_num_guesses
	print "\n" + "The current paragraph reads as such: " + "\n" +  active_quiz + "\n"
	win = None
	i_qnum = 0  # index for the number of questions in the quiz
	while i_qnum < len(active_qnums):
		active_responses[i_qnum] = raw_input('What should be substituted in for ' + active_qnums[i_qnum] + '? :')
		if active_responses[i_qnum].lower() == active_answers[i_qnum]:
			active_quiz, i_qnum, num_guesses_left, win = correct_response(active_quiz, i_qnum, active_responses[i_qnum], active_qnums, num_guesses_left, max_num_guesses, win)
			if win == True:
				return "CONGRATULATIONS, YOU WON!!"
		else:
			num_guesses_left, win = incorrect_response(active_quiz, num_guesses_left, win)
			if win == False:
				return "Bummer! Why don't you try this quiz again?"


"""Main program:"""
level_index = input_level()
max_num_guesses = max_guesses()
active_qnums = qnums[level_index]
conclude_message = ""
active_quiz, active_qnums, active_answers, active_responses = set_quiz_level(level_index, quiz, qnums, answers, responses)
conclude_message = play_game(active_quiz, active_qnums, active_answers, active_responses, max_num_guesses)
print "\n" + conclude_message + "\n"

# end program












