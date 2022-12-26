import time
import pyttsx3

engine = pyttsx3.init()  # Initialize the text-to-speech engine

def speak_and_print(text):
  print(text)
  engine.say(text)
  engine.runAndWait()



speak_and_print("Hey Dear! Please Write Your Name ")
User_name = input(":")

speak_and_print(f"Hey {User_name} Welcome to KBC \nBest of Luck !")
User_Account_Bal = 0

Questions_list = ["Q.1 who is the president of India ? ",
                  "Q.2 who is the pm of India ? ",
                  "Q.3  The red sandalwood or red sanders trees, shown in the film “Pusha: The Rise”, are endemic to which region of India ?",
                  "Q.4  What name has been given to the 216-feet statue of Sri Ramanujacharya, unveiled in Hyderabad in February 2022 ? ",
                  ]
Option_list = [
    "\n(a). Droupadi Murmu \n(b). Mhatma Gandi \n(c). Sardar bhagat Singh \n(d). Narendar Modi" ,
               "\n(a). Droupadi Murmu \n(b). Mhatma Gandi \n(c). Sardar bhagat Singh \n(d). Narendar Modi",
               "\n(a). Western Ghats \n(b). Eastern Ghats \n(c). Sundarbans \n(d). Doaba",
               "\n(a). Statue of Unity \n(b). Statue of Freedom \n(c). Statue of Fraternity \n(d). Statue of Equality",
]
Answer_list = ['a','d','b','d']
Price_list = [2000,3000,5000,60000]
for i in range(len(Questions_list)):
    try:
        speak_and_print(Questions_list[i])
        speak_and_print(Option_list[i])

        speak_and_print("Choose Any one of these : a,b,c,d ")
        User_Answer = input(":")
        speak_and_print("We are Checking your Answer...........")
        time.sleep(3)
        if User_Answer == Answer_list[i]:
            speak_and_print(f"Congratulations you win  {Price_list[i]} rupees !! ")
            User_Account_Bal = User_Account_Bal + Price_list[i]

        else:
            speak_and_print(f"you Lose {Price_list[i]} rupees ")

            User_Account_Bal = User_Account_Bal - Price_list[i]

        speak_and_print(f"The Next Round is for {Price_list[i+1]} Rupees ,Would you like to play for the next round?  ")
        User_Play_again = input("press [y/n]  \n:")
        if User_Play_again == "y":
            continue
        else:

            speak_and_print(f"Your Total Amount  is : {User_Account_Bal}")

            speak_and_print(f"Thank you {User_name} For Playig KBC")
            break

    except IndexError:
         speak_and_print(f"Your Total Amount  is : {User_Account_Bal}")

         speak_and_print(f"Thank you {User_name} For Playig KBC")
         break




