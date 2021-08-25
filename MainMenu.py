class Main_menu:
        #Ask the user to select an option on why they are here. A number from 1 to 6 must be typed in at this point.
        import sys
        print()
        def __init__(self, main_menu):
            self.main_menu = main_menu
        def serve_user(self):
            import subcategories
            import random
            while self.main_menu == '':
                self.main_menu = list(range(1,5))
                random.shuffle(self.main_menu)
                self.main_menu = random.choice(self.main_menu)
                self.main_menu = str(self.main_menu)
                subset = subcategories.subcategories(self.main_menu)
                subset.user_choice()
            while self.main_menu == '1' or self.main_menu == '2' or self.main_menu == '3' or self.main_menu == '4' or self.main_menu == '5':
                subset = subcategories.subcategories(self.main_menu)
                subset.user_choice()
            while self.main_menu != '1' or self.main_menu != '2' or self.main_menu != '3' or self.main_menu != '4' or self.main_menu != '5':
                try:
                    self.main_menu = input(int("No valid number! Please type a digit from 1 to 6: "))
                except:
                    self.main_menu = input(("Whoopsie! Please type a digit from 1 to 5: "))
                    subset = subcategories.subcategories(self.main_menu)
                    subset.user_choice()