
class player:

    # Allow the player to change what icon they want to use
    def __init__(self, icon):
        self.icon = icon

    # Provide input from players
    @staticmethod
    def get_input():
        player_input = str(input())

        return player_input
