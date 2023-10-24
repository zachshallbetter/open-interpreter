
from typing import Dict, Any

class UserProfile:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.history = [] # list of previous interactions
        self.preferences = {} # user's preferences
        self.user_specific_phrases = [] # record of user-specific phrases

    def update_history(self, interaction: str):
        self.history.append(interaction)

    def update_preferences(self, preferences: Dict[str, Any]):
        self.preferences.update(preferences)

    def add_user_phrase(self, phrase: str):
        self.user_specific_phrases.append(phrase)
