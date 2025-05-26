import sqlite3

# Connection to the database whcih check access to the file. It creates the file if it doesn't exist
conn = sqlite3.connect('emaildb.sqlite')
# Handle. You open it, send SQL commands through the cursor and get your responses through the cursor
cur = conn.cursor()

# If the table Counts already exists, it drops it
cur.execute('DROP TABLE IF EXISTS Counts')

#Creates the table Counts with 2 columns 
cur.execute('''
            CREATE TABLE Counts (email TEXT, count INTEGER)''')


fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox-short-2.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From '):
        continue
    pieces = line.split()
    email = pieces[1]
    # Select count from our db where email is equal to the email. The '?' is a placeholder for what goes into the variable email
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
    row = cur.fetchone()
    # It goes through the rows and if it doesn't find a match for the email, it creates a record for that email with a count 1
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                    VALUES (?, 1)''', (email,))
    #If the row exists, we just add one to the number
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()