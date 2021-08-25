'''Be sure to install unidecode: pip install unidecode '''

#Greet the user using their names and display the date and time.
class user:

    #Initialize the object
    def __init__(self,firstname):
        
        self.firstname = firstname.capitalize()

    def greet_user(self):

        #If the user doesn't give a name, call them dear user. 
        if self.firstname == "":
            self.firstname = "dear user"
            
        from datetime import datetime
        
        # Current date and time
        now = datetime.now()
        
        
        # Current hour
        hour= now.strftime('%H')

        # An integer representation of the hour
        hour=int(hour)
        
        
        #  Greetings depending on the time of the day
        if 5<=hour<=11:
            greeting_time='Good morning,'

        elif 12<=hour<=17:
            greeting_time='Good afternoon,'

        elif 18<=hour<=23 or 0<hour<4:
            greeting_time='Good evening,'


        #Greet our user depending on the time of day 
        left=f'{greeting_time} {self.firstname}.'
        

        #Return a left justified version of the string

        x = left.ljust(60)

        #Print two blank lines and the desired message

        print()

        print (x, 'Current date and time : ', now.strftime('%d-%m-%Y %H:%M'))