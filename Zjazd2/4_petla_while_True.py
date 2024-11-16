# standard_username = 'Kamil'
# standard_passwd = '1234'
# service_passwd = 'service'
#
# username = input('Podaj nazwe:  ')
# passwd = input('Podaj haslo:  ')
# while username != standard_username or passwd != standard_passwd:
#     print('Zle dane')
#     username = input('Podaj nazwe:  ')
#     passwd = input('Podaj haslo:  ')
# print('Zalogowano')

standard_username = 'Kamil'
standard_passwd = '1234'
service_passwd = 'service'

username = input('Podaj nazwe:  ')
passwd = input('Podaj haslo:  ')
while True:
    if username == standard_username and passwd == standard_passwd:
        break
    elif passwd == service_passwd:
        break
    print('Zle dane')
    username = input('Podaj nazwe:  ')
    passwd = input('Podaj haslo:  ')

print('Zalogowano')
