from src.Model.Constants import GameMode, GameModes


class MainMenuView:
    """
        View for main menu screen (game mode and agents selection)
    """
    def __init__(self):
        self.menu_template: str = """
* UNO AI *

Available agents:
{avail_agents}

Game modes:
{game_modes}

Current selection:
{cur_players}
 - Game mode: {cur_game_mode}

 
Input instructions: <run | [[player[1|2|3] | mode] [<player/agent> | <game-mode>]] | exit>
Feedback: {feedback}
 > """

    def display_menu(self, available_agent_names: list[str], cur_players: list[str], cur_game_mode: GameMode, feedback: str) -> str:
        return input(self._format_menu(available_agent_names, cur_players, cur_game_mode, feedback))

    def _format_menu(self, available_agent_names: list[str], cur_players: list[str], cur_game_mode: str, feedback: str) -> str:
        # Display available agents
        available_agents_str: str = str()
        for agent in available_agent_names:
            available_agents_str += " - {}\n".format(agent)

        # Display game modes
        game_modes_str: str = str()
        for game_mode in GameModes:
            game_modes_str += " - {}\n".format(game_mode if game_mode != str() else "-")

        # Select players/agents
        cur_players_str = str()
        for n, player in enumerate(cur_players):
            cur_players_str + " - Player {}: {}\n".format(n + 1, player if player != str() else "No player")

        # Feedback
        feedback = "/" if feedback == str() else feedback

        return self.menu_template.format(avail_agents=available_agents_str, game_modes=game_modes_str, cur_players=cur_players, cur_game_mode=cur_game_mode, feedback=feedback)
