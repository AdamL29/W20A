import mariadb
import dbcreds

def connect_db():
    try:
        conn = mariadb.connect(
            user=dbcreds.user, 
            password=dbcreds.password, 
            host=dbcreds.host, 
            port=dbcreds.port, 
            database=dbcreds.database, 
            autocommit=True)
        cursor = conn.cursor()
        return cursor
    except mariadb.OperationalError as error:
        print("OPERATIONAL ERROR:", error)
    except Exception as error:
        print("UNEXPECTED ERROR:", error)

def disconnect_db(cursor):
    try:
        conn = cursor.connection
        cursor.close()
        conn.close()    
    except mariadb.OperationalError as error:
        print("OPERATIONAL ERROR:", error)
    except mariadb.InternalError as e:
        print("INTERNAL ERROR: ", e)
    except Exception as error:
        print("UNEXPECTED ERROR:", error)

def execute_statement(cursor, statement, args=[]):
    try:
        cursor.execute(statement, args)
        results = cursor.fetchall()
        return results
    except mariadb.ProgrammingError as e:
        print("Syntax error in your SQL statement: ", e)
        return str(e)
    except mariadb.IntegrityError as e:
        print("The statement failed to execute due to integrity error: ", e)
        return str(e)
    except mariadb.DataError as e:
        print("DATA ERROR: ", e)
        return str(e)
    except Exception as e:
        print("Unexpected error: ", e)
        return str(e)

def run_statement(statement, args=[]):
    cursor = connect_db()
    if (cursor == None):
        return "Connection Error!"
    results = execute_statement(cursor, statement, args)
    disconnect_db(cursor)
    return results