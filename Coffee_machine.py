game_is_on = True

Bank = 0

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
	"water": 300,
	"milk": 200,
	"coffee": 100,
}
resources["money"] = 0.00

"""THOSE ARE RESOURCES THAT U HAVE TO SUBTRACT FROM U HAVE VARIABLE NAMES TOO ALREADY"""

water_ml = resources["water"]
milk_ml = resources["milk"]
coffe_g = resources["coffee"]
bank = resources["money"]








# TODO n1 : print report
# TODO n2 : check resources sufficient ?
# TODO n3 : process coins
# TODO n4 : check transaction successful
# TODO n5 : Make Coffe


while game_is_on:

	choices = input("What would you like espresso/latte/cappuccino").lower()
	if choices == "report".lower():
		ingredients = list(resources.items())
		print(ingredients[0][0], ":", water_ml, "ml")
		print(ingredients[1][0], ":", milk_ml, "ml")
		print(ingredients[2][0], ":", coffe_g, "g")
		print(ingredients[3][0], ":", bank, "$$$")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ ESPRESSO ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	elif choices == "espresso".lower():

		print("Please insert coins")
		quarters = int(input("How many quarters?: "))
		dimes = int(input("How many dimes?: "))
		nickles = int(input("How many nickles?: "))
		pennies = int(input("How many pennies?: "))

		quarters = quarters * 0.25
		dimes = dimes * 0.10
		nickles = nickles * 0.05
		pennies = pennies * 0.01

		money_inputed = (quarters + dimes + nickles + pennies)

		# ESPRESSO RECOURCES REQUIRMENTS

		to_pay1 = MENU["espresso"]["ingredients"]["water"]
		to_pay2 = MENU["espresso"]["ingredients"]["coffee"]

		cost_of_drink = MENU["espresso"]["cost"]

		# checks if there is enough resources in the coffe machine
		if cost_of_drink > money_inputed:
			print("That's not enough money ")
		elif water_ml < to_pay1 and coffe_g < to_pay2:
			print("There is not enough water and coffee")
		elif water_ml < to_pay1:
			print("There is not enough water\n")
		elif coffe_g < to_pay2:
			print("There is not enough coffee\n")
		elif water_ml > to_pay1 and coffe_g > to_pay2:

			change = money_inputed - cost_of_drink
			rounded_change = round(change, 3)

			water_ml -= to_pay1
			coffe_g -= to_pay2
			bank += cost_of_drink
			print(f"Here is your espresso ☕ Enjoy here is your change {rounded_change}")
# ~~~~~~~~~~~~~~~~~~~~~~~ LATTE ~~~~~~~~~~~~~~~~~~~~~~
	elif choices == "latte".lower():

		print("Please insert coins")
		quarters = int(input("How many quarters?: "))
		dimes = int(input("How many dimes?: "))
		nickles = int(input("How many nickles?: "))
		pennies = int(input("How many pennies?: "))

		quarters = quarters * 0.25
		dimes = dimes * 0.10
		nickles = nickles * 0.05
		pennies = pennies * 0.01

		money_inputed = (quarters + dimes + nickles + pennies)

		# LATTE RECOURSES req

		to_pay1 = MENU["latte"]["ingredients"]["water"]
		to_pay2 = MENU["latte"]["ingredients"]["milk"]
		to_pay3 = MENU["latte"]["ingredients"]["coffee"]

		cost_of_drink = MENU["latte"]["cost"]

		# checks if there is enough resources in the coffe machine
		if cost_of_drink > money_inputed:
			print("That's not enough money ")
		elif water_ml < to_pay1 and coffe_g < to_pay2 and milk_ml < to_pay3:
			print("There is not enough water and coffee & milk")
		elif water_ml < to_pay1 and milk_ml < to_pay2:
			print("There is not enough water and milk")
		elif water_ml < to_pay1:
			print("There is not enough water\n")
		elif milk_ml < to_pay2:
			print("There is not enough milk")
		elif coffe_g < to_pay3:
			print("There is not enough coffee\n")
		elif water_ml > to_pay1 and milk_ml > to_pay2 and coffe_g > to_pay3:

			change = money_inputed - cost_of_drink
			rounded_change = round(change, 3)

			water_ml -= to_pay1
			coffe_g -= to_pay3
			milk_ml -= to_pay2
			bank += cost_of_drink
			print(f"Here is your latte ☕ Enjoy here is your change {rounded_change}")
# ############################### CAPPUCCINO ###################################
	elif choices == "cappuccino".lower():

		print("Please insert coins")
		quarters = int(input("How many quarters?: "))
		dimes = int(input("How many dimes?: "))
		nickles = int(input("How many nickles?: "))
		pennies = int(input("How many pennies?: "))

		quarters = quarters * 0.25
		dimes = dimes * 0.10
		nickles = nickles * 0.05
		pennies = pennies * 0.01

		money_inputed = (quarters + dimes + nickles + pennies)

		# LATTE RECOURSES req

		to_pay1 = MENU["cappuccino"]["ingredients"]["water"]
		to_pay2 = MENU["cappuccino"]["ingredients"]["milk"]
		to_pay3 = MENU["cappuccino"]["ingredients"]["coffee"]

		cost_of_drink = MENU["cappuccino"]["cost"]

		# checks if there is enough resources in the coffe machine
		if cost_of_drink > money_inputed:
			print("That's not enough money ")
		elif water_ml < to_pay1 and coffe_g < to_pay2 and milk_ml < to_pay3:
			print("There is not enough water and coffee & milk")
		elif water_ml < to_pay1 and milk_ml < to_pay2:
			print("There is not enough water and milk")
		elif water_ml < to_pay1:
			print("There is not enough water\n")
		elif milk_ml < to_pay2:
			print("There is not enough milk")
		elif coffe_g < to_pay3:
			print("There is not enough coffee\n")
		elif water_ml > to_pay1 and milk_ml > to_pay2 and coffe_g > to_pay3:

			change = money_inputed - cost_of_drink
			rounded_change = round(change, 3)

			water_ml -= to_pay1
			coffe_g -= to_pay3
			milk_ml -= to_pay2
			bank += cost_of_drink
			print(f"Here is your cappuccino ☕ Enjoy here is your change {rounded_change}")

	else:
		print("We only offer latte cappuccino & espresso , sorry :( ")







