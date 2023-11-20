import time
import unittest

class menu:
    # Метод запуску програми
    def doje_(self, n):
        print("Care to make an order?\n1 - Yes\n2 - No")
        if n == "YES":
            print("Alright, lets continue.")
            self.select_menu()  # Call select_menu method
        elif n == "NO":
            print("As you desire, see you next time.")
            return 0
        else:
            print("Invalid input... try again.")
            return 0

    def select_menu(self):
        #m = input(" What kind of meal you want? \n Desserts\n Drinks\n Pizzas\n Salads\n")
        print("What kind of meal you want? \n Desserts\n Drinks\n Pizzas\n Salads\n")
        m="Salads"
        if m == "Desserts":
            print("You have chosen Desserts")
            time.sleep(5)
        elif m == "Drinks":
            print("You have chosen Drinks")
            time.sleep(5)
        elif m == "Pizzas":
            print("You have chosen Pizzas")
            time.sleep(5)
        elif m == "Salads":
            print("You have chosen Salads")
            time.sleep(5)
        else:
            print("There is an input error... try again.")
            return 0

class TestMenu(unittest.TestCase):
    def test_starting_option(self):
        menu().doje_("YES")

if __name__ == '__main__':
    unittest.main()
#test