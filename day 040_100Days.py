name = input("Input your name : ").strip().capitalize()
birth = input("Input your date of birth : ").strip()
phone = input("Input your phone number : ").strip()
email = input("Input your email : ")

contact_card = {"name" : name , "birth" : birth , "phone" : phone , "email" : email}


print(f"Hi {name}. Our dictionary says that you were born on {birth}. We can call you on {phone} or send you an email at {email}.")
