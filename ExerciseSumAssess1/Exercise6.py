correct = '12345'
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    user = input('Enter password: ')
    if user == correct:
        print ('Access Granted')
        break
    else:
        attempts += 1
        print (f'Access Denied, You have {max_attempts-attempts} attempts left')

if attempts == max_attempts:
    print('The Authorities has been alerted')