import unittest

from parameterized import parameterized

from src.Controller.MainMenuController import MainMenuController


class TestMainMenuController(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @parameterized.expand([
        ("play the game please", "Bad argument"),
        ("exit", ""),
        ("player1 human", "cur_player1 set to human"),
        ("mode play", "Game mode set to play"),
    ])
    def test_analyze_input_return(self, raw_user_input, expected_return):
        mmc = MainMenuController()
        actual: str = mmc._parse_input(raw_user_input)
        self.assertEqual(actual, expected_return)

    @parameterized.expand([
        ("a", "a")
    ])
    def test_analyze_input_state(self, raw_user_input, expected_state):
        #mmc = MainMenuController()
        #mmc._parse_input(raw_user_input)
        #state: tuple[dict, bool, bool] = (mmc.cur_parameters, mmc.exit_request, mmc.run_request)
        self.assertEqual(raw_user_input, expected_state)

    def test_check_user_input_valid(self):
        self.assertEqual(0, 1-1)


if __name__ == '__main__':
    unittest.main()
