from commands import execute_command
from ai import ask_ai, understand_command

print("========== BEASTAG ==========")

while True:

    command = input("BEASTAG > ")

    if command.lower() == "exit":
        print("Goodbye!")
        break

    response = execute_command(command)
  
    if response == "Sorry, I don't understand that command.":

        ai_command = understand_command(command)

        if ai_command != "none":
            response = execute_command(ai_command)
        else:
            response = ask_ai(command)

    print(response)