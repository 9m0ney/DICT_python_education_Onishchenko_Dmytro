class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.money = 550
        self.state = "choosing_action"

    def process_input(self, user_input):
        if self.state == "choosing_action":
            self.handle_action(user_input)
        elif self.state == "choosing_coffee":
            self.handle_coffee_choice(user_input)
        elif self.state == "filling_water":
            self.handle_filling(user_input, "water")
        elif self.state == "filling_milk":
            self.handle_filling(user_input, "milk")
        elif self.state == "filling_beans":
            self.handle_filling(user_input, "coffee_beans")
        elif self.state == "filling_cups":
            self.handle_filling(user_input, "cups")

    def handle_action(self, action):
        if action == "buy":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            self.state = "choosing_coffee"
        elif action == "fill":
            print("Write how many ml of water you want to add:")
            self.state = "filling_water"
        elif action == "take":
            self.take_money()
            self.state = "choosing_action"
        elif action == "remaining":
            self.print_status()
            self.state = "choosing_action"
        elif action == "exit":
            exit()

    def handle_coffee_choice(self, choice):
        if choice == "back":
            self.state = "choosing_action"
            return

        try:
            coffee_type = int(choice)
        except ValueError:
            self.state = "choosing_action"
            return

        if coffee_type == 1:  # espresso
            self.make_coffee(250, 0, 16, 4)
        elif coffee_type == 2:  # latte
            self.make_coffee(350, 75, 20, 7)
        elif coffee_type == 3:  # cappuccino
            self.make_coffee(200, 100, 12, 6)

        self.state = "choosing_action"

    def make_coffee(self, water_needed, milk_needed, beans_needed, cost):
        if self.water < water_needed:
            print("Sorry, not enough water!")
            return
        if self.milk < milk_needed:
            print("Sorry, not enough milk!")
            return
        if self.coffee_beans < beans_needed:
            print("Sorry, not enough coffee beans!")
            return
        if self.cups < 1:
            print("Sorry, not enough disposable cups!")
            return

        print("I have enough resources, making you a coffee!")
        self.water -= water_needed
        self.milk -= milk_needed
        self.coffee_beans -= beans_needed
        self.cups -= 1
        self.money += cost

    def handle_filling(self, amount, resource):
        try:
            amount = int(amount)
        except ValueError:
            self.state = "choosing_action"
            return

        if resource == "water":
            self.water += amount
            print("Write how many ml of milk you want to add:")
            self.state = "filling_milk"
        elif resource == "milk":
            self.milk += amount
            print("Write how many grams of coffee beans you want to add:")
            self.state = "filling_beans"
        elif resource == "coffee_beans":
            self.coffee_beans += amount
            print("Write how many disposable cups you want to add:")
            self.state = "filling_cups"
        elif resource == "cups":
            self.cups += amount
            self.state = "choosing_action"

    def take_money(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def print_status(self):
        print("\nThe coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee_beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"${self.money} of money\n")


def main():
    machine = CoffeeMachine()

    while True:
        try:
            if machine.state == "choosing_action":
                print("Write action (buy, fill, take, remaining, exit):")

            user_input = input().strip().lower()
            machine.process_input(user_input)
        except KeyboardInterrupt:
            print("\nProgram interrupted by user")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break


if __name__ == "__main__":
    main()