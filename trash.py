from setings import *
import mysql.connector
from time import sleep
import random
#======================= bd.connection #=======================

db = mysql.connector.connect(
    host= host,
    user=user,
    passwd=passwd,
    database=database,
)

mycursor = db.cursor()

slowo_pl = "kurwa"
slowo_ang = "fuk"

def add_to_db(user_db,slowo_pl,slowo_ang ):
    login_list = []
    mycursor.execute(f"INSERT INTO fiszki_{user_db} (po_pol, po_ang) ")

    for x in mycursor:
        login_list.append(x)

    value= list(f"{login_list[0]}")

    del value[0:2]
    del value[-3:]
    login_ok = "".join(value)
    login_ok = str(login_ok)

    return login_ok

def count_words(user_login):
    word_list = []
    mycursor.execute(f"SELECT po_pol FROM fiszki_{user_login}")

    for x in mycursor:
        word_list.append(x)


    return len(word_list)



def prepare_words(user_login):

    words_list_pl = []
    words_list_ok_pl = []
    mycursor.execute(f"SELECT po_pol FROM fiszki_{user_login} ")

    for x in mycursor:
        words_list_pl.append(x)
    for i in range(0,len(words_list_pl)):
        value= list(f"{words_list_pl[i]}")

        del value[0:2]
        del value[-3:]
        login_ok = "".join(value)
        login_ok = str(login_ok)
        words_list_ok_pl.append(login_ok)

    words_list_ang = []
    words_list_ok_ang = []

    mycursor.execute(f"SELECT po_ang FROM fiszki_{user_login} ")

    for x in mycursor:
        words_list_ang.append(x)
    for i in range(0,len(words_list_ang)):
        value= list(f"{words_list_ang[i]}")

        del value[0:2]
        del value[-3:]
        login_ok = "".join(value)
        login_ok = str(login_ok)
        print(login_ok)
        words_list_ok_ang.append(login_ok)

    words_dict = dict(zip(words_list_ok_pl,words_list_ok_ang))

    
    return words_dict 
    


