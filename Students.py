#Make sure to run the command pip3 install python-dateutil
class Students:
    def view_students():        
        collection = input('Which collection do you want to see?\n1.A collection of all the students\n2.A collection of all the students per course\n3.A collection of all the students that belong to more than one courses\n4.Back\nPlease make your choice: ')
        if collection.isdigit():
            if collection == '1':
                print(Students.view_students1())
                print()
                Students.view_students()
            if collection == '2':
                print(Students.view_students2())
                print()
                Students.view_students()
            if collection == '3':
                print()
                print(Students.view_students3())
                print()
                Students.view_students()
            if collection == '4':
                print()
            if collection != '1' and collection != '2' and collection != '3' and collection != '4':
                print()
                print('Ooops! What you have typed is not a number from 1 to 4. Try again. ;)')
                Students.view_students()
        elif not collection.isdigit():
            while not collection.isdigit():
                collection = input(f"I didn\'t get that. Please type your numbers in digits: ")
            else:
                if collection == '1':
                    print(Students.view_students1())
                    print()
                    Students.view_students()
                if collection == '2':
                    print(Students.view_students2())
                    print()
                    Students.view_students()
                if collection == '3':
                    print(Students.view_students3())
                    print()
                    Students.view_students()
                if collection == '4':
                    print()
                if collection != '1' and collection != '2' and collection != '3' and collection != '4':
                    print()
                    print('Ooops! What you have typed is not a number from 1 to 4. Try again. ;)')
                    Students.view_students()
    def view_students1():
            print()
            print('----------------------------------------------------')
            print('                        ⓅⓇⒾⓋⒶⓉⒺ  ⓈⒸⒽⓄⓄⓁ                                        ')
            print("Existing students are shown below:")
            print()        
            NewStudents = [
                {"Code": "0001","First Name": "MICHAELA","Last Name":"GORDON", "Date of Birth":"7/6/1990","Tuition Fees":"700"},
                {"Code": "0002","First Name": "ALEXANDER","Last Name":"FULLER", "Date of Birth":"2/9/1989","Tuition Fees":"2500"}
                ]
            return NewStudents
    def view_students2():
            print()
            print('----------------------------------------------------')
            print('                        ⓅⓇⒾⓋⒶⓉⒺ  ⓈⒸⒽⓄⓄⓁ                                        ')
            print("Existing students are shown below:")
            print()        
            NewStudents = [
                {"Code": "0001","First Name": "MICHAELA","Last Name":"GORDON", "Date of Birth":"7/6/1990","Tuition Fees":"700", "Course(s)": "PYTHON, JAVA"},
                {"Code": "0002","First Name": "ALEXANDER","Last Name":"FULLER", "Date of Birth":"2/9/1989","Tuition Fees":"2500", "Course(s)": "JAVA"}
                ]
            return NewStudents
    def view_students3():
            print()     
            NewStudents = [
                {"Code": "0001","First Name": "MICHAELA","Last Name":"GORDON"}
                ]
            return NewStudents
    def add_students(list, item):
        import copy
        list.append(item)
        return list
    def new_student():
        collection = input('Which collection do you want to update?\n1.A collection of all the students\n2.A collection of all the students per course\n3.Back\nPlease make your choice: ')
        if collection.isdigit():
            if collection == '1':
                Students.new_student1()
                print()
                Students.new_student()
            if collection == '2':
                Students.new_student2()
                print()
                Students.new_student()
            if collection == '3':
                print()
            if collection != '1' and collection != '2' and collection != '3':
                print()
                print('Ooops! What you have typed is not a number from 1 to 3. Try again. ;)')
                Students.new_student()
        elif not collection.isdigit():
            while not collection.isdigit():
                collection = input(f"I didn\'t get that. Please type your numbers in digits: ")
            else:
                if collection == '1':
                    Students.new_student1()
                    print()
                    Students.new_student()
                if collection == '2':
                    Students.new_student2()
                    print()
                    Students.new_student()
                if collection == '3':
                    print()
                if collection != '1' and collection != '2' and collection != '3':
                    print()
                    print('Ooops! What you have typed is not a number from 1 to 3. Try again. ;)')
                    Students.new_student()
    def new_student1():
        number = input('How many students do you want to add? ')
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
                    random_identifiers = list(range(100000,999999))
                    random.shuffle(random_identifiers)
                    code=random.sample(random_identifiers, 1)
                    code=''.join([str(elem) for elem in code])
                    first_name = unidecode.unidecode(input('Student\'s name: ')).upper()
                    if first_name=='':
                        random_first_names = ['Juliette', 'Diego', 'Jason', 'Carlos', 'Emilio', 'Selena ']
                        random.shuffle(random_first_names)
                        first_name = random.choice(random_first_names)
                    last_name = unidecode.unidecode(input('Student\'s surname: ')).upper()
                    if last_name=='':
                        random_last_names = ['Brown','Jones','Garcia','Davis','Lopez', 'Jackson']
                        random.shuffle(random_last_names)
                        last_name = random.choice(random_last_names)
                    from dateutil.parser import parse
                    try:
                        date_of_birth=parse(input("Date of birth in the format(m/d/y): "))
                    except ValueError:
                        random_dates=['11/12/2012','3/6/2011','12/8/2013','1/1/1999','6/5/1992','7/9/2000','4/6/2001','12/27/2002', '12/26/2007', '5/15/2008']
                        random.shuffle(random_dates)
                        date_of_birth=random.choice(random_dates)
                        pass                                                    
                    else:
                        date_of_birth = date_of_birth.strftime('%m/%d/%Y')
                        pass
                    fees=input("Tuition fees: ")
                    if fees=='':
                        random_fees=['1010','1600','1800','850','1543','2123','1780','2100', '1503', '1450']
                        random.shuffle(random_fees)
                        fees=random.choice(random_fees)
                    while not (fees.isdigit()):
                        fees=input("Please type your numbers in digits:\nTuition fees: ")
                    else:
                        pass
                    print()
                    print('Thank you! The form has been submitted successfully.')
                    print('----------------------------------------------------')
                    print()
                    new_student = {"Code": code, "First Name": first_name, "Last Name": last_name, "Date of Birth": date_of_birth, "Tuition Fees": fees}
                    newlist = Students.add_students(Students.view_students1(), new_student)
                    print('Here\'s the new student that will be added in the upcomimg days.')
                    print(newlist)
        else:
            import sys
            for i in range(int(number)):
                import unidecode
                print()
                print('Please fill out every field in the form, and then press ENTER. For dummy data, leave the fields empty.')
                import random
                random_identifiers = list(range(100000,999999))
                random.shuffle(random_identifiers)
                code=random.sample(random_identifiers, 1)
                code=''.join([str(elem) for elem in code])
                first_name = unidecode.unidecode(input('Student\'s name: ')).upper()
                if first_name=='':
                    random_first_names = ['Juliette', 'Diego', 'Jason', 'Carlos', 'Emilio', 'Selena ']
                    random.shuffle(random_first_names)
                    first_name = random.choice(random_first_names)
                last_name = unidecode.unidecode(input('Student\'s surname: ')).upper()
                if last_name=='':
                    random_last_names = ['Brown','Jones','Garcia','Davis','Lopez', 'Jackson']
                    random.shuffle(random_last_names)
                    last_name = random.choice(random_last_names)
                from dateutil.parser import parse
                try:
                    date_of_birth=parse(input("Date of birth in the format(m/d/y): "))
                except ValueError:
                    random_dates=['11/12/2012','3/6/2011','12/8/2013','1/1/1999','6/5/1992','7/9/2000','4/6/2001','12/27/2002', '12/26/2007', '5/15/2008']
                    random.shuffle(random_dates)
                    date_of_birth=random.choice(random_dates)
                    pass                                                    
                else:
                    date_of_birth = date_of_birth.strftime('%m/%d/%Y')
                    pass
                fees=input("Tuition fees: ")
                if fees=='':
                    random_fees=['1010','1600','1800','850','1543','2123','1780','2100', '1503', '1450']
                    random.shuffle(random_fees)
                    fees=random.choice(random_fees)
                while not (fees.isdigit()):
                    fees=input("Please type your numbers in digits:\nTuition fees: ")
                else:
                    pass
                print()
                print('Thank you! The form has been submitted successfully.')
                print('----------------------------------------------------')
                print()
                new_student = {"Code": code, "First Name": first_name, "Last Name": last_name, "Date of Birth": date_of_birth, "Tuition Fees": fees}
                newlist = Students.add_students(Students.view_students1(), new_student)
                print('Here\'s the new student that will be added in the upcomimg days.')
                print(newlist)
        print()
        print("After the secretary's authorization, your information will be published\non our website within three working days. If you find out any mistakes,\nplease email us at infoprivateschool@gmail.com as soon as possible.")
    def new_student2():
        number = input('How many students do you want to add? ')
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
                    random_identifiers = list(range(100000,999999))
                    random.shuffle(random_identifiers)
                    code=random.sample(random_identifiers, 1)
                    code=''.join([str(elem) for elem in code])
                    first_name = unidecode.unidecode(input('Student\'s name: ')).upper()
                    if first_name=='':
                        random_first_names = ['Juliette', 'Diego', 'Jason', 'Carlos', 'Emilio', 'Selena ']
                        random.shuffle(random_first_names)
                        first_name = random.choice(random_first_names)
                    last_name = unidecode.unidecode(input('Student\'s surname: ')).upper()
                    if last_name=='':
                        random_last_names = ['Brown','Jones','Garcia','Davis','Lopez', 'Jackson']
                        random.shuffle(random_last_names)
                        last_name = random.choice(random_last_names)
                    from dateutil.parser import parse
                    try:
                        date_of_birth=parse(input("Date of birth in the format(m/d/y): "))
                    except ValueError:
                        random_dates=['11/12/2012','3/6/2011','12/8/2013','1/1/1999','6/5/1992','7/9/2000','4/6/2001','12/27/2002', '12/26/2007', '5/15/2008']
                        random.shuffle(random_dates)
                        date_of_birth=random.choice(random_dates)
                        pass                                                    
                    else:
                        date_of_birth = date_of_birth.strftime('%m/%d/%Y')
                        pass
                    fees=input("Tuition fees: ")
                    if fees=='':
                        random_fees=['1010','1600','1800','850','1543','2123','1780','2100', '1503', '1450']
                        random.shuffle(random_fees)
                        fees=random.choice(random_fees)
                    while not (fees.isdigit()):
                        fees=input("Please type your numbers in digits:\nTuition fees: ")
                    else:
                        pass
                    course= unidecode.unidecode(input("Our school provides the following courses:Python, C#, Javascript and Java.\nCourse:")).upper() 
                    while course != 'C#' and course != 'JAVASCRIPT' and course != 'JAVA' and course != 'PYTHON' and course != '':
                        course = unidecode.unidecode(input("Our school provides only the following courses:\nPython, C#, Javascript and Java. Course: ")).upper()
                    if course == '':
                        random_courses = ['DZONGKHA', 'YUE', 'TUVALUAN']
                        random.shuffle(random_courses)
                        course = random.choice(random_courses)
                    course2 = unidecode.unidecode(input("Does the student attend another course? Y or N? ")).upper()
                    if course2 == 'Y':
                        newcourse = unidecode.unidecode(input("Our school provides the following courses:Python, C#, Javascript and Java.\nCourse:")).upper() 
                        while newcourse != 'C#' and newcourse != 'JAVASCRIPT' and newcourse != 'JAVA' and newcourse != 'PYTHON' and newcourse != '':
                            newcourse = unidecode.unidecode(input("Our school provides only the following courses:\nPython, C#, Javascript and Java. Course: ")).upper()
                        if newcourse == '':
                            random_courses = ['DZONGKHA', 'YUE', 'TUVALUAN']
                            random.shuffle(random_courses)
                            newcourse = random.choice(random_courses)
                        students_courses = course + ', '+ newcourse
                        print()
                        print('Thank you! The form has been submitted successfully.')
                        print('----------------------------------------------------')
                        print()
                        new_student = {"Code": code, "First Name": first_name, "Last Name": last_name, "Date of Birth": date_of_birth, "Tuition Fees": fees, "Course(s)": students_courses}
                        newlist = Students.add_students(Students.view_students2(), new_student)
                        newcomer = {"Code": code, "First Name": first_name, "Last Name": last_name}
                        newlist2 = Students.add_students(Students.view_students3(), newcomer)
                        print('Here\'s the new student that will be added in the upcomimg days.\nThis student belongs to more than one courses.')
                        print(newlist)
                        print()
                        print(newlist2)
                        print()
                        print("After the secretary's authorization, your information will be published\non our website within three working days. If you find out any mistakes,\nplease email us at infoprivateschool@gmail.com as soon as possible.")
                    else:
                        print('Thank you! The form has been submitted successfully.')
                        print('----------------------------------------------------')
                        print()
                        new_student = {"Code": code, "First Name": first_name, "Last Name": last_name, "Date of Birth": date_of_birth, "Tuition Fees": fees, "Course(s)": course}
                        newlist = Students.add_students(Students.view_students2(), new_student)
                        print('Here\'s the new student that will be added in the upcomimg days.')
                        print(newlist)
                        print()
                        print("After the secretary's authorization, your information will be published\non our website within three working days. If you find out any mistakes,\nplease email us at infoprivateschool@gmail.com as soon as possible.")
        else:
            import sys
            for i in range(int(number)):
                import unidecode
                print()
                print('Please fill out every field in the form, and then press ENTER. For dummy data, leave the fields empty.')
                import random
                random_identifiers = list(range(100000,999999))
                random.shuffle(random_identifiers)
                code=random.sample(random_identifiers, 1)
                code=''.join([str(elem) for elem in code])
                first_name = unidecode.unidecode(input('Student\'s name: ')).upper()
                if first_name=='':
                    random_first_names = ['Juliette', 'Diego', 'Jason', 'Carlos', 'Emilio', 'Selena ']
                    random.shuffle(random_first_names)
                    first_name = random.choice(random_first_names)
                last_name = unidecode.unidecode(input('Student\'s surname: ')).upper()
                if last_name=='':
                    random_last_names = ['Brown','Jones','Garcia','Davis','Lopez', 'Jackson']
                    random.shuffle(random_last_names)
                    last_name = random.choice(random_last_names)
                from dateutil.parser import parse
                try:
                    date_of_birth=parse(input("Date of birth in the format(m/d/y): "))
                except ValueError:
                    random_dates=['11/12/2012','3/6/2011','12/8/2013','1/1/1999','6/5/1992','7/9/2000','4/6/2001','12/27/2002', '12/26/2007', '5/15/2008']
                    random.shuffle(random_dates)
                    date_of_birth=random.choice(random_dates)
                    pass                                                    
                else:
                    date_of_birth = date_of_birth.strftime('%m/%d/%Y')
                    pass
                fees=input("Tuition fees: ")
                if fees=='':
                    random_fees=['1010','1600','1800','850','1543','2123','1780','2100', '1503', '1450']
                    random.shuffle(random_fees)
                    fees=random.choice(random_fees)
                while not (fees.isdigit()):
                    fees=input("Please type your numbers in digits:\nTuition fees: ")
                else:
                    pass
                course= unidecode.unidecode(input("Our school provides the following courses:Python, C#, Javascript and Java.\nCourse:")).upper() 
                while course != 'C#' and course != 'JAVASCRIPT' and course != 'JAVA' and course != 'PYTHON' and course != '':
                    course = unidecode.unidecode(input("Our school provides only the following courses:\nPython, C#, Javascript and Java. Course: ")).upper()
                if course == '':
                    random_courses = ['DZONGKHA', 'YUE', 'TUVALUAN']
                    random.shuffle(random_courses)
                    course = random.choice(random_courses)
                course2 = unidecode.unidecode(input("Does the student attend another course? Y or N? ")).upper()
                if course2 == 'Y':
                    newcourse = unidecode.unidecode(input("Our school provides the following courses:Python, C#, Javascript and Java.\nCourse:")).upper() 
                    while newcourse != 'C#' and newcourse != 'JAVASCRIPT' and newcourse != 'JAVA' and newcourse != 'PYTHON' and newcourse != '':
                        newcourse = unidecode.unidecode(input("Our school provides only the following courses:\nPython, C#, Javascript and Java. Course: ")).upper()
                    if newcourse == '':
                        random_courses = ['DZONGKHA', 'YUE', 'TUVALUAN']
                        random.shuffle(random_courses)
                        newcourse = random.choice(random_courses)
                    students_courses = course + ', '+ newcourse
                    print()
                    print('Thank you! The form has been submitted successfully.')
                    print('----------------------------------------------------')
                    print()
                    new_student = {"Code": code, "First Name": first_name, "Last Name": last_name, "Date of Birth": date_of_birth, "Tuition Fees": fees, "Course(s)": students_courses}
                    newlist = Students.add_students(Students.view_students2(), new_student)
                    newcomer = {"Code": code, "First Name": first_name, "Last Name": last_name}
                    newlist2 = Students.add_students(Students.view_students3(), newcomer)
                    print('Here\'s the new student that will be added in the upcomimg days.\nThis student belongs to more than one courses.')
                    print(newlist)
                    print()
                    print(newlist2)
                    print()
                    print("After the secretary's authorization, your information will be published\non our website within three working days. If you find out any mistakes,\nplease email us at infoprivateschool@gmail.com as soon as possible.")
                else:
                    print('Thank you! The form has been submitted successfully.')
                    print('----------------------------------------------------')
                    print()
                    new_student = {"Code": code, "First Name": first_name, "Last Name": last_name, "Date of Birth": date_of_birth, "Tuition Fees": fees, "Course(s)": course}
                    newlist = Students.add_students(Students.view_students2(), new_student)
                    print('Here\'s the new student that will be added in the upcomimg days.')
                    print(newlist)
                    print()
                    print("After the secretary's authorization, your information will be published\non our website within three working days. If you find out any mistakes,\nplease email us at infoprivateschool@gmail.com as soon as possible.")
