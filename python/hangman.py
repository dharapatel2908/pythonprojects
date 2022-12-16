import random
def hangman():
    word = random.choice(list(["dorm","painter","conference","carriage","publicity","contraction","constituency","fashion","inn","ball","patience","rotation","terrify","cinema","nomination"]))
    validletters = 'abcdefghijklmnopqrstuvwxyz'
    attempt= 10
    guessmade = ''
    while len(word) > 0:
        missed = 0
        main = ""
        for letters in word:
            if letters in guessmade:
                main = main + letters

            else:
                main = main +"_" + ""

        if main == word:
            print(word)
            print("YOU WIN!!") 
            break

        print("Guess the word ",main)
        guess = input() 

        if guess in validletters:
            guessmade = guessmade + guess
        else:
            print("Please enter proper character")
            guess = input()

        if guess not in word:
            attempt = attempt - 1
            if attempt == 9:
                print("9 chances are left")
                print("------")
            if attempt == 8:
                print("8 chances are left")
                print("------")
                print("  O   ")
            if attempt == 7:
                print("7 chances are left")
                print("------")
                print("  O   ")
                print("  |   ")
            if attempt == 6:
                print("6 chances are left")
                print("------")
                print("  O   ")
                print("  |   ")
                print("  |   ")
                
            if attempt == 5:
                print("5 chances are left")
                print("------")
                print("  O   ")
                print("  |   ")
                print("  |   ")
                print(" /    ")
            if attempt == 4:
                print("4 chances are left")
                print("------")
                print("  O   ")
                print("  |   ")
                print("  |   ")
                print(" / \  ")
            if attempt == 3:
                print("3 chances are left")
                print("------")
                print(" \O   ")
                print("  |   ")
                print("  |   ")
                print(" / \  ")
            if attempt == 2:
                print("2 chances are left")
                print("------")
                print(" \O/  ")
                print("  |   ")
                print("  |   ")
                print(" / \  ")
            if attempt == 1:
                print("1 chance are left")
                print("------")
                print(" \O|/ ")
                print("  |   ")
                print("  |   ")
                print(" / \  ")
                print(" Last Chance")
            if attempt == 0:
                print("------")
                print("  O|  ")
                print(" /|\  ")
                print("  |   ")
                print(" / \  ")
                print(" YOU LOSE!!")


name = input("Enter your Name : ")
print("welcome to HangMan Game " + name + "!" )
print("-------------")
print("You have to guess the word within 10 tries.")
x = hangman()
print(x)