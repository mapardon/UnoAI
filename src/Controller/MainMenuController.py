import os
from argparse import ArgumentError

from src.Model.Constants import AgentTypes, GameModes, ControllerInstruction
from src.View.MainMenuView import MainMenuView
from src.db.DbUtils import retrieve_agent_names
from src.util.utils import CLEAR_SCREEN_CMD


class MainMenuController:
    """
        Controller for main menu screen (game mode and agents selection)
    """
    def __init__(self):
        self.cur_parameters: dict = {"cur_game_mode": str(), "cur_player1": str(),
                                     "cur_player2": str(), "cur_player3": str()}
        self.view: MainMenuView = MainMenuView()
        self.exit_request: bool = False
        self.run_request: bool = False

    def run_main_menu(self) -> ControllerInstruction:
        """
            Run a loop displaying the main menu and analyzing received input
        """

        raw_user_input: str
        feedback: str = str()
        available_agent_names: list[str] = retrieve_agent_names() + AgentTypes

        while not (self.exit_request or self.run_request):
            os.system(CLEAR_SCREEN_CMD)
            raw_user_input = self.view.display_menu(available_agent_names, [self.cur_parameters["cur_player1"],
                                                                                      self.cur_parameters["cur_player2"],
                                                                                      self.cur_parameters["cur_player3"]],
                                                    self.cur_parameters["cur_game_mode"], feedback)
            feedback = self._analyze_input(raw_user_input)

        return "exit" if self.exit_request else self.run_request

    def _analyze_input(self, raw_user_input: str) -> str:
        """
            Analyze and process user input.

        :param raw_user_input: Commandline user typed input
        :return: Feedback to display on user interface
        """

        split_input: list
        command: str
        arg: str
        input_ok: bool
        feedback: str = "Bad argument"

        try:
            if ' ' in raw_user_input:
                split_input = raw_user_input.split(' ')
                if len(split_input) == 2:
                    command, arg = split_input
                else:
                    raise ArgumentError
            else:
                command, arg =  raw_user_input, str()

            input_ok, feedback = self._check_user_input_valid(command, arg)
            if not input_ok:
                    raise ArgumentError
        except Exception:
            return feedback

        if "player" in command:
            self.cur_parameters["cur_" + command] = arg
            feedback = "{} set to {}".format("cur_" + command, arg)
        elif command == "mode":
            self.cur_parameters["cur_game_mode"] = arg
            feedback = "Game mode set to {}".format(arg)
        elif command == "run":
            self.run_request = True
            feedback = str()
        elif command == "exit":
            self.exit_request = True
            feedback = str()
        else:
            raise AssertionError("Shouldn't have landed here")

        return feedback

    def _check_user_input_valid(self, command: str, arg: str) -> tuple[bool, str]:
        """
            Check if user provided input corresponds to a command of the program

        :param command: instruction requested by the user
        :param arg: argument completing the instruction, possibly empty
        :return: boolean indicating if the input corresponds to a command of the program & a feedback related to the
            verification of the input
        """

        sentinel: bool
        feedback: str = str()

        # Command is player selection
        if "player" in command:
            sentinel = command in ["player1", "player2", "player3"] and arg in retrieve_agent_names() + AgentTypes
            if not sentinel:
                feedback = "Unknown player"
            else:
                sentinel = not (arg == "human" and self.cur_parameters["cur_game_mode"] != "play")
                if not sentinel:
                    feedback = "Human cannot be selected for train and compare modes"

        # Command is game mode selection
        elif command == "mode":
            sentinel = arg in GameModes
            if not sentinel:
                feedback = "Unknown game mode"
            else:
                sentinel = not (arg in ["train", "compare"] and "human" in self.cur_parameters.values())
                if not sentinel:
                    feedback = "Human cannot be selected for train and compare modes"

        # Command is run (parameters must be complete to launch game)
        elif command == "run":
            sentinel = None not in self.cur_parameters.values()
            if not sentinel:
                feedback = "Missing parameters to run game"

        # Command is exit (nothing special)
        elif command == "exit":
            sentinel = True
            feedback = str()

        # Something else (input is not correct)
        else:
            sentinel = False
            feedback = "Bad input"

        return sentinel, feedback
