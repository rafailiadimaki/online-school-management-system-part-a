class Trainers:
    def view_trainers():        
        collection = input('Which collection do you want to see?\n1.A collection of all the trainers\n2.A collection of all the trainers per course\n3.Back\nPlease make your choice: ')
        if collection.isdigit():
            if collection == '1':
                print(Trainers.view_trainers1())
                print()
                Trainers.view_trainers()
            if collection == '2':
                print(Trainers.view_trainers2())
                print()
                Trainers.view_trainers()
            if collection == '3':
                print()
            if collection != '1' and collection != '2' and collection != '3':
                print()
                print('Ooops! What you have typed is not a number from 1 to 3. Try again. ;)')
                Trainers.view_trainers()
        elif not collection.isdigit():
            while not collection.isdigit():
                collection = input(f"I didn\'t get that. Please type your numbers in digits: ")
            else:
                if collection == '1':
                    print(Trainers.view_trainers1())
                    print()
                    Trainers.view_trainers()
                if collection == '2':
                    print(Trainers.view_trainers2())
                    print()
                    Trainers.view_trainers()
                if collection == '3':
                    print()
                if collection != '1' and collection != '2' and collection != '3':
                    print()
                    print('Ooops! What you have typed is not a number from 1 to 3. Try again. ;)')
                    Trainers.view_trainers()
    def view_trainers1():
            print()
            print('----------------------------------------------------')
            print('                        ⓅⓇⒾⓋⒶⓉⒺ  ⓈⒸⒽⓄⓄⓁ                                        ')
            print("Existing trainers are shown below:")
            print()        
            NewTrainers = [
                {"Code": "2000","First Name": "ANTHONY","Last Name":"FOX", "subject":"SOFTWARE DESIGN AND DEVELOPMENT"},
                {"Code": "2001","First Name": "ALEXANDER","Last Name":"FULLER", "subject":"SOFTWARE DESIGN AND DEVELOPMENT"}
                ]
            return NewTrainers
    def view_trainers2():
            print()
            print('---------------------------------------------------------------')
            print('                        ⓅⓇⒾⓋⒶⓉⒺ  ⓈⒸⒽⓄⓄⓁ                                        ')
            print("Existing trainers are shown below:")
            print()        
            NewTrainers = [
                {"Code": "2000","First Name": "ANTHONY","Last Name":"FOX","subject":"SOFTWARE DESIGN AND DEVELOPMENT","Course": "C#"},
                {"Code": "2001","First Name": "ALEXANDER","Last Name":"FULLER","subject":"SOFTWARE DESIGN AND DEVELOPMENT","Course": "PYTHON"}
                ]
            return NewTrainers
    def add_trainers(list, item):
        import copy
        list.append(item)
        return list
    def new_trainer():
        collection = input('Which collection do you want to update?\n1.A collection of all the trainers\n2.A collection of all the trainers per course\n3.Back\nPlease make your choice: ')
        if collection.isdigit():
            if collection == '1':
                Trainers.new_trainer1()
                print()
                Trainers.new_trainer()
            if collection == '2':
                Trainers.new_trainer2()
                print()
                Trainers.new_trainer()
            if collection == '3':
                print()
            if collection != '1' and collection != '2' and collection != '3':
                print()
                print('Ooops! What you have typed is not a number from 1 to 3. Try again. ;)')
                Trainers.new_trainer()
        elif not collection.isdigit():
            while not collection.isdigit():
                collection = input(f"I didn\'t get that. Please type your numbers in digits: ")
            else:
                if collection == '1':
                    Trainers.new_trainer1()
                    print()
                    Trainers.new_trainer()
                if collection == '2':
                    Trainers.new_trainer2()
                    print()
                    Trainers.new_trainer()
                if collection == '3':
                    print()
                if collection != '1' and collection != '2' and collection != '3':
                    print()
                    print('Ooops! What you have typed is not a number from 1 to 3. Try again. ;)')
                    Trainers.new_trainer()    
    def new_trainer1():
        number = input('How many trainers do you want to add? ')
        if not number.isdigit():
            while not number.isdigit():
                number = input(f"I didn\'t get that. Please type your numbers in digits: ")
            else:
                import sys
                for i in range(int(number)):
                    import unidecode
                    print()
                    print('Please fill out every field in the form, and then press ENTER. For dummy data, leave the fields empty.')
                    import random
                    random_identifiers = list(range(10000,99999))
                    random.shuffle(random_identifiers)
                    code = random.sample(random_identifiers, 1)
                    code = ' '.join([str(elem) for elem in code])
                    first_name = unidecode.unidecode(input('Trainer\'s name: ')).upper()
                    if first_name=='':
                        random_first_names = ['Samantha', 'Kim','Oscar', 'Tom', 'Oz']
                        random.shuffle(random_first_names)
                        first_name = random.choice(random_first_names)
                    last_name = unidecode.unidecode(input('Trainer\'s surname: ')).upper()
                    if last_name=='':
                        random_last_names = ['Johnson','Williams','Brown','Jones','Garcia']
                        random.shuffle(random_last_names)
                        last_name = random.choice(random_last_names)
                    subject = unidecode.unidecode(input("There are the following subjects available:\n* Software Design and Development\n* Introduction to Programming\n* Object Oriented Programming\n* Web Design and Development Fundamentals (Front End)\n* (Relational) Databases\n* Web Application Development, MVC and other Frameworks\n* Software Testing And Debugging\n* UI/UX - Usability\n* Developer soft skills and teamwork\nSubject: ")).upper()
                    while subject != 'SOFTWARE DESIGN AND DEVELOPMENT' and subject != 'INTRODUCTION TO PROGRAMMING' and subject != 'OBJECT ORIENTED PROGRAMMING' and subject !='WEB DESIGN AND DEVELOPMENT FUNDAMENTALS (FRONT END)' and subject !='(RELATIONAL) DATABASES' and subject !='WEB APPLICATION DEVELOPMENT, MVC AND OTHER FRAMEWORKS' and subject !='SOFTWARE TESTING AND DEBUGGING' and subject !='UI/UX - USABILITY' and subject !='DEVELOPER SOFT SKILLS AND TEAMWORK' and subject !='':
                        subject = unidecode.unidecode(input("Fix your spelling mistakes and try again. Subject: ")).upper()
                    if subject=='':
                        random_subjects = ['SOFTWARE DESIGN AND DEVELOPMENT', 'INTRODUCTION TO PROGRAMMING', 'OBJECT ORIENTED PROGRAMMING','WEB DESIGN AND DEVELOPMENT FUNDAMENTALS (FRONT END)', '(RELATIONAL) DATABASES', 'WEB APPLICATION DEVELOPMENT, MVC AND OTHER FRAMEWORKS', 'SOFTWARE TESTING AND DEBUGGING', 'UI/UX - USABILITY', 'DEVELOPER SOFT SKILLS AND TEAMWORK']
                        random.shuffle(random_subjects)
                        subject = random.choice(random_subjects)
                    print()
                    print('Thank you! The form has been submitted successfully.')
                    print('----------------------------------------------------')
                    print()
                    new_trainer = {"Code": code, "First Name": first_name, "Last Name": last_name, "Subject": subject}
                    newlist = Trainers.add_trainers(Trainers.view_trainers1(), new_trainer)
                    print('Here\'s the new trainer that will be added in the upcomimg days.')
                    print(newlist)
        else:
            import sys
            for i in range(int(number)):
                import unidecode
                print()
                print('Please fill out every field in the form, and then press ENTER. For dummy data, leave the fields empty.')
                import random
                random_identifiers = list(range(10000,99999))
                random.shuffle(random_identifiers)
                code = random.sample(random_identifiers, 1)
                code = ' '.join([str(elem) for elem in code])
                first_name = unidecode.unidecode(input('Trainer\'s name: ')).upper()
                if first_name=='':
                    random_first_names = ['SAMANTHA', 'KIM','OSCAR', 'TOM', 'OZ']
                    random.shuffle(random_first_names)
                    first_name = random.choice(random_first_names)
                last_name = unidecode.unidecode(input('Trainer\'s surname: ')).upper()
                if last_name=='':
                    random_last_names = ['JOHNSON','WILLIAMS','BROWN','JONES','GARCIA']
                    random.shuffle(random_last_names)
                    last_name = random.choice(random_last_names)
                subject = unidecode.unidecode(input("There are the following subjects available:\n* Software Design and Development\n* Introduction to Programming\n* Object Oriented Programming\n* Web Design and Development Fundamentals (Front End)\n* (Relational) Databases\n* Web Application Development, MVC and other Frameworks\n* Software Testing And Debugging\n* UI/UX - Usability\n* Developer soft skills and teamwork\nSubject: ")).upper()
                while subject != 'SOFTWARE DESIGN AND DEVELOPMENT' and subject != 'INTRODUCTION TO PROGRAMMING' and subject != 'OBJECT ORIENTED PROGRAMMING' and subject !='WEB DESIGN AND DEVELOPMENT FUNDAMENTALS (FRONT END)' and subject !='(RELATIONAL) DATABASES' and subject !='WEB APPLICATION DEVELOPMENT, MVC AND OTHER FRAMEWORKS' and subject !='SOFTWARE TESTING AND DEBUGGING' and subject !='UI/UX - USABILITY' and subject !='DEVELOPER SOFT SKILLS AND TEAMWORK' and subject !='':
                    subject = unidecode.unidecode(input("Fix your spelling mistakes and try again. Subject: ")).upper()
                if subject=='':
                    random_subjects = ['SOFTWARE DESIGN AND DEVELOPMENT', 'INTRODUCTION TO PROGRAMMING', 'OBJECT ORIENTED PROGRAMMING','WEB DESIGN AND DEVELOPMENT FUNDAMENTALS (FRONT END)', '(RELATIONAL) DATABASES', 'WEB APPLICATION DEVELOPMENT, MVC AND OTHER FRAMEWORKS', 'SOFTWARE TESTING AND DEBUGGING', 'UI/UX - USABILITY', 'DEVELOPER SOFT SKILLS AND TEAMWORK']
                    random.shuffle(random_subjects)
                    subject = random.choice(random_subjects)
                print()
                print('Thank you! The form has been submitted successfully.')
                print('----------------------------------------------------')
                print()
                new_trainer = {"Code": code, "First Name": first_name, "Last Name": last_name, "Subject": subject}
                newlist = Trainers.add_trainers(Trainers.view_trainers1(), new_trainer)
                print('Here\'s the new trainer that will be added in the upcomimg days.')
                print(newlist)
        print()
        print("After the secretary's authorization, your information will be published\non our website within three working days. If you find out any mistakes,\nplease email us at infoprivateschool@gmail.com as soon as possible.")
    def new_trainer2():
        number = input('How many trainers do you want to add? ')
        if not number.isdigit():
            while not number.isdigit():
                number = input(f"I didn\'t get that. Please type your numbers in digits: ")
            else:
                import sys
                for i in range(int(number)):
                    import unidecode
                    print()
                    print('Please fill out every field in the form, and then press ENTER. For dummy data, leave the fields empty.')
                    import random
                    random_identifiers = list(range(10000,99999))
                    random.shuffle(random_identifiers)
                    code = random.sample(random_identifiers, 1)
                    code = ' '.join([str(elem) for elem in code])
                    first_name = unidecode.unidecode(input('Trainer\'s name: ')).upper()
                    if first_name=='':
                        random_first_names = ['Samantha', 'Kim','Oscar', 'Tom', 'Oz']
                        random.shuffle(random_first_names)
                        first_name = random.choice(random_first_names)
                    last_name = unidecode.unidecode(input('Trainer\'s surname: ')).upper()
                    if last_name=='':
                        random_last_names = ['Johnson','Williams','Brown','Jones','Garcia']
                        random.shuffle(random_last_names)
                        last_name = random.choice(random_last_names)
                    subject = unidecode.unidecode(input("There are the following subjects available:\n* Software Design and Development\n* Introduction to Programming\n* Object Oriented Programming\n* Web Design and Development Fundamentals (Front End)\n* (Relational) Databases\n* Web Application Development, MVC and other Frameworks\n* Software Testing And Debugging\n* UI/UX - Usability\n* Developer soft skills and teamwork\nSubject: ")).upper()
                    while subject != 'SOFTWARE DESIGN AND DEVELOPMENT' and subject != 'INTRODUCTION TO PROGRAMMING' and subject != 'OBJECT ORIENTED PROGRAMMING' and subject !='WEB DESIGN AND DEVELOPMENT FUNDAMENTALS (FRONT END)' and subject !='(RELATIONAL) DATABASES' and subject !='WEB APPLICATION DEVELOPMENT, MVC AND OTHER FRAMEWORKS' and subject !='SOFTWARE TESTING AND DEBUGGING' and subject !='UI/UX - USABILITY' and subject !='DEVELOPER SOFT SKILLS AND TEAMWORK' and subject !='':
                        subject = unidecode.unidecode(input("Fix your spelling mistakes and try again. Subject: ")).upper()
                    if subject=='':
                        random_subjects = ['SOFTWARE DESIGN AND DEVELOPMENT', 'INTRODUCTION TO PROGRAMMING', 'OBJECT ORIENTED PROGRAMMING','WEB DESIGN AND DEVELOPMENT FUNDAMENTALS (FRONT END)', '(RELATIONAL) DATABASES', 'WEB APPLICATION DEVELOPMENT, MVC AND OTHER FRAMEWORKS', 'SOFTWARE TESTING AND DEBUGGING', 'UI/UX - USABILITY', 'DEVELOPER SOFT SKILLS AND TEAMWORK']
                        random.shuffle(random_subjects)
                        subject = random.choice(random_subjects)
                    course= unidecode.unidecode(input("Our school provides the following courses:Python, C#, Javascript and Java.\nCourse:")).upper() 
                    while course != 'C#' and course != 'JAVASCRIPT' and course != 'JAVA' and course != 'PYTHON' and course != '':
                        course = unidecode.unidecode(input("Our school provides only the following courses:\nPython, C#, Javascript and Java. Course: ")).upper()
                    if course == '':
                        random_courses = ['DZONGKHA', 'YUE', 'TUVALUAN']
                        random.shuffle(random_courses)
                        course = random.choice(random_courses)
                    print()
                    print('Thank you! The form has been submitted successfully.')
                    print('----------------------------------------------------')
                    print()
                    new_trainer = {"Code": code, "First Name": first_name, "Last Name": last_name, "Subject": subject, "Course": course}
                    newlist = Trainers.add_trainers(Trainers.view_trainers2(), new_trainer)
                    print('Here\'s the new trainer that will be added in the upcomimg days.')
                    print(newlist)
        else:
            import sys
            for i in range(int(number)):
                import unidecode
                print()
                print('Please fill out every field in the form, and then press ENTER. For dummy data, leave the fields empty.')
                import random
                random_identifiers = list(range(10000,99999))
                random.shuffle(random_identifiers)
                code = random.sample(random_identifiers, 1)
                code = ' '.join([str(elem) for elem in code])
                first_name = unidecode.unidecode(input('Trainer\'s name: ')).upper()
                if first_name=='':
                    random_first_names = ['SAMANTHA', 'KIM','OSCAR', 'TOM', 'OZ']
                    random.shuffle(random_first_names)
                    first_name = random.choice(random_first_names)
                last_name = unidecode.unidecode(input('Trainer\'s surname: ')).upper()
                if last_name=='':
                    random_last_names = ['JOHNSON','WILLIAMS','BROWN','JONES','GARCIA']
                    random.shuffle(random_last_names)
                    last_name = random.choice(random_last_names)
                subject = unidecode.unidecode(input("There are the following subjects available:\n* Software Design and Development\n* Introduction to Programming\n* Object Oriented Programming\n* Web Design and Development Fundamentals (Front End)\n* (Relational) Databases\n* Web Application Development, MVC and other Frameworks\n* Software Testing And Debugging\n* UI/UX - Usability\n* Developer soft skills and teamwork\nSubject: ")).upper()
                while subject != 'SOFTWARE DESIGN AND DEVELOPMENT' and subject != 'INTRODUCTION TO PROGRAMMING' and subject != 'OBJECT ORIENTED PROGRAMMING' and subject !='WEB DESIGN AND DEVELOPMENT FUNDAMENTALS (FRONT END)' and subject !='(RELATIONAL) DATABASES' and subject !='WEB APPLICATION DEVELOPMENT, MVC AND OTHER FRAMEWORKS' and subject !='SOFTWARE TESTING AND DEBUGGING' and subject !='UI/UX - USABILITY' and subject !='DEVELOPER SOFT SKILLS AND TEAMWORK' and subject !='':
                    subject = unidecode.unidecode(input("Fix your spelling mistakes and try again. Subject: ")).upper()
                if subject=='':
                    random_subjects = ['SOFTWARE DESIGN AND DEVELOPMENT', 'INTRODUCTION TO PROGRAMMING', 'OBJECT ORIENTED PROGRAMMING','WEB DESIGN AND DEVELOPMENT FUNDAMENTALS (FRONT END)', '(RELATIONAL) DATABASES', 'WEB APPLICATION DEVELOPMENT, MVC AND OTHER FRAMEWORKS', 'SOFTWARE TESTING AND DEBUGGING', 'UI/UX - USABILITY', 'DEVELOPER SOFT SKILLS AND TEAMWORK']
                    random.shuffle(random_subjects)
                    subject = random.choice(random_subjects)
                course= unidecode.unidecode(input("Our school provides the following courses:Python, C#, Javascript and Java.\nCourse:")).upper() 
                while course != 'C#' and course != 'JAVASCRIPT' and course != 'JAVA' and course != 'PYTHON' and course != '':
                    course = unidecode.unidecode(input("Our school provides only the following courses:\nPython, C#, Javascript and Java. Course: ")).upper()
                if course == '':
                    random_courses = ['DZONGKHA', 'YUE', 'TUVALUAN']
                    random.shuffle(random_courses)
                    course = random.choice(random_courses)
                print()
                print('Thank you! The form has been submitted successfully.')
                print('----------------------------------------------------')
                print()
                new_trainer = {"Code": code, "First Name": first_name, "Last Name": last_name, "Subject": subject, "Course":course}
                newlist = Trainers.add_trainers(Trainers.view_trainers2(), new_trainer)
                print('Here\'s the new trainer that will be added in the upcomimg days.')
                print(newlist)
        print()
        print("After the secretary's authorization, your information will be published\non our website within three working days. If you find out any mistakes,\nplease email us at infoprivateschool@gmail.com as soon as possible.")
