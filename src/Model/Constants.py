from typing import Literal


ControllerInstruction = Literal["run", "exit", "main_menu"]

AgentType = Literal["random", "human"]
AgentTypes: list[AgentType] = ["random", "human"]

GameMode = Literal["train", "play", "compare"]
GameModes: list[GameMode] = ["train", "play", "compare"]
