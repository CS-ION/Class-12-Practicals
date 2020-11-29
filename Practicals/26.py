emails,username,domain = (),(),()

for I in range(int(input('Enter the total no of email ids :'))):
    email = input('Enter email id :') 
    emails += (email,)
    username += (email.split('@')[0],)
    domain += (email.split('@')[1],)

for I in range(len(emails)):
    print(f'{emails[I]} \t {username[I]}  \t  {domain[I]}')