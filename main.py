from password_manager import PasswordManager

def main():
    password_manager = PasswordManager('passwords.db')

    while True:
        print('What would you like to do?')
        print('1. Add a password')
        print('2. Retrieve a password')
        print('3. Update a password')
        print('4. Delete a password')
        print('5. Quit')

        choice = input('> ')

        if choice == '1':
            website = input('Enter the website: ')
            username = input('Enter the username: ')
            password = input('Enter the password: ')
            password_manager.add_password(website, username, password)
            print('Password added successfully!')
        elif choice == '2':
            website = input('Enter the website: ')
            username = input('Enter the username: ')
            password = password_manager.get_password(website, username)
            if password:
                print('Password:', password)
            else:
                print('Password not found.')
        elif choice == '3':
            website = input('Enter the website: ')
            username = input('Enter the username: ')
            password = input('Enter the new password: ')
            password_manager.update_password(website, username, password)
            print('Password updated successfully!')
        elif choice == '4':
            website = input('Enter the website: ')
            username = input('Enter the username: ')
            password_manager.delete_password(website, username)
            print('Password deleted successfully!')
        elif choice == '5':
            password_manager.close()
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
