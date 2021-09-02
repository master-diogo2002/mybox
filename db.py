import sqlite3


class db_operations:

    def __init__(self,user=None,password=None):
        self.user = user
        self.password=password
        self.conn = sqlite3.connect('./db/logins.db')
        self.c = self.conn.cursor()
    
    def verify_user(self):
        try:
            self.c.execute('SELECT * FROM Logins WHERE User=?', (self.user,))
            password=self.c.fetchall()[0][1]


            if password == str(self.password):
                return True
            else:
                return False
            

        except:
            return False #user not existent