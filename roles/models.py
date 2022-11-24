from django.db import connection

# Create your models here.

class CreateTable():
    def __init__(self):
        with connection.cursor() as cursor:
            query = '''
            CREATE TABLE IF NOT EXISTS `User` (
              `user_id` int(11) NOT NULL auto_increment,
              `first_name` varchar(250) NOT NULL,
              `last_name` varchar(250) NOT NULL,
              `email` varchar(250)  NOT NULL,
              `password`  varchar(100) NOT NULL,
              `role`  varchar(100),
              `airline`  varchar(100),
               PRIMARY KEY  (`user_id`)
            );
            '''
            cursor.execute(query)

    def insert_user(self, f_name, l_name, email, password):
        try:
            query = "insert into User(name, email, password) VALUES(%s, %s, %s)"
            args = (f_name, l_name, email, password)
            with connection.cursor() as cursor:
                cursor.execute(query, args)
            return True
        except:
            return False
        finally:
            cursor.close()

    from django.contrib.auth import login

    def check_login(self, email, password):
        try:
            query = "select * from User where email = %s and password = %s"
            args = (email, password)
            with connection.cursor() as cursor:
                cursor.execute(query, args)
                result = cursor.fetchone()
                return result
        except:
            return False
        finally:
            cursor.close()

    def all_flights(self):
        try:
            query = "select * from flights order by time_at_gate "
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except:
            return False
        finally:
            cursor.close()






