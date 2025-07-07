print("Replit Login System")
print()

def login():
  while True:
      login_dict = {
      "jiho" : "jiho123", 
      "nao" : "nao123", 
      "taro" : "taro123", 
      "kuro" : "kuro123", 
      "shiro" : "shiro123"
      }
  
      user_id = input("What is your ID?: ")
      password = input("What is your password?: ")

      if user_id in login_dict and login_dict[user_id] ==   password:
        print("Welcome to Replit!")
        break
      elif user_id not in login_dict:
        print("Please Check your ID or password")
      elif user_id in login_dict and login_dict[user_id] != password:
        print("Please Check your password")
      else:
        print("Please Check your ID or password")

login()
