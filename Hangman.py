# Simple Hangman game with python
# Author: Roxana Haghgoo


import random

HANGMANPICS = ['''

   +---+

   |   |

       |

       |

       |

       |
=========''', '''

   +---+

   |   |

   O   |

       |

       |

       |
=========''', '''

   +---+

   |   |

   O   |

   |   |

       |

       |
=========''', '''

   +---+

   |   |

   O   |

  /|   |

       |

       |
=========''', '''

   +---+

   |   |

   O   |

  /|\  |

       |

       |
=========''', '''

   +---+

   |   |

   O   |

  /|\  |

  /    |

       |
=========''', '''
   +---+

   |   |

   O   |

  /|\  |

  / \  |

       |
=========''']


# Hangman 
print("---------------------------------------------------------------------------------------------")
print("Welcome to Hangman game!\nTry to guess the word Before the man will be hanged!!!.\n")

# Categories
animals = ['dog','cat','lion','bear','horse','tiger','goat','elephant','cow','wolf','camel','sheep','monkey','rabbit']
citis = ['london','paris','newyork','berlin','amsterdam','tehran','toronto','barcelona','istanbul','moscow']
objects = ['house','table','shoes','carpet','television','desk','chair','phone']
fruits = ['apple','banana','orange','cucumber','cherry','grape','peach','strawberry']
color = ['blue','orange','purple','yellow','green','brown','black','white']

# choose a category

print("categpries :\n1.Animals \n2.Citis \n3.Objects \n4.Fruits \n5.color")
run = True
while run:
    c = input("choose a category : ")
    try:
        c = int(c)
        if c >= 1 and c <= 5:
            run = False
        else:  
            print("\n> please type a number in range! \n")
    except:   
        print("\n> please type a number! \n") 

if c == 1:
    word = random.choice(animals)
elif c == 2 :
    word = random.choice(citis)
elif c == 3 :
    word = random.choice(objects)
elif c == 4 :
    word = random.choice(fruits)
elif c == 5 :
    word = random.choice(color)


message = ''
correctLetters = []
missedLetters = []
pic = 0
blanks = "_  " * len(word)
print("\n>>> Let's begin:")


while len(missedLetters) < 6:
    print(message)
    print(HANGMANPICS[pic]+'\n')
    print(blanks)
    print(" ".join(missedLetters) + "\n")
    guess = input("\n>>> Guess a letter : ")
    if len(guess) != 1 :
        message = '\n> Please enter a single letter.'

    elif guess in (correctLetters or missedLetters) :
        message = '\n> You have already guessed that letter. Choose again.'

    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
        message = '\n> Please enter a LETTER.'

    elif guess in word :
        correctLetters.append(guess)
        for i in range(len(word)):
            if word[i] in correctLetters :
                split = blanks.split()
                split[i] = word[i]
                blanks =" ".join(split)
                c = blanks.replace(" ","")
        if c == word :
            word = word.upper()
            print(f'\n\n>>> yes "{word}", You nailed it !!\n\n')
            break
        message = "\n> Right! Keep Going..."
       
                
    elif guess not in word :
        missedLetters.append(guess) 
        message = "\n> opps!...."
        pic +=1
     
        
if pic == 6 :
    print("\n\nGAME OVER !")
    print(HANGMANPICS[-1])
    
