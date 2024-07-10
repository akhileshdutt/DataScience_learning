import json

class databases:
    def insert_data(name,email,password):
        with open("users.json","r") as rd:
            user_data = json.load(rd)
        
            if email in user_data:
                return 0
            else:
                user_data[email] = [name,password]

        with open("users.json","w") as wr:
            json.dump(user_data,wr)
            return 1

