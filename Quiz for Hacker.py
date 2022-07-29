
# -----------------------------------------QUIZ TIME--------------------------------------------------------------
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("--------------------------QUIZ TIME---------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORREXT ANSWER!")
        return 1
    else:
        print("WRONG ANSWER!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Score: "+str(score)+"%")

# -------------------------
def play_again():

    response = input("Play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------


questions = {
 "Ethical hacker is also known as ......": "A",
 "The process of professionally or ethically hacking a message is called": "C",
 "What is the maximum length of an SSID?": "A",
 "What is the attack called “evil twin”? ": "C",
 "What does the term 'Ethical Hacking' mean?" : "A",
 "Which tool can be used to perform a DNS zone transfer on Windows?":"B"
}


options = [["a)White hat Hacker", "b)Penetration Tester ", "c)Both white hat hacker & penetration tester ", "d)Black hat hacker"],
          ["a)Cryptography", "b)Encryption", "c)Penetration Testing", "d)Decryption"],
          ["a)32 characters", "b)16 characters", "c)64 characters", "d)8 bcharacters"],
          ["a)MAC spoofing" , "b)Session hijacking", "b)Rogue access point", "d)ARP poisoning"],
          ["a)Someone who is using his/her skills for offensive purposes", "b)Someone who is using his/her skills for ethical reasons" , "c)Someone who is hack for ethical reasons", "d)Someone who is using his/her skills for defensive purposes."],b
          ["a)DNS lookup", "b)nslookup", "c)whois", "d)ipconfig"]]
new_game()

while play_again():
    new_game()

print("GOOdBYES!")

# -------------------------