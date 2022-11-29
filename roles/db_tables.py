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
              `role`  varchar(100) default null,
              `airline`  varchar(100) default null,
               PRIMARY KEY  (`user_id`)
            );
            '''
            cursor.execute(query)

            query = '''
                        CREATE TABLE IF NOT EXISTS `flights` (
                          `flight_id` int(11) NOT NULL auto_increment,
                          `aircraft_id` int,
                          `company_airline` varchar(250) default null,
                          `type_of_flight` varchar(250) default null,
                          `terminal` varchar(250) default null,
                          `time_at_gate` Timestamp NOT NULL,
                          `destination` varchar(250) default null,
                          `duration` varchar(250) default null,
                           PRIMARY KEY  (`flight_id`)
                        );
                        '''
            cursor.execute(query)

            query = '''
                    CREATE TABLE IF NOT EXISTS `gates` (
                      `gate_id` int(11) NOT NULL auto_increment,
                      `gate_number` varchar(32),
                      `status` int(1) default 0,
                      `terminal_number` varchar(250) NOT NULL,
                       PRIMARY KEY  (`gate_id`)
                    );
                    '''
            cursor.execute(query)
            query = '''
                        CREATE TABLE IF NOT EXISTS `flights_gates` (
                          `gate_id` int(11) NOT NULL,
                          `flight_id` int(11) Not Null,
                          `daparture_time` Timestamp default null
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
            query = '''select f.*, g2.gate_number from flights f
                        left join flights_gates g on g.flight_id = f.flight_id
                        left join gates g2 on g.gate_id = g2.gate_id
                         where time_at_gate > current_timestamp order by time_at_gate desc'''
        else:
            query = '''select f.*, g2.gate_number from flights f
                        left join flights_gates g on g.flight_id = f.flight_id
                        left join gates g2 on g.gate_id = g2.gate_id
                        where time_at_gate > current_timestamp and company_airline = %s order by time_at_gate desc'''
        with connection.cursor() as cursor:
            cursor.execute(query, (airline,)) if airline else cursor.execute(query)
            result = cursor.fetchall()
            return result
    except:
        return None
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


def get_all_gates_information():
    try:
        query = "select fg.flight_id, g.gate_number from flights_gates fg join gates g on g.gate_id = fg.gate_id"
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
    except:
        return False
    finally:
        cursor.close()


def is_already_exist(email):
    try:
        query = "select * from User where email = %s"
        args = (email,)
        with connection.cursor() as cursor:
            cursor.execute(query, args)
            result = cursor.fetchall()
            return result
    except:
        return False
    finally:
        cursor.close()


def setup_gates():
    try:
        query = "select gate_id, gate_number from gates where status = 0 order by gate_number"
        # args = (email,)
        with connection.cursor() as cursor:
            cursor.execute(query)
            gates_result = cursor.fetchall()
            query = '''select f.flight_id from flights f
              left join flights_gates fg on fg.flight_id = f.flight_id
              where f.time_at_gate > current_timestamp and fg.flight_id is
                  null order by f.time_at_gate'''
            cursor.execute(query)
            flights_result = cursor.fetchall()

            return gates_result, flights_result
    except:
        return False
    finally:
        cursor.close()


def insert_flights_gates(gates_id, flight_id):
    try:
        query = "insert into flights_gates(gate_id, flight_id) VALUES (%s, %s)"
        args = (gates_id, flight_id)
        with connection.cursor() as cursor:
            cursor.execute(query, args)
            query = "update gates set status=1 where gate_id=%s"
            args = (gates_id,)
            cursor.execute(query, args)
            return True
    except Exception as e:
        print(e)
        return False
    finally:
        cursor.close()


def free_gate():
    try:
        query = '''update gates g
    join flights_gates fg on g.gate_id = fg.gate_id
    join flights f on fg.flight_id = f.flight_id
    set g.status=0
    where f.time_at_gate <= current_timestamp '''
        # args = (email,)
        with connection.cursor() as cursor:
            cursor.execute(query)
            query = '''delete fg from
                flights_gates fg join flights f on fg.flight_id = f.flight_id
                where f.time_at_gate <= current_timestamp '''
            cursor.execute(query)
            return True
    except:
        return False
    finally:
        cursor.close()
