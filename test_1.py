from setings import *
import mysql.connector

from test_0 import fiszki_make

#======================= bd.connection #=======================

db = mysql.connector.connect(
    host= host,
    user=user,
    passwd=passwd,
    database=database,
)

mycursor = db.cursor()


def fiszki_game(user_name,user_nick):
    print("Dobra to tera zagramy w te fiszki")
    print("Z iloma słuówkami sie zabawimy?")
    anser = input("-->")

    slowka_pl = []
    slowkapl_list=[]

    slowka_ang = []
    slowkaang_list = []
    mycursor.execute(f"SELECT po_pol FROM fiszki_{user_name}")

    for x in mycursor:
            pass_list.append(x)

            value= list(f"{pass_list[0]}")

            del value[0:2]
            del value[-3:]
            user_name = "".join(value)




def make_fiszki(user_name,user_nick):
    print("=="*10)
    print("Dobra pora zrobić fiszki !!! jezeli chcesz skończyć wciśnij q")
    make_fiszki_status = True
    while make_fiszki_status:

        print("Słowo po polsku")
        anser_pl = input("-->")
        print("Słowo po angielsku")
        anser_ang = input("-->")
        print("**"*5)
        print(f"Czy tak to ma być ? {anser_pl} = {anser_ang} ? (y/n)")

        anser = input("-->")

        if anser == "y":
        
            mycursor.execute (f"INSERT INTO fiszki_{user_name} (po_pol,po_ang) VALUES ('{anser_pl}','{anser_ang}')")
            db.commit()
            print("Dodano do bazy")
            continue

        if anser == "n":
            continue
        if anser == "q":
            user_page(user_name,user_nick)

        else:
            print("zła odp ")
       
            






def user_page(user_name,user_nick):
    print("=="*10)
    print(f"Siemano {user_nick}")
    user_page_status = True
    while user_page_status:
        print("Co chcesz zrobić??")
        print("Stworzyć nowe fiszki ? (1)")
        print("Albooo, popracować z już zrobionymi :) (2)")
        anser = input("-->")

        if anser == "1":
            make_fiszki(user_name,user_nick)

        elif anser == "2":
            fiszki_game(user_name,user_nick)

        else:
            print("zła odp")







def registration():
    rejestration = True
    while rejestration:

        print("Siemano, przyszła pora na rejestrowanko")
        print("=="*10)
        user_name = input("podaj imię: ")
        user_nickname = input("podaj nickane: ")
        user_passwd = input("podaj  hasło: ")
        user_email  = input("podaj  emial: ")
        print("=="*10)

        print("czy następujące dane są prawidłowe? (Y/N)")
        print(f"imie: {user_name}")
        print(f"nickane: {user_nickname}")
        print(f"haslo: {user_passwd}")
        print(f"email: {user_email}")

        anser_status = True
        while anser_status:
            anser = input("---> ")
            anser.lower

            if anser == "y":
                
                mycursor.execute ("INSERT INTO Users (name,email,nickname,password) VALUES (%s,%s,%s,%s)",(f"{user_name}",f"{user_email}",f"{user_nickname}",f"{user_passwd}"))
                mycursor.execute (f"CREATE TABLE fiszki_{user_name} (po_pol VARCHAR(50), po_ang VARCHAR(50) )")
                db.commit()
                print("****DODANO****")
                anser_status= False
                rejestration = False
                login()

            if anser== "n":
                
                anser_status=False
            else:
                print("zła odpowiedz (Y/N)")











def login():
    print("Siemano, przyszła pora na logowanko")
    print("=="*10)
    login_status = True
    while login_status:

        user_nick = input("podaj login: ")
        user_passwd = input("podaj  hasło: ")

        try:
            login_list = []
            pass_list = []

            mycursor.execute(f"SELECT nickname FROM Users WHERE nickname = '{user_nick}' ")

            for x in mycursor:
                login_list.append(x)

            value= list(f"{login_list[0]}")

            del value[0:2]
            del value[-3:]
            login_ok = "".join(value)


            mycursor.execute(f"SELECT password FROM Users WHERE nickname = '{user_nick}' ")

            for x in mycursor:
                pass_list.append(x)

            value= list(f"{pass_list[0]}")

            del value[0:2]
            del value[-3:]
            passwd_ok = "".join(value)

            mycursor.execute(f"SELECT name FROM Users WHERE nickname = '{user_nick}' ")

            for x in mycursor:
                pass_list.append(x)

            value= list(f"{pass_list[0]}")

            del value[0:2]
            del value[-3:]
            user_name = "".join(value)

        
            if user_nick == login_ok and user_passwd == passwd_ok:
                user_page(user_name,user_nick)
                login_status = False
                
        except:
                print("złe passy :/")



def introducing():


    print("Hejka naklejka, jest to prosty program z fiszkami :)")
    print("Jeżeli masz już konto możesz sie zalogować wybierając (1) ")
    print("jeżeli nie możesz sie zalogować wybierając (2)")

    anser = input()

    if anser == "2":
        registration()
    if anser == "1":
        login()
    else:
        print("spróbuj raz jeszcze ")
        introducing()


def main_game():


    fiszki_make('tomek','twojastara')






main_game()