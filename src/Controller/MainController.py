from src.Controller.MainMenuController import MainMenuController
from src.Model.Constants import ControllerInstruction


class MainController:
    def __init__(self):
        self.main_menu_controller = MainMenuController()
        self.GameController = None

    def run(self):
        next_instruction: ControllerInstruction = "main_menu"

        while next_instruction != "exit":

            if next_instruction == "main_menu":
                next_instruction = self.main_menu_controller.run_main_menu()

            elif next_instruction == "run":
                next_instruction = "exit"
