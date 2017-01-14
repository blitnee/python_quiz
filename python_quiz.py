easy_question = """\n'__1__' is a tool used in python that gives the '__2__' position
in the search string where the '__3__' string appears. If the
target string is not found the output is '__4__'.\n"""
# lowest level question

easy_answer = ['.find', 'first', 'target', '-1']
# lowest level answers

medium_question = """\nThe '__1__' command will display the results of a function
call. To produce output, functions must end with a '__2__' statement.
'__3__' represents an equality comparison. A '__4__' statement will always
return true or false.\n"""
# middle level question

medium_answer = ["print", "return", "==", "boolean"]
# middle level answers

hard_question = """\nSome list operations include: '__1__', which is invoked on a
list adding an element to the '__2__' of the list. '__3__' makes a new
list by combining two existing lists. '__4__' outputs the number of
elements in a given list.\n"""
# highest level question

hard_answer = ["append", "end", "plus", "len"]
# highest level answer

blanks = ['__1__', '__2__', '__3__', '__4__']
# assings blanks to 'blanks' list for replacing in string


def quiz_par(user_level):
    '''assigns selected user level to quiz question and answers'''
    if user_level == "easy":
        return (easy_question, easy_answer)
    elif user_level == "medium":
        return (medium_question, medium_answer)
    elif user_level == "hard":
        return (hard_question, hard_answer)


def quiz_rules(user_level, blanks, questions, answers):
    '''defines rules for quiz, including lives'''
    print questions
    # displays selected quiz question
    index = 0
    # starts quiz at first index
    lives = 4
    # user begins with 4 lives
    while index < len(blanks):
        # while loop that allows user 4 attempts
        user_answer = raw_input("\nFill in blanks as they appear: ")
        # prompts user to input first answer, assigns answer to 'user_answer'
        if user_answer == answers[index]:
            # compares user's answer to answers in level selected
            questions = questions.replace(blanks[index], answers[index])
            # reassigns questions so blanks are replaced with answers, ordered
            print ("Correct!")
            # prompts user that their answer is correct
            print questions
            # reprints appended string
            index = (index + 1)
            # moves quiz elements (blanks & answers) forward one step
        else:
            # alternative condition, if user answer is not in answers
            lives = (lives - 1)
            # removes one life
            print ("Try again...")
            # prompts user to enter different answer
        if lives == 0:
            # condition when all lives lost
            print("\nGAME OVER :(\n")
            # prompts user that they are out of lives
            return exit()
            # ends quiz
        elif index == len(blanks):
            # alternative condition if lives != 0
            print("\nFantastic job! YOU WIN!\n")
            # prompts user that they have won the game


def play_quiz():
    '''takes in user data (name & level), starts quiz'''
    user_name = raw_input("\nPlease enter your name: ")
    # prompts user to input their name
    user_level = raw_input("\nChoose your difficulty (easy/medium/hard): ")
    # prompts user to choose a quiz difficulty
    leveler = ['easy', 'medium', 'hard']
    # assigns level options to leveler list
    while user_level not in leveler:
        # while loop that does not allow user to input outside of leveler list
        user_level = raw_input("Choose your difficulty (easy/medium/hard):")
        # prompts user to input difficulty again
    print "\nHello, "+user_name+"! I see you're playing on "+user_level+"."
    # prints greeting to user, utilizing user inputs
    print "\nFill in the blanks. You have 4 lives, then it's game over!"
    # prints instructions to user
    questions, answers = quiz_par(user_level)
    # assigns questions and answers to quiz_par for replacement
    return quiz_rules(user_level, blanks, questions, answers)
    # continues game through quiz_rules function

play_quiz()
# starts quiz
