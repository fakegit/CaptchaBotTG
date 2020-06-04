from dbconnector import *
class UserList(object):

    #Add value to list with users
    def Save(self,user_id):
     if self.Check_User(user_id)==False:
         edit(f"insert into user values({user_id})")


    #Check if user in list
    def Check_User(self,user_id):
        return Get_Lenght(f"select id from user where id= {user_id}")