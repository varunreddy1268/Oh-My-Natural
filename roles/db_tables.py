from django.db import connection


# Create your models here.


class CreateTable:
    def __init__(self):
        with connection.cursor() as cursor:
            query = '''
            CREATE TABLE IF NOT EXISTS `User` (
              `user_id` int(11) NOT NULL auto_increment,
              `f_name` varchar(250) NOT NULL,
              `l_name` varchar(250) NOT NULL,
              `email` varchar(250)  NOT NULL,
              `password`  varchar(100) NOT NULL,
              `role`  varchar(100) NULL,
              `airline`  varchar(100) NULL,
               PRIMARY KEY  (`user_id`)
            );
            '''
            cursor.execute(query)

            query = '''
                        CREATE TABLE IF NOT EXISTS `flights` (
                          `flight_id` int(11) NOT NULL auto_increment,
                          `aircraft_id` int,
                          `company_airline` varchar(250) NOT NULL,
                          `type_of_flight` varchar(250) NOT NULL,
                          `terminal` varchar(250) NOT NULL,
                          `time_at_gate` Timestamp NOT NULL,
                          `destination` varchar(250) NOT NULL,
                          `duration` varchar(250) NOT NULL,
                           PRIMARY KEY  (`flight_id`)
                        );
                        '''
            cursor.execute(query)


def insert_user(f_name, l_name, email, password):
    try:
        query = "insert into User(f_name, l_name, email, password) VALUES (%s, %s, %s, %s)"
        args = (f_name, l_name, email, password)
        with connection.cursor() as cursor:
            cursor.execute(query, args)
            return True
    except Exception as e:
        print(e)
        return False
    finally:
        cursor.close()


def check_login(email, password):
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


def all_flights_in_db(airline):
    try:
        if not airline:
            query = "select * from flights where time_at_gate > current_timestamp order by time_at_gate desc"
        else:
            query = "select * from flights where time_at_gate > current_timestamp and airline = %s order by time_at_gate desc"
        with connection.cursor() as cursor:
            args = (airline)
            cursor.execute(query, args)
            result = cursor.fetchall()

            return result
    except:
        return False
    finally:
        cursor.close()


def update_flight_time(id, time):
    try:
        query = "update flights set time_at_gate = %s where flight_id = %s"
        args = (time, id)
        with connection.cursor() as cursor:
            cursor.execute(query, args)
            return True
    except:
        return False
    finally:
        cursor.close()
