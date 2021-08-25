#Ask for his/her name for a personalised experience
import greeting
user = greeting.user(input('What\'s your name? '))
#Greet our user
user.greet_user()
#Visit Main Menu
import MainMenu
main_page = MainMenu.Main_menu(main_menu =(
            input("Choose a category:\n1. Trainers\n2. Students\n3. Courses\n4. Assignments\n5. Exit \nPlease express your desire by typing one of the numbers above: ")))
main_page.serve_user()