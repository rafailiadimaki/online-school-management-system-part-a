#Make sure to run the command pip3 install python-dateutil
class Assignments:
    def view_assignments():        
        collection = input('Which collection do you want to see?\n1.A collection of all the assignments\n2.A collection of all the assignments per course\n3.A collection of all the assignments per student per course\n4.Back\nPlease make your choice: ')
        if collection.isdigit():
            if collection == '1':
                print(Assignments.view_assignments1())
                print()
                Assignments.view_assignments()
            if collection == '2':
                print(Assignments.view_assignments2())
                print()
                Assignments.view_assignments()
            if collection == '3':
                print()
                print(Assignments.view_assignments3())
                print()
                Assignments.view_assignments()
            if collection == '4':
                print()
            if collection != '1' and collection != '2' and collection != '3' and collection != '4':
                print()
                print('Ooops! What you have typed is not a number from 1 to 4. Try again. ;)')
                Assignments.view_assignments()
        elif not collection.isdigit():
            while not collection.isdigit():
                collection = input(f"I didn\'t get that. Please type your numbers in digits: ")
            else:
                if collection == '1':
                    print(Assignments.view_assignments1())
                    print()
                    Assignments.view_assignments()
                if collection == '2':
                    print(Assignments.view_assignments2())
                    print()
                    Assignments.view_assignments()
                if collection == '3':
                    print(Assignments.view_assignments3())
                    print()
                    Assignments.view_assignments()
                if collection == '4':
                    print()
                if collection != '1' and collection != '2' and collection != '3' and collection != '4':
                    print()
                    print('Ooops! What you have typed is not a number from 1 to 4. Try again. ;)')
                    Assignments.view_assignments()
    def view_assignments1():
            print()
            print('----------------------------------------------------')
            print('                        ⓅⓇⒾⓋⒶⓉⒺ  ⓈⒸⒽⓄⓄⓁ                                        ')
            print("Existing assignments are shown below:")
            print()        
            Newassignments = [
                {"Code":"00010","Title": "AN INTRODUCTION TO PYTHON PROGRAMMING LANGUAGE","Description": "FLESH IT OUT WITH MORE DETAILS","Date of Submission":"11/12/2022", "Mark for the Submitted Code":"80","Mark for the Oral Mark":"20"},
                {"Code":"00011","Title": "AN ANALYSIS OF THE C# PROGRAMMING LANGUAGE","Description": "FLESH IT OUT WITH MORE DETAILS","Date of Submission":"11/12/2022", "Mark for the Submitted Code":"70","Mark for the Oral Mark":"30"}
                ]
            return Newassignments
    def view_assignments2():
            print()
            print('----------------------------------------------------')
            print('                        ⓅⓇⒾⓋⒶⓉⒺ  ⓈⒸⒽⓄⓄⓁ                                        ')
            print("Existing assignments are shown below:")
            print()        
            Newassignments = [
                {"Code":"00010","Title": "AN INTRODUCTION TO PYTHON PROGRAMMING LANGUAGE","Description": "FLESH IT OUT WITH MORE DETAILS","Date of Submission":"11/12/2022", "Mark for the Submitted Code":"80","Mark for the Oral Mark":"20", "Course": 'PYTHON'},
                {"Code":"00011","Title": "AN ANALYSIS OF THE C# PROGRAMMING LANGUAGE","Description": "FLESH IT OUT WITH MORE DETAILS","Date of Submission":"11/12/2022", "Mark for the Submitted Code":"70","Mark for the Oral Mark":"30", "Course": 'C#'}
                ]
            return Newassignments
    def view_assignments3():
            print()
            print('----------------------------------------------------')
            print('                        ⓅⓇⒾⓋⒶⓉⒺ  ⓈⒸⒽⓄⓄⓁ                                        ')
            print("Existing assignments are shown below:")
            print()        
            Newassignments = [
                {"Student": "0003 MICHAEL DAWSON","Code":"00010","Title": "AN INTRODUCTION TO PYTHON PROGRAMMING LANGUAGE","Description": "FLESH IT OUT WITH MORE DETAILS","Date of Submission":"11/12/2022", "Mark for the Submitted Code":"80","Mark for the Oral Mark":"20", "Course": 'PYTHON'},
                {"Student": "0004 MARGARET CAMPBELL","Code":"00011","Title": "AN ANALYSIS OF THE C# PROGRAMMING LANGUAGE","Description": "FLESH IT OUT WITH MORE DETAILS","Date of Submission":"11/12/2022", "Mark for the Submitted Code":"70","Mark for the Oral Mark":"30", "Course": 'C#'}
                ]
            return Newassignments
    def add_assignments(list, item):
        import copy
        list.append(item)
        return list
    def new_assignment():
        collection = input('Which collection do you want to update?\n1.A collection of all the assignments\n2.A collection of all the assignments per course\n3.A collection of all the assignments per student per course\n4.Back\nPlease make your choice: ')
        if collection.isdigit():
            if collection == '1':
                Assignments.new_assignment1()
                print()
                Assignments.new_assignment()
            if collection == '2':
                Assignments.new_assignment2()
                print()
                Assignments.new_assignment()
            if collection == '3':
                Assignments.new_assignment3()
                print()
                Assignments.new_assignment()
            if collection == '4':
                print()
            if collection != '1' and collection != '2' and collection != '3' and collection != '4':
                print()
                print('Ooops! What you have typed is not a number from 1 to 4. Try again. ;)')
                Assignments.new_assignment()
        elif not collection.isdigit():
            while not collection.isdigit():
                collection = input(f"I didn\'t get that. Please type your numbers in digits: ")
            else:
                if collection == '1':
                    Assignments.new_assignment1()
                    print()
                    Assignments.new_assignment()
                if collection == '2':
                    Assignments.new_assignment2()
                    print()
                    Assignments.new_assignment()
                if collection == '3':
                    Assignments.new_assignment3()
                    print()
                    Assignments.new_assignment()
                if collection == '4':
                    print()
                if collection != '1' and collection != '2' and collection != '3' and collection != '4':
                    print()
                    print('Ooops! What you have typed is not a number from 1 to 4. Try again. ;)')
                    Assignments.new_assignment()
    def new_assignment1():
        number = input('How many assignments do you want to add? ')
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
                    title=unidecode.unidecode(input("Title: ")).upper()
                    if title == '':
                        import random
                        random_assignment_titles=['A COMPARISON BETWEEN OBJECT-ORIENTED PROGRAMMING AND PROCEDURAL PROGRAMMING', 'AN OVERVIEW OF FOUR PROGRAMMING LANGUAGES', 'EXPLORING THE CAREER OF A COMPUTER PROGRAMMER', 'AN INTRODUCTION TO THE WORK OF COMPUTER PROGRAMMERS', 'THE GREAT DEAL IN TRAINING AND EDUCATION FOR PROGRAMMERS', 'AN ANALYSIS OF THE REQUIREMENTS OF BEING A PROGRAMMER', 'A FOCUS ON THE CAREER OF A SOFTWARE PROGRAMMER', 'AN ANALYSIS OF THE PROFESSION OF A SOFTWARE PROGRAMMER', 'BEING A COMPUTER PROGRAMMER', 'OBJECT-ORIENTED PROGRAMMING', 'PROGRAMMING BEST PRACTICES', 'THE INFLUENCE PYTHON HAS ON THE DEVELOPMENT OF OTHER PROGRAMMING LANGUAGES']
                        random.shuffle(random_assignment_titles)
                        title=random.choice(random_assignment_titles)
                    description = unidecode.unidecode(input("Description: ")).upper()
                    if description == '':
                        description = 'Flesh it out with more details.'.upper()
                    from dateutil.parser import parse
                    try:
                        date_of_submission=parse(input("Date of submission in the format (m-d-y): "))
                    except ValueError:
                        random_dates=['11/12/2022','3/6/2022','12/8/2022','1/1/2022','6/5/2022','7/9/2022','4/6/2022','12/27/2022', '12/26/2022', '5/15/2022']
                        random.shuffle(random_dates)
                        date_of_submission = random.choice(random_dates)     
                        pass
                    else:
                        date_of_submission = date_of_submission.strftime('%m-%d-%Y')
                        pass
                    submitted_code_mark = unidecode.unidecode(input("Mark for the submitted code: ")).upper()
                    if submitted_code_mark == '':
                        submitted_code_mark = '100'
                    if not submitted_code_mark.isdigit():
                        while not submitted_code_mark.isdigit():
                            submitted_code_mark = unidecode.unidecode(input("Please type your numbers in digits.\nMark for the submitted code: ")).upper()
                        else:
                            pass
                    else:
                        pass
                    oral_mark = unidecode.unidecode(input("Mark for the oral mark: ")).upper()
                    if oral_mark == '':
                        random_marks=['10','20','30','40','50','60','70','80']
                        random.shuffle(random_marks)
                        oral_mark = random.choice(random_marks)
                    if not oral_mark.isdigit():
                        while not oral_mark.isdigit():
                            oral_mark = unidecode.unidecode(input("Please type your numbers in digits.\nMark for the oral mark: ")).upper()
                        else:
                            pass
                    else:
                        pass
                    print()
                    print('Thank you! The form has been submitted successfully.')
                    print('----------------------------------------------------')
                    print()
                    new_assignment = {"Code": code,"Title": title,"Description": description,"Date of Submission": date_of_submission, "Mark for the Submitted Code":submitted_code_mark,"Mark for the Oral Mark":oral_mark}
                    newlist = Assignments.add_assignments(Assignments.view_assignments1(), new_assignment)
                    print('Here\'s the new assignment that will be added in the upcomimg days.')
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
                title=unidecode.unidecode(input("Title: ")).upper()
                if title == '':
                    import random
                    random_assignment_titles=['A COMPARISON BETWEEN OBJECT-ORIENTED PROGRAMMING AND PROCEDURAL PROGRAMMING', 'AN OVERVIEW OF FOUR PROGRAMMING LANGUAGES', 'EXPLORING THE CAREER OF A COMPUTER PROGRAMMER', 'AN INTRODUCTION TO THE WORK OF COMPUTER PROGRAMMERS', 'THE GREAT DEAL IN TRAINING AND EDUCATION FOR PROGRAMMERS', 'AN ANALYSIS OF THE REQUIREMENTS OF BEING A PROGRAMMER', 'A FOCUS ON THE CAREER OF A SOFTWARE PROGRAMMER', 'AN ANALYSIS OF THE PROFESSION OF A SOFTWARE PROGRAMMER', 'BEING A COMPUTER PROGRAMMER', 'OBJECT-ORIENTED PROGRAMMING', 'PROGRAMMING BEST PRACTICES', 'THE INFLUENCE PYTHON HAS ON THE DEVELOPMENT OF OTHER PROGRAMMING LANGUAGES']
                    random.shuffle(random_assignment_titles)
                    title=random.choice(random_assignment_titles)
                description = unidecode.unidecode(input("Description: ")).upper()
                if description == '':
                    description = 'Flesh it out with more details.'.upper()
                from dateutil.parser import parse
                try:
                    date_of_submission=parse(input("Date of submission in the format (m-d-y): "))
                except ValueError:
                    random_dates=['11/12/2022','3/6/2022','12/8/2022','1/1/2022','6/5/2022','7/9/2022','4/6/2022','12/27/2022', '12/26/2022', '5/15/2022']
                    random.shuffle(random_dates)
                    date_of_submission = random.choice(random_dates)     
                    pass
                else:
                    date_of_submission = date_of_submission.strftime('%m-%d-%Y')
                    pass
                submitted_code_mark = unidecode.unidecode(input("Mark for the submitted code: ")).upper()
                if submitted_code_mark == '':
                    submitted_code_mark = '100'
                if not submitted_code_mark.isdigit():
                    while not submitted_code_mark.isdigit():
                        submitted_code_mark = unidecode.unidecode(input("Please type your numbers in digits.\nMark for the submitted code: ")).upper()
                    else:
                        pass
                else:
                    pass
                oral_mark = unidecode.unidecode(input("Mark for the oral mark: ")).upper()
                if oral_mark == '':
                    random_marks=['10','20','30','40','50','60','70','80']
                    random.shuffle(random_marks)
                    oral_mark = random.choice(random_marks)
                if not oral_mark.isdigit():
                    while not oral_mark.isdigit():
                        oral_mark = unidecode.unidecode(input("Please type your numbers in digits.\nMark for the oral mark: ")).upper()
                    else:
                        pass
                else:
                    pass
                print()
                print('Thank you! The form has been submitted successfully.')
                print('----------------------------------------------------')
                print()
                new_assignment = {"Code": code,"Title": title,"Description": description,"Date of Submission": date_of_submission, "Mark for the Submitted Code":submitted_code_mark,"Mark for the Oral Mark":oral_mark}
                newlist = Assignments.add_assignments(Assignments.view_assignments1(), new_assignment)
                print('Here\'s the new assignment that will be added in the upcomimg days.')
                print(newlist)
        print()
        print("After the secretary's authorization, your information will be published\non our website within three working days. If you find out any mistakes,\nplease email us at infoprivateschool@gmail.com as soon as possible.")
    def new_assignment2():
        number = input('How many assignments do you want to add? ')
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
                    title=unidecode.unidecode(input("Title: ")).upper()
                    if title == '':
                        import random
                        random_assignment_titles=['A COMPARISON BETWEEN OBJECT-ORIENTED PROGRAMMING AND PROCEDURAL PROGRAMMING', 'AN OVERVIEW OF FOUR PROGRAMMING LANGUAGES', 'EXPLORING THE CAREER OF A COMPUTER PROGRAMMER', 'AN INTRODUCTION TO THE WORK OF COMPUTER PROGRAMMERS', 'THE GREAT DEAL IN TRAINING AND EDUCATION FOR PROGRAMMERS', 'AN ANALYSIS OF THE REQUIREMENTS OF BEING A PROGRAMMER', 'A FOCUS ON THE CAREER OF A SOFTWARE PROGRAMMER', 'AN ANALYSIS OF THE PROFESSION OF A SOFTWARE PROGRAMMER', 'BEING A COMPUTER PROGRAMMER', 'OBJECT-ORIENTED PROGRAMMING', 'PROGRAMMING BEST PRACTICES', 'THE INFLUENCE PYTHON HAS ON THE DEVELOPMENT OF OTHER PROGRAMMING LANGUAGES']
                        random.shuffle(random_assignment_titles)
                        title=random.choice(random_assignment_titles)
                    description = unidecode.unidecode(input("Description: ")).upper()
                    if description == '':
                        description = 'Flesh it out with more details.'.upper()
                    from dateutil.parser import parse
                    try:
                        date_of_submission=parse(input("Date of submission in the format (m-d-y): "))
                    except ValueError:
                        random_dates=['11/12/2022','3/6/2022','12/8/2022','1/1/2022','6/5/2022','7/9/2022','4/6/2022','12/27/2022', '12/26/2022', '5/15/2022']
                        random.shuffle(random_dates)
                        date_of_submission = random.choice(random_dates)     
                        pass
                    else:
                        date_of_submission = date_of_submission.strftime('%m-%d-%Y')
                        pass
                    submitted_code_mark = unidecode.unidecode(input("Mark for the submitted code: ")).upper()
                    if submitted_code_mark == '':
                        submitted_code_mark = '100'
                    if not submitted_code_mark.isdigit():
                        while not submitted_code_mark.isdigit():
                            submitted_code_mark = unidecode.unidecode(input("Please type your numbers in digits.\nMark for the submitted code: ")).upper()
                        else:
                            pass
                    else:
                        pass
                    oral_mark = unidecode.unidecode(input("Mark for the oral mark: ")).upper()
                    if oral_mark == '':
                        random_marks=['10','20','30','40','50','60','70','80']
                        random.shuffle(random_marks)
                        oral_mark = random.choice(random_marks)
                    if not oral_mark.isdigit():
                        while not oral_mark.isdigit():
                            oral_mark = unidecode.unidecode(input("Please type your numbers in digits.\nMark for the oral mark: ")).upper()
                        else:
                            pass
                    else:
                        pass
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
                    new_assignment = {"Code": code,"Title": title,"Description": description,"Date of Submission": date_of_submission, "Mark for the Submitted Code":submitted_code_mark,"Mark for the Oral Mark":oral_mark,"Course": course}
                    newlist = Assignments.add_assignments(Assignments.view_assignments2(), new_assignment)
                    print('Here\'s the new assignment that will be added in the upcomimg days.')
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
                title=unidecode.unidecode(input("Title: ")).upper()
                if title == '':
                    import random
                    random_assignment_titles=['A COMPARISON BETWEEN OBJECT-ORIENTED PROGRAMMING AND PROCEDURAL PROGRAMMING', 'AN OVERVIEW OF FOUR PROGRAMMING LANGUAGES', 'EXPLORING THE CAREER OF A COMPUTER PROGRAMMER', 'AN INTRODUCTION TO THE WORK OF COMPUTER PROGRAMMERS', 'THE GREAT DEAL IN TRAINING AND EDUCATION FOR PROGRAMMERS', 'AN ANALYSIS OF THE REQUIREMENTS OF BEING A PROGRAMMER', 'A FOCUS ON THE CAREER OF A SOFTWARE PROGRAMMER', 'AN ANALYSIS OF THE PROFESSION OF A SOFTWARE PROGRAMMER', 'BEING A COMPUTER PROGRAMMER', 'OBJECT-ORIENTED PROGRAMMING', 'PROGRAMMING BEST PRACTICES', 'THE INFLUENCE PYTHON HAS ON THE DEVELOPMENT OF OTHER PROGRAMMING LANGUAGES']
                    random.shuffle(random_assignment_titles)
                    title=random.choice(random_assignment_titles)
                description = unidecode.unidecode(input("Description: ")).upper()
                if description == '':
                    description = 'Flesh it out with more details.'.upper()
                from dateutil.parser import parse
                try:
                    date_of_submission=parse(input("Date of submission in the format (m-d-y): "))
                except ValueError:
                    random_dates=['11/12/2022','3/6/2022','12/8/2022','1/1/2022','6/5/2022','7/9/2022','4/6/2022','12/27/2022', '12/26/2022', '5/15/2022']
                    random.shuffle(random_dates)
                    date_of_submission = random.choice(random_dates)     
                    pass
                else:
                    date_of_submission = date_of_submission.strftime('%m-%d-%Y')
                    pass
                submitted_code_mark = unidecode.unidecode(input("Mark for the submitted code: ")).upper()
                if submitted_code_mark == '':
                    submitted_code_mark = '100'
                if not submitted_code_mark.isdigit():
                    while not submitted_code_mark.isdigit():
                        submitted_code_mark = unidecode.unidecode(input("Please type your numbers in digits.\nMark for the submitted code: ")).upper()
                    else:
                        pass
                else:
                    pass
                oral_mark = unidecode.unidecode(input("Mark for the oral mark: ")).upper()
                if oral_mark == '':
                    random_marks=['10','20','30','40','50','60','70','80']
                    random.shuffle(random_marks)
                    oral_mark = random.choice(random_marks)
                if not oral_mark.isdigit():
                    while not oral_mark.isdigit():
                        oral_mark = unidecode.unidecode(input("Please type your numbers in digits.\nMark for the oral mark: ")).upper()
                    else:
                        pass
                else:
                    pass
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
                new_assignment = {"Code": code,"Title": title,"Description": description,"Date of Submission": date_of_submission, "Mark for the Submitted Code":submitted_code_mark,"Mark for the Oral Mark":oral_mark,"Course": course}
                newlist = Assignments.add_assignments(Assignments.view_assignments2(), new_assignment)
                print('Here\'s the new assignment that will be added in the upcomimg days.')
                print(newlist)
        print()
        print("After the secretary's authorization, your information will be published\non our website within three working days. If you find out any mistakes,\nplease email us at infoprivateschool@gmail.com as soon as possible.")
    def new_assignment3():
        number = input('How many assignments do you want to add? ')
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
                    course= unidecode.unidecode(input("Our school provides the following courses:Python, C#, Javascript and Java.\nCourse:")).upper() 
                    while course != 'C#' and course != 'JAVASCRIPT' and course != 'JAVA' and course != 'PYTHON' and course != '':
                        course = unidecode.unidecode(input("Our school provides only the following courses:\nPython, C#, Javascript and Java. Course: ")).upper()
                    if course == '':
                        random_courses = ['DZONGKHA', 'YUE', 'TUVALUAN']
                        random.shuffle(random_courses)
                        course = random.choice(random_courses)
                    code=''.join([str(elem) for elem in code])
                    student = input('These are our students:\n1. 0006 James Jason\n2. 0007 Veronica Robinson\n3. 0008 Valentino Bandera\n4. 0009 Nicole Klein\nWho is it for? ')
                    while student != '1' and student != '2' and student != '3' and student != '4' and student != '':
                        input('I didn\'t get that. Please type your numbers in digits: ')
                    else:
                        if student == '1':
                            student = '0006 JAMES JASON'
                        if student == '2':
                            student = '0007 VERONICA ROBINSON'
                        if student == '3':
                            student = '0008 VALENTINO BANDERA'
                        if student == '4':
                            student = '0009 NICOLE KLEIN'
                        if student == '':
                            import random
                            random_students = ['0010 QUELLA WAHLE', '0010 BILL SMITH', '0011 YAHIR ZAHN']
                            random.shuffle(random_students)
                            student = random.choice(random_students)                        
                    title=unidecode.unidecode(input("Title: ")).upper()
                    if title == '':
                        import random
                        random_assignment_titles=['A COMPARISON BETWEEN OBJECT-ORIENTED PROGRAMMING AND PROCEDURAL PROGRAMMING', 'AN OVERVIEW OF FOUR PROGRAMMING LANGUAGES', 'EXPLORING THE CAREER OF A COMPUTER PROGRAMMER', 'AN INTRODUCTION TO THE WORK OF COMPUTER PROGRAMMERS', 'THE GREAT DEAL IN TRAINING AND EDUCATION FOR PROGRAMMERS', 'AN ANALYSIS OF THE REQUIREMENTS OF BEING A PROGRAMMER', 'A FOCUS ON THE CAREER OF A SOFTWARE PROGRAMMER', 'AN ANALYSIS OF THE PROFESSION OF A SOFTWARE PROGRAMMER', 'BEING A COMPUTER PROGRAMMER', 'OBJECT-ORIENTED PROGRAMMING', 'PROGRAMMING BEST PRACTICES', 'THE INFLUENCE PYTHON HAS ON THE DEVELOPMENT OF OTHER PROGRAMMING LANGUAGES']
                        random.shuffle(random_assignment_titles)
                        title=random.choice(random_assignment_titles)
                    description = unidecode.unidecode(input("Description: ")).upper()
                    if description == '':
                        description = 'Flesh it out with more details.'.upper()
                    from dateutil.parser import parse
                    try:
                        date_of_submission=parse(input("Date of submission in the format (m-d-y): "))
                    except ValueError:
                        random_dates=['11/12/2022','3/6/2022','12/8/2022','1/1/2022','6/5/2022','7/9/2022','4/6/2022','12/27/2022', '12/26/2022', '5/15/2022']
                        random.shuffle(random_dates)
                        date_of_submission = random.choice(random_dates)     
                        pass
                    else:
                        date_of_submission = date_of_submission.strftime('%m-%d-%Y')
                        pass
                    submitted_code_mark = unidecode.unidecode(input("Mark for the submitted code: ")).upper()
                    if submitted_code_mark == '':
                        submitted_code_mark = '100'
                    if not submitted_code_mark.isdigit():
                        while not submitted_code_mark.isdigit():
                            submitted_code_mark = unidecode.unidecode(input("Please type your numbers in digits.\nMark for the submitted code: ")).upper()
                        else:
                            pass
                    else:
                        pass
                    oral_mark = unidecode.unidecode(input("Mark for the oral mark: ")).upper()
                    if oral_mark == '':
                        random_marks=['10','20','30','40','50','60','70','80']
                        random.shuffle(random_marks)
                        oral_mark = random.choice(random_marks)
                    if not oral_mark.isdigit():
                        while not oral_mark.isdigit():
                            oral_mark = unidecode.unidecode(input("Please type your numbers in digits.\nMark for the oral mark: ")).upper()
                        else:
                            pass
                    else:
                        pass
                    print()
                    print('Thank you! The form has been submitted successfully.')
                    print('----------------------------------------------------')
                    print()
                    new_assignment = {"Student": student,"Code": code,"Title": title,"Description": description,"Date of Submission": date_of_submission, "Mark for the Submitted Code":submitted_code_mark,"Mark for the Oral Mark":oral_mark,"Course": course}
                    newlist = Assignments.add_assignments(Assignments.view_assignments3(), new_assignment)
                    print('Here\'s the new assignment that will be added in the upcomimg days.')
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
                course= unidecode.unidecode(input("Our school provides the following courses:Python, C#, Javascript and Java.\nCourse:")).upper() 
                while course != 'C#' and course != 'JAVASCRIPT' and course != 'JAVA' and course != 'PYTHON' and course != '':
                    course = unidecode.unidecode(input("Our school provides only the following courses:\nPython, C#, Javascript and Java. Course: ")).upper()
                if course == '':
                    random_courses = ['DZONGKHA', 'YUE', 'TUVALUAN']
                    random.shuffle(random_courses)
                    course = random.choice(random_courses)
                code=''.join([str(elem) for elem in code])
                student = input('These are our students:\n1. 0006 James Jason\n2. 0007 Veronica Robinson\n3. 0008 Valentino Bandera\n4. 0009 Nicole Klein\nWho is it for? ')
                while student != '1' and student != '2' and student != '3' and student != '4' and student != '':
                    input('I didn\'t get that. Please type your numbers in digits: ')
                else:
                    if student == '1':
                        student = '0006 JAMES JASON'
                    if student == '2':
                        student = '0007 VERONICA ROBINSON'
                    if student == '3':
                        student = '0008 VALENTINO BANDERA'
                    if student == '4':
                        student = '0009 NICOLE KLEIN'
                    if student == '':
                        import random
                        random_students = ['0010 QUELLA WAHLE', '0010 BILL SMITH', '0011 YAHIR ZAHN']
                        random.shuffle(random_students)
                        student = random.choice(random_students)                        
                title=unidecode.unidecode(input("Title: ")).upper()
                if title == '':
                    import random
                    random_assignment_titles=['A COMPARISON BETWEEN OBJECT-ORIENTED PROGRAMMING AND PROCEDURAL PROGRAMMING', 'AN OVERVIEW OF FOUR PROGRAMMING LANGUAGES', 'EXPLORING THE CAREER OF A COMPUTER PROGRAMMER', 'AN INTRODUCTION TO THE WORK OF COMPUTER PROGRAMMERS', 'THE GREAT DEAL IN TRAINING AND EDUCATION FOR PROGRAMMERS', 'AN ANALYSIS OF THE REQUIREMENTS OF BEING A PROGRAMMER', 'A FOCUS ON THE CAREER OF A SOFTWARE PROGRAMMER', 'AN ANALYSIS OF THE PROFESSION OF A SOFTWARE PROGRAMMER', 'BEING A COMPUTER PROGRAMMER', 'OBJECT-ORIENTED PROGRAMMING', 'PROGRAMMING BEST PRACTICES', 'THE INFLUENCE PYTHON HAS ON THE DEVELOPMENT OF OTHER PROGRAMMING LANGUAGES']
                    random.shuffle(random_assignment_titles)
                    title=random.choice(random_assignment_titles)
                description = unidecode.unidecode(input("Description: ")).upper()
                if description == '':
                    description = 'Flesh it out with more details.'.upper()
                from dateutil.parser import parse
                try:
                    date_of_submission=parse(input("Date of submission in the format (m-d-y): "))
                except ValueError:
                    random_dates=['11/12/2022','3/6/2022','12/8/2022','1/1/2022','6/5/2022','7/9/2022','4/6/2022','12/27/2022', '12/26/2022', '5/15/2022']
                    random.shuffle(random_dates)
                    date_of_submission = random.choice(random_dates)     
                    pass
                else:
                    date_of_submission = date_of_submission.strftime('%m-%d-%Y')
                    pass
                submitted_code_mark = unidecode.unidecode(input("Mark for the submitted code: ")).upper()
                if submitted_code_mark == '':
                    submitted_code_mark = '100'
                if not submitted_code_mark.isdigit():
                    while not submitted_code_mark.isdigit():
                        submitted_code_mark = unidecode.unidecode(input("Please type your numbers in digits.\nMark for the submitted code: ")).upper()
                    else:
                        pass
                else:
                    pass
                oral_mark = unidecode.unidecode(input("Mark for the oral mark: ")).upper()
                if oral_mark == '':
                    random_marks=['10','20','30','40','50','60','70','80']
                    random.shuffle(random_marks)
                    oral_mark = random.choice(random_marks)
                if not oral_mark.isdigit():
                    while not oral_mark.isdigit():
                        oral_mark = unidecode.unidecode(input("Please type your numbers in digits.\nMark for the oral mark: ")).upper()
                    else:
                        pass
                else:
                    pass
                print()
                print('Thank you! The form has been submitted successfully.')
                print('----------------------------------------------------')
                print()
                new_assignment = {"Student": student,"Code": code,"Title": title,"Description": description,"Date of Submission": date_of_submission, "Mark for the Submitted Code":submitted_code_mark,"Mark for the Oral Mark":oral_mark,"Course": course}
                newlist = Assignments.add_assignments(Assignments.view_assignments3(), new_assignment)
                print('Here\'s the new assignment that will be added in the upcomimg days.')
                print(newlist)
        print()
        print("After the secretary's authorization, your information will be published\non our website within three working days. If you find out any mistakes,\nplease email us at infoprivateschool@gmail.com as soon as possible.")