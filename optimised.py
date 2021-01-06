import mysql.connector

con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)
cursor = con.cursor()
w = input("Enter word: ")
w = w.lower()
query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % w)
results = cursor.fetchall()
if results:
    for result in results:
        print(result[0])

else:
    w = w.title()
    query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % w)
    results = cursor.fetchall()
    if results:
        for result in results:
            print(result[0])
    else:
        w = w.upper()
        query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % w)
        results = cursor.fetchall()
        if results:
            for result in results:
                print(result[0])
        else:
            print("The word doesn't exist.Please double check it.")
