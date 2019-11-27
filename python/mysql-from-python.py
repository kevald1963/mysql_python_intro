import os
import datetime
import pymysql

# Get username from Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
   
    """ Run a query. """
    #with connection.cursor(pymysql.cursors.DictCursor) as cursor:
    #    sql = "select * from Genre;"
    #    cursor.execute(sql)
    #    for row in cursor:
    #        print(row)

    """ Create a table. """
    #with connection.cursor(pymysql.cursors.DictCursor) as cursor:
    #    cursor.execute("""create table if not exists
    #                      Friends(name char(20),
    #                              age int,
    #                              DOB datetime);
    #                   """)

    """ Insert a single row. """
    #with connection.cursor() as cursor:
    #    row = ("Jim", 55, "1964-03-11 02:19:00")
    #    cursor.execute("""insert into Friends
    #                      values(%s, %s, %s);""", row)
    #    connection.commit()

    """ Insert many rows using a list of tuples and 'executemany' method of cursor. """
    #with connection.cursor() as cursor:
    #    row = [("Jim", 19, "2000-05-07 12:41:00"),
    #           ("Bill", 15, "2015-04-29 02:39:56"),
    #           ("Ben", 20, "1999-04-29 02:39:56"),
    #           ("Anita", 26, "1993-12-14 12:14:23"),
    #           ("Samantha", 29, "2080-05-17 12:41:00")]
    #    cursor.executemany("""insert into Friends
    #                      values(%s, %s, %s);""", row)
    #    connection.commit()

    """ Simple update. """
    #with connection.cursor() as cursor:
    #    cursor.execute("""update Friends
    #                      set age = 22, DOB = "1997-12-14 12:14:23"
    #                      where name = "Anita";""")
    #    connection.commit()

    """ Update using string interpolation."""
    #with connection.cursor() as cursor:
    #    cursor.execute("""update Friends set age = %s, name = %s, DOB = %s
    #                      where name = %s;""",
    #                      (17, "Will", "2002-12-14 12:14:23", "William"))  # << N.B. This part is outside the SQL statement.
    #    connection.commit()

    """ Update many rows a list of tuples and 'execute many' method of cursor."""
    #with connection.cursor() as cursor:
    #    row = [("54", "Sam"),
    #           ("53", "Will")]
    #    cursor.executemany("""update Friends set age = %s
    #                      where name = %s;""",
    #                      row)
    #    connection.commit()

    """ Simple delete, single rows (not best practice). """
    #with connection.cursor() as cursor:
    #    cursor.execute("delete from Friends where name = 'Jim';")
    #    connection.commit()

    """ Simple delete many rows with IN clause #1 (not best practice). """
    #with connection.cursor() as cursor:
    #    cursor.execute("delete from Friends where name in ('Jim', 'Ben');")
    #    connection.commit()

    """ Delete many with IN clause and string interpolation #1 (not best practice). """
    #with connection.cursor() as cursor:
    #    names = ['Kim', 'Bill']        
    #    cursor.execute("delete from Friends where name in (%s, %s);", names)
    #    connection.commit()

    """ Delete many (BEST PRACTICE). Note does not use 'executemany' i.e. multiple SQL statements
        that delete single rows but one single statement that deletes many rows.
    """
    with connection.cursor() as cursor:
        list_of_names = ['Anita', 'Kevin']        
        # Prepare a string with the same number of placeholders as per the list of names.
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("delete from Friends where name in ({});".format(format_strings), list_of_names)
        connection.commit()

finally:
    # Close the connection, whether or not successful.
    connection.close()
