from interface import Interface

def run():
    program = Interface()
    program.playlist_menu()
    program.get_choice()
    program.handleChoice()


run()