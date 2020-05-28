first_name = "Julie"
last_name = "Blevins"
def account_generator(first_name,last_name):
  p1= first_name[:3]
  p2= last_name[:3]
  account_name= p1+ p2
  return account_name
print(account_generator("Julie","Blevins"))
new_account=account_generator("Julie","Blevins")
print(new_account)