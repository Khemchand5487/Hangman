
#  ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
#  ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
#  ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
#  ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
#  ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
#  ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
#

from random import choice



# Print Hangman on screen
def draw_hangman():
    print("""
        
  ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
  ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
  ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
  ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
  ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
  ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝                                                              
""")


# Draw Stand of hanger
def draw_stand():
    draw_hangman()
    print("\n")
    print("        ____________________")
    for _ in range(21):
        print("        |                    ")
    print("^^^^^^^^^^^^^^^^^")

# Draw rope of hanger
def draw_rope():
        print("\n"*50)
        draw_hangman()
        print("\n")
        print("        ____________________")
        for _ in range(3):
                print("        |                   |")
        for _ in range(19):
                print("        |                    ")
        print("^^^^^^^^^^^^^^^^^")

# Draw head of person
def draw_head():
        print("\n" * 50)
        draw_hangman()
        print("\n")
        print("        ____________________")
        for _ in range(3):
                print("        |                   |")
        print("        |                  ###")
        print("        |                ##   ##")
        print("        |		#	#")
        print("        |		 ##   ##")
        print("        |		   ###")
        for _ in range(14):
                print("        |                    ")
        print("^^^^^^^^^^^^^^^^^")

# Draw Body of person
def draw_body():
        print("\n" * 50)
        draw_hangman()
        print("\n")
        print("        ____________________")
        for _ in range(3):
                print("        |                   |")
        print("        |                  ###")
        print("        |                ##   ##")
        print("        |		#	#")
        print("        |		 ##   ##")
        print("        |		   ###")
        for _ in range(6):
                print("        |		    |")
        for _ in range(8):
                print("        |                    ")
        print("^^^^^^^^^^^^^^^^^")

# Drar hands of person
def draw_hands():
        print("\n" * 50)
        draw_hangman()
        print("\n")
        print("        ____________________")
        for _ in range(3):
                print("        |                   |")
        print("        |                  ###")
        print("        |                ##   ##")
        print("        |		#	#")
        print("        |		 ##   ##")
        print("        |		   ###")
        print("        |		   /|\\")
        print("        |		  / | \\")
        print("        |		 /  |  \\")
        print("        |		/   |   \\")
        print("	|		    |")
        print("	|		    |")
        for _ in range(8):
                print("        |                    ")
        print("^^^^^^^^^^^^^^^^^")

# Draw legs of person
def draw_legs():
        print("\n" * 50)
        draw_hangman()
        print("\n")
        print("        ____________________")
        for _ in range(3):
                print("        |                   |")
        print("        |                  ###")
        print("        |                ##   ##")
        print("        |		#	#")
        print("        |		 ##   ##")
        print("        |		   ###")
        print("        |		   /|\\")
        print("        |		  / | \\")
        print("        |		 /  |  \\")
        print("        |		/   |   \\")
        print("	|		    |")
        print("	|		    |")
        print("	|		   / \\")
        print("	|		  /   \\")
        print("	|		 /     \\")
        print("	|		/       \\")
        for _ in range(3):
                print("        |                    ")
        print("^^^^^^^^^^^^^^^^^")

# Draw Game Over
def draw_gameover():
        print("""
        
   ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
  ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
  ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
  ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
  ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
   ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
                                                                            

        """)

# Draw You Won
def draw_youwon():
        print("\n"*50)
        print("""
        
  ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗ ██████╗ ███╗   ██╗
  ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██╔═══██╗████╗  ██║
   ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║   ██║██╔██╗ ██║
    ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║   ██║██║╚██╗██║
     ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║ ╚████║
     ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝
                                                              

        """)


#   ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗
#  ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
#  ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
#  ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
#  ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
#   ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
#

#  ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗ ██████╗ ███╗   ██╗
#  ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██╔═══██╗████╗  ██║
#   ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║   ██║██╔██╗ ██║
#    ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║   ██║██║╚██╗██║
#     ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║ ╚████║
#     ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝
#

# Random Words
def random_word(seq):
        word1 = choice(seq)
        word1.lower()
        return word1

# Finding indexes of matched element
def get_index(word1, letter1):
        result = []
        for i in range(len(word1)-1):
                if word[i] == letter1:
                        result.append(i)
        return result


# Print Word
def print_word(letters_list):
        word_string = " ".join(letters_list)
        print(word_string)
        print("\n")

# check that the letter entered by user is repeated or not
def check_letter(letter1):
        if letter1 in blanks_list:
                return False
        return True

# set the letter on blanks if it match
def set_letter(letter1, indexes):
        for i in indexes:
                blanks_list[i] = letter1
        print_word(blanks_list)

# taking input from user
def player_input():
        while 1:
                letter1 = input("Guess the letter and press 1 for hint: ")
                letter1.lower()
                if track_hints <= 0:
                        print("Your Hints are over...")
                        continue
                if check_letter(letter1):
                        letters_used.append(letter1)
                        return letter1
                print("Letter is invalid, Try again....")

# Check that player win or not
def win_check(seq):
        if "_" in seq:
                return False
        return True

# check that lives are left or not
def check_lives(count):
        if count == 1:
                draw_rope()
                return True
        if count == 2:
                draw_head()
                return True
        if count == 3:
                draw_body()
                return True
        if count == 4:
                draw_hands()
                return True
        return False


# give hint
def hint():
        while 1:
                letter1 = choice(word)
                if (letter1 in blanks_list) or (letter1 == "\n"):
                        continue
                return letter1


if __name__ == '__main__':
        words = list(open("words.txt", 'r'))
        replay = True
        while replay:
                letters_used = []
                count_lives = 0
                track_hints = 2
                word = random_word(words)
                blanks_list = ["_"] * (len(word)-1)
                while replay:
                        if count_lives == 0:
                                draw_stand()
                                print("You used following letters")
                                print_word(letters_used)
                                print("Word contains {} words and {} hints left".format((len(word)-1), track_hints))
                                print_word(blanks_list)
                        letter = player_input()
                        if letter == '1' and track_hints > 0:
                                letter = hint()
                                track_hints -= 1
                        if letter in word:
                                set_letter(letter, get_index(word, letter))
                                if win_check(blanks_list):
                                        draw_youwon()
                                        replay = False

                        else:
                                count_lives += 1
                                if check_lives(count_lives):
                                        print("You used following letters")
                                        print_word(letters_used)
                                        print("Word contains {} words and {} hints left".format((len(word)-1), track_hints))
                                        print_word(blanks_list)
                                        continue
                                draw_legs()
                                print("The word was {}".format(word))
                                draw_gameover()
                                replay = False
                response = input("Are you want to play again: ")
                response.lower()
                if response[0] == 'y':
                        replay = True

                                
                        

