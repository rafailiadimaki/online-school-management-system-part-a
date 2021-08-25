class Courses:
    def view_courses():
            print()
            print('---------------------------------------------------------------')
            print('                        ⓅⓇⒾⓋⒶⓉⒺ  ⓈⒸⒽⓄⓄⓁ                                        ')
            print("Existing courses are shown below:")
            print()        
            NewCourses = [
                {"Code": "1000","Course Title": "CB13FTPY","Course Language":"PYTHON","Course Description": "PYTHON 12 WEEKS", "Course Type": "FULL TIME"},
                {"Code": "1001","Course Title": "CB13PTPY","Course Language":"PYTHON","Course Description": "PYTHON 24 WEEKS", "Course Type": "PART TIME"}
                ]
            return NewCourses
    def add_courses(list, item):
        import copy
        list.append(item)
        return list
    def new_course():
        number = input('How many courses do you want to add? ')
        if not number.isdigit():
            while not number.isdigit():
                number = input(f"I didn\'t get that. Please type your numbers in digits: ")
            else:
                import sys
                for i in range(int(number)):
                    import unidecode
                    print()
                    print('Our school provides the following courses:Python, C#, Javascript and Java.')
                    print()
                    print('Please fill out every field in the form, and then press ENTER. For dummy data, leave the fields empty.')
                    import random
                    random_identifiers = list(range(1003,9999))
                    random.shuffle(random_identifiers)
                    code = random.sample(random_identifiers, 1)
                    code = ' '.join([str(elem) for elem in code])
                    c_language = unidecode.unidecode(input("Language: ")).upper() 
                    while c_language != 'C#' and c_language != 'JAVASCRIPT' and c_language != 'JAVA' and c_language != 'PYTHON' and c_language != '':
                        c_language = unidecode.unidecode(input("Our school provides only the following courses:\nPython, C#, Javascript and Java. Language: ")).upper()
                    if c_language == '':
                        random_languages = ['Dzongkha', 'Yue', 'Tuvaluan']
                        random.shuffle(random_languages)
                        c_language = random.choice(random_languages)
                    c_type = unidecode.unidecode(input("You can choose among two options: Full time, part time.\nType: ")).upper()
                    while c_type != 'FULL TIME' and c_type != 'PART TIME' and c_type != '':
                        c_type = unidecode.unidecode(input("You can choose among only two options: Full time and part time.\nType: ")).upper()
                    if c_type == '':
                        random_types = ['FULL TIME', 'PART TIME']
                        random.shuffle(random_types)
                        c_type = random.choice(random_types)
                        
                    if c_language == 'Dzongkha' or c_language == 'Yue' or c_language == 'Tuvaluan':
                        c_description = '-'
                        random_titles=['XYZ', 'ABC', 'KLM']
                        random.shuffle(random_titles)
                        c_title = random.choice(random_titles)
                        
                    if c_language == 'PYTHON' and c_type == 'FULL TIME':
                        c_description = 'PYTHON 12 WEEKS'
                        c_title = 'CB13FTPY'
                        
                    if c_language == 'PYTHON' and c_type == 'PART TIME':
                        c_description = 'PYTHON 24 WEEKS'
                        c_title = 'CB13PTPY'
                        
                    if c_language == 'C#' and c_type == 'FULL TIME':
                        c_title = 'CB13FTC'
                        c_description = 'C# 12 WEEKS'

                    if c_language == 'C#' and c_type == 'PART TIME':
                        c_title = 'CB13PTC'
                        c_description = 'C# 24 WEEKS'

                    if c_language == 'JAVA' and c_type == 'FULL TIME':
                        c_title = 'CB13FTJV'
                        c_description = 'JAVA 12 WEEKS'

                    if c_language == 'JAVA' and c_type == 'PART TIME':
                        c_title = 'CB13PTJV'
                        c_description = 'JAVA 24 WEEKS'

                    if c_language == 'JAVASCRIPT' and c_type == 'FULL TIME':
                        c_title = 'CB13FTJS'
                        c_description = 'JAVASCRIPT 12 WEEKS'

                    if c_language == 'JAVASCRIPT' and c_type == 'PART TIME':
                        c_title = 'CB13PTJS'
                        c_description = 'JAVASCRIPT 24 WEEKS'
                    print()
                    print('Thank you! The form has been submitted successfully.')
                    print('----------------------------------------------------')
                    print()
                    new_course = {"Code": code, "Course Title": c_title, "Course Language": c_language, "Course Description": c_description, "Course Type": c_type}
                    newlist = Courses.add_courses(Courses.view_courses(), new_course)
                    print('Here\'s the new course that will be added in the upcomimg days.')
                    print(newlist) 
        else:
            import sys
            for i in range(int(number)):
                import unidecode
                print()
                print('Our school provides the following courses:Python, C#, Javascript and Java.')
                print()
                print('Please fill out every field in the form, and then press ENTER. For dummy data, leave the fields empty.')
                import random
                random_identifiers = list(range(1003,9999))
                random.shuffle(random_identifiers)
                code = random.sample(random_identifiers, 1)
                code = ' '.join([str(elem) for elem in code])
                c_language = unidecode.unidecode(input("Language: ")).upper()
                if c_language=='C':
                    c_language='C#' 
                while c_language != 'C#' and c_language != 'JAVASCRIPT' and c_language != 'JAVA' and c_language != 'PYTHON' and c_language != '':
                    c_language = unidecode.unidecode(input("Our school provides only the following courses:\nPython, C#, Javascript and Java. Language: ")).upper()
                if c_language == '':
                    random_languages = ['Dzongkha', 'Yue', 'Tuvaluan']
                    random.shuffle(random_languages)
                    c_language = random.choice(random_languages)
                c_type = unidecode.unidecode(input("You can choose among two options: Full time, part time.\nType: ")).upper()
                while c_type != 'FULL TIME' and c_type != 'PART TIME' and c_type != '':
                    c_type = unidecode.unidecode(input("You can choose among only two options: Full time and part time.\nType: ")).upper()
                if c_type == '':
                    random_types = ['FULL TIME', 'PART TIME']
                    random.shuffle(random_types)
                    c_type = random.choice(random_types)
                    
                if c_language == 'Dzongkha' or c_language == 'Yue' or c_language == 'Tuvaluan':
                    c_description = '-'
                    random_titles=['XYZ', 'ABC', 'KLM']
                    random.shuffle(random_titles)
                    c_title = random.choice(random_titles)
                    
                if c_language == 'PYTHON' and c_type == 'FULL TIME':
                    c_description = 'PYTHON 12 WEEKS'
                    c_title = 'CB13FTPY'
                    
                if c_language == 'PYTHON' and c_type == 'PART TIME':
                    c_description = 'PYTHON 24 WEEKS'
                    c_title = 'CB13PTPY'
                    
                if c_language == 'C#' and c_type == 'FULL TIME':
                    c_title = 'CB13FTC'
                    c_description = 'C# 12 WEEKS'

                if c_language == 'C#' and c_type == 'PART TIME':
                    c_title = 'CB13PTC'
                    c_description = 'C# 24 WEEKS'

                if c_language == 'JAVA' and c_type == 'FULL TIME':
                    c_title = 'CB13FTJV'
                    c_description = 'JAVA 12 WEEKS'

                if c_language == 'JAVA' and c_type == 'PART TIME':
                    c_title = 'CB13PTJV'
                    c_description = 'JAVA 24 WEEKS'

                if c_language == 'JAVASCRIPT' and c_type == 'FULL TIME':
                    c_title = 'CB13FTJS'
                    c_description = 'JAVASCRIPT 12 WEEKS'

                if c_language == 'JAVASCRIPT' and c_type == 'PART TIME':
                    c_title = 'CB13PTJS'
                    c_description = 'JAVASCRIPT 24 WEEKS'
                print()
                print('Thank you! The form has been submitted successfully.')
                print('----------------------------------------------------')
                print()
                new_course = {"Code": code, "Course Title": c_title, "Course Language": c_language, "Course Description": c_description, "Course Type": c_type}
                newlist = Courses.add_courses(Courses.view_courses(), new_course)
                print('Here\'s the new course that will be added in the upcomimg days.')
                print(newlist)
        print()
        print("After the secretary's authorization, your information will be published\non our website within three working days. If you find out any mistakes,\nplease email us at infoprivateschool@gmail.com as soon as possible.")