from automation import open_chrome, open_notepad, open_calculator,open_spotify


commands = {
    "open chrome": open_chrome,
    "launch chrome": open_chrome,
    "start chrome": open_chrome,

    "open notepad": open_notepad,
    "launch notepad": open_notepad,

    "open calculator": open_calculator,
    "launch calculator": open_calculator,

    "open spotify": open_spotify,
    "launch spotify": open_spotify
}


def execute_command(command):

    command = command.strip().lower()

    if command in commands:
        commands[command]()
        return "done"
    else:
        return "Sorry, I don't understand that command."