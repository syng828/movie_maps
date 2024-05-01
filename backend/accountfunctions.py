import dbfunctions
import os
import hashlib

def createAccount(conn, username, password):
    salt = generate_salt()
    hashed_password = encrypt(password, salt)
    command = "INSERT INTO AccountsDB(Username, HashPassword, Salt) VALUES ('"+username+"', '"+hashed_password+"', '"+salt+"');"

    return dbfunctions.SQLConn(conn, "television.db", command)

def searchAccountID(conn, username):
    command = "SELECT AccountID FROM AccountsDB WHERE Username = '"+username+"';"

    return dbfunctions.SQLConn(conn, "television.db", command)

def verifyLogin(conn, username, password):
    command = "SELECT HashPassword, Salt FROM AccountsDB WHERE Username = '"+username+"';"
    result = dbfunctions.SQLConn(conn, "television.db", command)

    if(result is not None):
        database_password = result[0][0]
        salt = result[0][1]
        hashed_password = encrypt(password, salt) #add in the salt from the database to compare
        
        if database_password == hashed_password:
            return True
    return False

def getUserReviews(conn, accountID):
    command = "SELECT Rating, Review FROM UserRatingsDB WHERE AccountID = '"+accountID+"';"
    
    return(dbfunctions.SQLConn(conn, "television.db", command))

def createReviews(conn, titleID, accountID, rating, review):
    command = "INSERT INTO UserRatingsDB(TitleID, AccountID, Rating, Review) VALUES ('"+titleID+"', '"+accountID+"', '"+rating+"', '"+review+"');"
    return(dbfunctions.SQLConn(conn, "television.db", command))

def fetchReviews(conn, titleID):
    command = "SELECT Username, Rating, Review FROM UserRatingsDB u INNER JOIN AccountsDB a ON u.AccountID = a.AccountID WHERE TitleID = '" + titleID + "';"
    return dbfunctions.SQLConn(conn, "television.db", command)

def generate_salt():
    return os.urandom(16).hex()

def encrypt(password, salt):
    salted_password = password + salt
    hash_object = hashlib.sha256()
    hash_object.update(salted_password.encode())

    return hash_object.hexdigest()



#test
conn = dbfunctions.dbConnect()
#account creation

createAccount(conn, "User", "Pass")
print(verifyLogin(conn, "User", "Pass"))


userID = searchAccountID(conn, "User")

#reviews
createReviews(conn, "tt0002591", str(userID[0][0]), str(10), "slaps") 
print(getUserReviews(conn, str(userID[0][0])))
print(fetchReviews(conn, "tt0002591"))
