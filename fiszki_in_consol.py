from setings import *
import mysql.connector
from time import sleep
#======================= bd.connection #=======================

db = mysql.connector.connect(
    host= host,
    user=user,
    passwd=passwd,
    database=database,
)

mycursor = db.cursor()

#=================== Funkcje #===================



def fiszki_game(user_login):
    print("=="*25)
    print("")
    print(f"Z iloma fiszkami chcesz zagrać? Dostępne {count_words(user_login)}")
    print(f"Aby wyjść wciśnij (q)")
    
    while True:
        anser = input("-->")

        if anser == "q":
            user_page(user_login)
            break

        anser = int(anser)
        if anser > count_words(user_login):
            print("Błąd")
            continue
        
        else:
            while True:
                word_pl = random.choice(list(prepare_words(user_login)))
                word_ang = prepare_words(user_login).get(f'{word_pl}')
                
                print(f"Koks zagramy z {anser} fiszkami. Wyjście (q)")
                print(f"Słowo po pl: {word_pl} ")
                while True:
                    anser_word = input("słowo po pol -->")

                    if anser_word == word_ang:
                        print("Doskonale :)")
                        break
                    if anser_word == "q":
                        fiszki_game(user_login)
                        break
                    else:
                        print("Żle")
                        continue





def fiszki_make(user_login):
    print("=="*25)
    print("")

    while True:
        print("Stworzymy fiszki. Aby wyjść (q)")
        slowo_pl = input("Po pol -->")
        if slowo_pl == "q" :
            user_page(user_login)
            break
        slowo_ang = input("Po ang -->")

        

        print(f"Oto chodiz?: {slowo_pl} = {slowo_ang} (Y/N) ")
        anser = input("-->")

        if anser == "Y":
            mycursor.execute (f"INSERT INTO fiszki_{user_login} (po_pol,po_ang) VALUES ('{slowo_pl}','{slowo_ang}')")
            db.commit()
            print("Dodano do bazy")
            continue
        
        if anser == "n" :
            user_page(user_login)
        else:
            pass


    print("")
    print("=="*25)
    


def user_page(user_login):
    print("=="*25)
    print("")
    print(f"Witaj {user_login}")
    print("Stworzyć nowe fiskzi. (1)")
    print("Zagrać w fiszki (2)")
    print("Wyjście (q)")
    while True:
        anser = input("-->")

        if anser == "1":
            fiszki_make(user_login)
        if anser == "2":
            fiszki_game(user_login)
        if anser == "q":
            break
        else:
            continue



    print("")
    print("=="*25)


def registration():
    print("=="*25)
    print("")

    print("***Registration***\n")

    while True:
        user_name = input("Imię: ")
        user_login = input("Login: ")
        email = input("Email: ")

        while True:
            user_password = input("Hasło: ")
            user_password_check = input("Hasło raz jeszcze: ")
            if user_password == user_password_check:
                break
            else:
                print("Źle.")
                continue
        
        
        print("*")
        sleep(0.5)
        print("*")
        sleep(0.5)
        print("*")

        print("Czy wszystko sie zgadza (Y/N) ?")
        print(f"Imię: {user_name}")
        print(f"Login: {user_login}")
        print(f"Hasło: {user_password}")
        print(f"Email: {email}")
        print("")
        
        while True:

            anser = input("-->")

            if anser == "Y":
                mycursor.execute (f"INSERT INTO Users (name,email,nickname,password) VALUES ('{user_name}','{email}','{user_login}','{user_password}')")
                mycursor.execute (f"CREATE TABLE fiszki_{user_login} (po_pol VARCHAR(50), po_ang VARCHAR(50) )")
                db.commit()
                print("***DODANO***")
                login_user()
            if anser == "N":
                registration()
                break  

            else:
                continue











def login_user():
    print("=="*25)
    print("")
    try:
        while True:
            user_login = input("Login: ")
            user_password = input("Hasło: ")
            print("")
            print("=="*25)
            a = select_from_db('password', f'{user_login}')
                    
                
            if a == user_password and user_login == select_from_db('nickname', f'{user_login}'):
                print("zajebiscie")
                user_page(user_login)
                return True
                break
    except:       
        print("Błędny login lub hasło")
        login_user()
            





def introducing():
    print("=="*25)
    print("Hejka naklejka, jest to prosty program z fiszkami :)")
    print("Nie masz konta ? Zalejestruj się. (1)")
    print("Zaloguj. (2)")
    print("=="*25)

    while True:
        anser = input("-->")

        if anser == "1":
            registration()
            break
        elif anser == "2":
            login_user()
            break

        else:
            print("Raz jeszcze.")
            continue


def main_loop():
    
    login_user()
        







main_loop()




#=================== Main loop #===================