import psycopg2
from Dbconnect import Databaseconnection

class Create_tables:

    
    def create_table_Users(self):
        
        """ create tables in the PostgreSQL database"""
        sqlcommand = """

            CREATE TABLE users (
                                User_id SERIAL PRIMARY KEY,
                                F_Name varchar(10) not null unique,
                                L_Name varchar(10) not null unique,
                                Age smallint not null unique,
                                Email text not null unique,
                                Password text not null unique,
                                Created_at DATE not null
                                )
            """
        
        
        try:
            db = Databaseconnection()
            db.cursor.execute(sqlcommand)
        
            db.cursor.close()
            
            dbcommit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if db is not None:
                db.cursor.close()



    def create_table_Categories(self):


        sqlcommand =   """ CREATE TABLE Categories (
                categories_id SERIAL PRIMARY KEY,
                task_id integer not null,
                categories_name VARCHAR(20) NOT NULL,
                title text not null,
                description text not null,
                created_at DATE not null,
                FOREIGN KEY (task_id)
                REFERENCES Tasks (task_id)
                ON UPDATE CASCADE ON DELETE CASCADE
                )
        """
   
        
        try:
            db = Databaseconnection()
            db.cursor.execute(sqlcommand)
        
            db.cursor.close()
            
            db.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if db is not None:
                db.cursor.close()



    def create_table_Tasks(self):

         
        sqlcommand =     """
            CREATE TABLE Tasks (
                        task_id serial PRIMARY KEY,
                        user_id integer NOT NULL,
                        title text NOT NULL,
                        description text not null,
                        created_at DATE,
                        FOREIGN KEY (user_id)
                        REFERENCES Users (user_id)
                        ON UPDATE CASCADE ON DELETE CASCADE
                )
                """
            
        try:
            db = Databaseconnection()
            db.cursor.execute(sqlcommand)
        
            db.cursor.close()
            
            db.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if db is not None:
                db.cursor.close()

    
    def Add_users(self):
        db = Databaseconnection()
        sql_stament = """insert into users (F_Name,L_Name,Age,Email,Password,Created_at)
        values('OChom','Zaac',12,'f1ghjjk@mail.com','r4rhgfd',current_timestamp);"""
        db.cursor.execute(sql_stament)
        users = db.cursor.fetchall()
        return users

    def Add_task(self):
        db = Databaseconnection()
        sql_stament = """insert into Tasks (title,description,created_at)values('Ochom_Andela','Isaac work done',current_timestamp);"""
        db.cursor.execute(sql_stament)
        users = db.cursor.fetchall()
        return users

    def Add_Catagories(self):
        db = Databaseconnection()
        sql_stament = """insert into Categories (category_name,title,description,created_at)values('Leve up','DBMS','Postgress python DBMS',current_timestamp);"""
        db.cursor.execute(sql_stament)
        users = db.cursor.fetchall()
        return users

    def select_user(self):
        db = Databaseconnection()
        sql_stament = """select * from users """
        #sql_stament = """insert into Andela (name,age,gender,broke)values('{}','{}','{}','{}');"""
        db.cursor.execute(sql_stament)
        users = db.cursor.fetchall()
        return users

    def select_task(self):
        db = Databaseconnection()
        sql_stament = """select * from tasks """
        #sql_stament = """insert into Andela (name,age,gender,broke)values('{}','{}','{}','{}');"""
        db.cursor.execute(sql_stament)
        users = db.cursor.fetchall()
        return users

    def select_categories(self):
        db = Databaseconnection()
        sql_stament = """select * from Categories """
        #sql_stament = """insert into Andela (name,age,gender,broke)values('{}','{}','{}','{}');"""
        db.cursor.execute(sql_stament)
        users = db.cursor.fetchall()
        return users

    def Update_user(self):
        db = Databaseconnection()
        sql_stament = """ UPDATE vendors
                SET vendor_name = %s
                WHERE vendor_id = %s"""
        #sql_stament = """insert into Andela (name,age,gender,broke)values('{}','{}','{}','{}');"""
        db.cursor.execute(sql_stament)
        users = db.cursor.fetchall()
        return users

    def Update_task(self):
        db = Databaseconnection()
        sql_stament = """ UPDATE Tasks
                SET title = %s,description = %s
                WHERE task_id = %s"""
        #sql_stament = """insert into Andela (name,age,gender,broke)values('{}','{}','{}','{}');"""
        db.cursor.execute(sql_stament)
        users = db.cursor.fetchall()
        return users 


    def Update_Categories(self):
        db = Databaseconnection()
        sql_stament = """ UPDATE Categories
                SET categories_name = %s ,title = %s,description = %s
                WHERE categories_id = %s"""
        #sql_stament = """insert into Andela (name,age,gender,broke)values('{}','{}','{}','{}');"""
        db.cursor.execute(sql_stament)
        users = db.cursor.fetchall()
        return users
    def get_user_task(self,user_id):
        db = Databaseconnection()
        sql_stament = """ select a.task_id,a.title,b.title,a.description from Tasks a INNER JOIN Categories b ON a.task_id = b.task_id
                      """
        #sql_stament = """insert into Andela (name,age,gender,broke)values('{}','{}','{}','{}');"""
        db.cursor.execute(sql_stament)
        users = db.cursor.fetchall()
        return users

   

if __name__ == "__main__":
    
    
    table = Create_tables()

    table.create_table_Users()
    table.create_table_Tasks()
    table.create_table_Categories()
    #table.Add_users()
    user = table.select_user()
    user_task = table.get_user_task(2)

    print(user)