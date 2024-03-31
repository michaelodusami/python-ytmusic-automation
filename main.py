from interface import Interface
import pyinputplus
def run():
    program = Interface()
    while True:
        program.playlist_menu()
        program.print_quit()
        program.get_choice()
        program.handleChoice()
        choice = pyinputplus.inputChoice(["y", "n"], prompt="Do you want to continue? (y/n) ")
        if choice == "n":
            break  # Exit the loop if user chooses not to continue

run()