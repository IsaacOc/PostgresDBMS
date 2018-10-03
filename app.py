import datetime
from Table_create import Create_tables




if __name__ == "__main__":

    created_at = datetime.datetime.now().strftime("%x %X")
    
    table = Create_tables()

    table.create_table_Users()
    table.create_table_Tasks()
    table.create_table_Categories()
    
    #table.Add_users('Mark','Kurl',30,'markkurl@mail.com','marko0',created_at)
    table.Update_user('Marks','kurl',20,'mark@mail.com','kurl00',created_at,6)
    
    user = table.select_user()
    user_task = table.get_user_task(2)
  
    print(user)
    print("\n")
    print(user_task)