"""Python CMD program for counting the vowels of the entered text.
using Python version 3.11.4
@version : 1.0
@license: MIT License
@author : Arman Azarnik
contact me at : armanazarnik@gmail.com
"""


def main():
    """
    main function for interacting with the user
    """

    while(True):
     # while loop to keep the program running

        print("Please enter your text :")
        input_text = input()
        a, e, i, o, u = vowels_counter(input_text)
        print("There are  " 
              +str(a)+ " a,  "
              +str(e)+ " e,  "
              +str(i)+ " i,  "
              +str(o)+ " o,  "
              +str(u)+ " u  in this text.")
        print("**************************")


def vowels_counter(text):
   """
   function for counting number of vowels.
   
   @param text: the input string.
   @type text: string
   @return: a, e, i, o, u for number of each vowel.
   @rtype: int
   """

   a = e = i = o = u = 0
   # initialize variables for vowels

   for char in text.lower():
       match char:
           case 'a':
                a += 1

           case 'e':
                e += 1

           case 'i':
                i += 1 

           case 'o':
                o += 1

           case 'u':
                u += 1

   return a, e, i, o, u


if __name__ == '__main__':
    main()