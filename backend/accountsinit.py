import dbfunctions

def accountinit(conn):
    tables = {
        "accounts" : (
                None,
                "AccountsDB",
                "CREATE TABLE IF NOT EXISTS AccountsDB(AccountID INTEGER PRIMARY KEY unique not null, Username TEXT unique not null, HashPassword TEXT unique not null, Salt TEXT not null)",
                ),
        "logins" : (
                None,
                "LoginsDB",
                "CREATE TABLE IF NOT EXISTS LoginsDB(LoginID INTEGER PRIMARY KEY unique not null, AccountID INTEGER not null)"
            ),
        "userRatings": (
                None,
                "UserRatingsDB",
                "CREATE TABLE IF NOT EXISTS UserRatingsDB(RatingID INTEGER PRIMARY KEY unique not null, AccountID INTEGER not null, TitleID TEXT not null, Rating REAL not null, Review TEXT)"
            )
        }
    try:
        for key in tables:
            print("passing:", *tables[key])
            dbfunctions.createTable(conn, *tables[key])
    except Exception as e:
        print(e)

conn = dbfunctions.dbConnect()
accountinit(conn)
dbfunctions.dbClose(conn)