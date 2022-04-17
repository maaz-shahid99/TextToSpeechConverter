from gtts import gTTS
import os

choice = -1

while(True):
    
    print("Press 1 for Hindi \nPress 2 for Bengali \nPress 0 for Exit")
    choice = int(input())

    if(choice == 0):
        print("Program Ended")
        break
    
    if(choice == 1):
        input_text = input()

        language = 'hi'

        output = gTTS(text = input_text, lang = language, slow = False)
        
        output.save("hindi.mp3")

        os.system("start hindi.mp3")

    if(choice == 2):
        input_text = input()

        language = 'bn'

        output = gTTS(text = input_text, lang = language, slow = False)
        
        output.save("hindi.mp3")

        os.system("start hindi.mp3")