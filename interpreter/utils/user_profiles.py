
from typing import Dict, Any
import datetime

class UserProfile:
    def __init__(self, user_id: str):
        self.user_id = user_id  # uniquely identifies the user
        self.history = []  # to keep track of user interactions
        self.preferences = {}  # to store user-specific preferences
        self.user_specific_phrases = []  # record of user-specific phrases

        # Habit tracking fields
        self.frequent_commands = {}  # to store frequent commands by the user
        self.activity_time = []  # store the active hours of the user
        self.language_preference = ''  # store the language preference of the user

    def update_history(self, interaction: str):
        self.history.append(interaction)  # Update history after each interaction

    def update_user_preferences_bulk(self, preferences: Dict[str, Any]):
        self.preferences.update(preferences)  # bulk update of user preferences

    def update_user_preferences(self, preference: str, value: str):
        self.preferences[preference] = value  # add new preference or update existing one

    def get_user_preference(self, preference: str):
        return self.preferences.get(preference)  # get the value of a specific preference

    def get_all_preferences(self):
        return self.preferences  # get all user preferences

    def add_user_phrase(self, phrase: str):
        self.user_specific_phrases.append(phrase)  # record a user-specific phrase

    def show_history(self):
        return self.history  # Get the history of all user interactions

    # Habit tracking methods
    def update_frequent_commands(self, command: str):
        if command in self.frequent_commands:
            self.frequent_commands[command] += 1
        else:
            self.frequent_commands[command] = 1

    def update_activity_time(self):
        self.activity_time.append(datetime.datetime.now().hour)

    def set_language_preference(self, language: str):
        self.language_preference = language
