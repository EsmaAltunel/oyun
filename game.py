import random

word_list = ["atkı","bere","cam","çicek","dünya","etek","fare","göl","hal","ırak","ilaç","jandarma","kalem","limon","mor","nal","okul","öğretmen","pırasa","rakun","saat","şal","toprak","uçak","ülke","vadi","yağmur","zencefil"]

print("Welcome to the word game \n Write '8' to begin game")
command = input("Command:")



if command == '8':
    first_word = random.choice(word_list)
    print("Your first word : {}".format(first_word))
    your_word = input("Write a new word: ")
    if your_word.endswith("ğ"):
        print("There is no word startswith 'ğ'\nGAME OVER!")
        quit()

    if your_word[0] == first_word[-1]:
     while True:
      for word in word_list:
            if word.startswith(your_word[-1]):
                  print(word)
                  your_word = input("Write a new word: ")
                  if your_word.endswith("ğ"):
                      print("There is no word startswith 'ğ'\nGAME OVER!")
                      quit()
                  if your_word[0] != word[-1]:
                      print("WRONG WORD!!\nGAME OVER!")
                      quit()

    else:
         print("GAME OVER!")
      
      


        
        

 
    
