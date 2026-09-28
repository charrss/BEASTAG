from automation import open_chrome

def execute_command(command):

    if command.lower() == "open chrome":
        print("Opening Chrome...")
        open_chrome()

    else:
        print("Sorry, I don't understand that command.")