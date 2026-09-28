from commands import execute_command

print("========== BEASTAG ==========")

while True:

    command = input("Enter your command: ")

    if command.lower() == "exit":
        print("Goodbye!")
        break

    execute_command(command)

