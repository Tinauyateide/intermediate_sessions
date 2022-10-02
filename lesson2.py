# # Create a function, that repeats the first 2 letters of a word which will be followed by 3 dots and a space after. The string should be ended with a question mark.

# def stutter(word):
#     return word[0:2]+ "..." + word[0:2] + "..." + word + " ?"

# print(stutter("Morning"))

# # Perform a for loop that searches through a string and prints only distinct vowel letters.
# words = input('Enter your sentence: ' )
# vowels = 'aeiouAEIOU'
# for letter in words:
#     if letter in vowels:
#         print(letter)

# Perform a while loop that requests for a name, if that name is entered, it will be printed else, if user types “end” (this command should be case insensitive), the while loop is terminated
# name = input("Please enter Your Name: ")
# while name != "end":
#     print(name)


def name():
    txt = input(" please enter your name: ").lower()
    while txt != "end":
        return txt
    else:
        pass

print(name())

  


        
