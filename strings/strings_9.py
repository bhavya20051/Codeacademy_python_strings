def username_generator(first_name,last_name):
  username= first_name[:3]+last_name[:4]
  return username
def password_generator(username):
  password=""
  for i in range(0,len(username)):
   password=username[-1]+username[0:-1]
   return password
   