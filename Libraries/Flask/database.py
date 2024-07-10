# import json

# class databases:
#     def insert_data(name,email,password):
#         with open("users.json","r") as rd:
#             users = json.load(rd)
        
#             if email in users:
#                 return 0
#             else:
#                 users[email] = [name,password]

#         with open("users.json","w") as wr:
#             json.dump(users,wr)
#             return 1

import json

class databases:
    def insert_data(self, name, email, password):
        try:
            with open("users.json", "r") as rd:
                user_data = json.load(rd)
        except FileNotFoundError:
            user_data = {}
        
        if email in user_data:
            return 0
        else:
            user_data[email] = [name, password]

        with open("users.json", "w") as wr:
            json.dump(user_data, wr)
        
        return 1
