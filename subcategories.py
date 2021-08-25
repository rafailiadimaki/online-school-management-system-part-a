class subcategories:
    def __init__(self, main_menu):
            self.main_menu = main_menu
    def user_choice(self):
        if self.main_menu == '1':
            print('______________________________________________________________')
            print()
            subcategory_option = input("1. View trainers\n2. Add trainers\n3. Back\nWhat would you like to do? Enter a number: ")
            Subcategory_menu   = subcategory_menu('trainers',f'{subcategory_option}')
            Subcategory_menu.subcategory_nextstep()
        if self.main_menu == '2':
            print('______________________________________________________________')
            print()
            subcategory_option = input("1. View students\n2. Add students\n3. Back\nWhat would you like to do? Enter a number: ")
            Subcategory_menu   = subcategory_menu('students',f'{subcategory_option}')
            Subcategory_menu.subcategory_nextstep()
        if self.main_menu == '3':
            print('______________________________________________________________')
            print()
            subcategory_option = input("1. View courses\n2. Add courses\n3. Back\nWhat would you like to do? Enter a number: ")
            Subcategory_menu   = subcategory_menu('courses',f'{subcategory_option}')
            Subcategory_menu.subcategory_nextstep()
        if self.main_menu == '4':
            print('______________________________________________________________')
            print()
            subcategory_option = input("1. View assignments\n2. Add assignments\n3. Back\nWhat would you like to do? Enter a number: ")
            Subcategory_menu   = subcategory_menu('assignments',f'{subcategory_option}')
            Subcategory_menu.subcategory_nextstep()
        if self.main_menu == '5':
            import sys
            print('______________________________________________________________')
            print()
            #Ask them before they leave for feedback 
            exit_question=input('Just a moment — Were you able to complete your task today? y/n ')
            if exit_question=='Y' or exit_question=='y':
                print('That\'s really nice to hear. I hope the rest of your day is pleasant. Byeeee.')
                sys.exit()
            elif exit_question=='N' or exit_question=='n':
                x=input('We\'re sorry for the inconvenience. Please let us know what we can do differently or better below:\n')
                print('Thank you for your time. We\'ll do our best in supporting you in the future. Goodbye.')
                sys.exit()
            else:
                print('I\'m not sure I understood that. Goodbye for now.')
                sys.exit()
class subcategory_menu():
    def __init__(self, of_what, option):
        self.of_what = of_what
        self.option  = option
    def subcategory_nextstep(self):
        #import dataset
        #import quantity
        import MainMenu
        if self.option.isdigit():
            if self.option == '1':
                import Courses
                import Trainers
                import Students
                import Assignments
                if self.of_what=='courses':
                    print(Courses.Courses.view_courses())
                if self.of_what=='trainers':
                    Trainers.Trainers.view_trainers()
                if self.of_what=='students':
                    Students.Students.view_students()
                if self.of_what=='assignments':
                    Assignments.Assignments.view_assignments()
                subset = subcategories('self.main_menu')
                subset.user_choice()
            if self.option == '2':
                print('______________________________________________________________')
                if self.of_what=='courses':
                    import Courses
                    print(Courses.Courses.new_course())
                if self.of_what=='trainers':
                    import Trainers
                    Trainers.Trainers.new_trainer()
                if self.of_what=='students':
                    import Students
                    Students.Students.new_student()
                if self.of_what=='assignments':
                    import Assignments
                    Assignments.Assignments.new_assignment()
                subset = subcategories('self.main_menu')
                subset.user_choice()
            if self.option == '3':
                print('______________________________________________________________')
                main_page = MainMenu.Main_menu(main_menu =(
                input("Choose a category:\n1. Trainers\n2. Students\n3. Courses\n4. Assignments\n5. Exit \nPlease express your desire by typing one of the numbers above: ")))
                main_page.serve_user()
            if self.option != '1' and self.option != '2' and self.option != '3':
                print('What you have typed is not a number from 1 to 3.')
                subset = subcategories('self.main_menu')
                subset.user_choice()
        elif not self.option.isdigit():
            while not self.option.isdigit():
                self.option = input(f"I didn\'t get that. Please type your numbers in digits: ")
            else:
                if self.option == '1':
                    if self.of_what=='courses':
                        import Courses
                        print(Courses.Courses.view_courses())
                    if self.of_what=='trainers':
                        import Trainers
                        Trainers.Trainers.view_trainers()
                    if self.of_what=='students':
                        import Students
                        Students.Students.view_students()
                    if self.of_what=='assignments':
                        import Assignments
                        Assignments.Assignments.view_assignments()
                subset = subcategories('self.main_menu')
                subset.user_choice()
                if self.option == '2':
                    print('______________________________________________________________')
                    if self.of_what=='courses':
                        import Courses
                        print(Courses.Courses.new_course())
                    if self.of_what=='trainers':
                        import Trainers
                        Trainers.Trainers.new_trainer()
                    if self.of_what=='students':
                        import Students
                        Students.Students.new_student()
                    if self.of_what=='assignments':
                        import Assignments
                        Assignments.Assignments.new_assignment()
                subset = subcategories('self.main_menu')
                subset.user_choice()
                if self.option == '3':
                    print('______________________________________________________________')
                    main_page = MainMenu.Main_menu(main_menu =(
                    input("Choose a category:\n1. Trainers\n2. Students\n3. Courses\n4. Assignments\n5. Exit \nPlease express your desire by typing one of the numbers above: ")))
                    main_page.serve_user()
                if self.option != '1' and self.option != '2' and self.option != '3':
                    print('What you have typed is not a number from 1 to 3.')
                    subset = subcategories('self.main_menu')
                    subset.user_choice()
                    if self.option == '1':
                        if self.of_what=='courses':
                            import Courses
                            print(Courses.Courses.view_courses())
                        if self.of_what=='trainers':
                            import Trainers
                            Trainers.Trainers.view_trainers()
                        if self.of_what=='students':
                            import Students
                            Students.Students.view_students()
                        if self.of_what=='assignments':
                            import Assignments
                            Assignments.Assignments.view_assignments()
                        subset = subcategories('self.main_menu')
                        subset.user_choice()
                    if self.option == '2':
                        print('______________________________________________________________')
                        if self.of_what=='courses':
                            import Courses
                            print(Courses.Courses.new_course())
                        if self.of_what=='trainers':
                            import Trainers
                            Trainers.Trainers.new_trainer()
                        if self.of_what=='students':
                            import Students
                            Students.Students.new_student()
                        if self.of_what=='assignments':
                            import Assignments
                            Assignments.Assignments.new_assignment()
                    subset = subcategories('self.main_menu')
                    subset.user_choice()
                    if self.option == '3':
                        print('______________________________________________________________')
                        main_page = MainMenu.Main_menu(main_menu =(
                        input("Choose a category:\n1. Trainers\n2. Students\n3. Courses\n4. Assignments\n5. Exit \nPlease express your desire by typing one of the numbers above: ")))
                        main_page.serve_user()
