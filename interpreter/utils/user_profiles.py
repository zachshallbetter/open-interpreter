
from typing import Dict, Any
import datetime


class UserProfile:
    """
    UserProfile object maintains the data related to a user.
    It includes user_id, interaction history, preferences, user specific phrases and habits related data.
    """

    def __init__(self, user_id: str):
        """
        Creates a new UserProfile instance.
        Args:
        user_id (str): ID to uniquely identify the user
        """
        self.user_id = user_id  # uniquely identifies the user
        self.history = []  # to keep track of user interactions
        self.preferences = {}  # to store user-specific preferences
        self.user_specific_phrases = []  # record of user-specific phrases

        # Habit tracking fields
        self.frequent_commands = {}  # to store frequent commands by the user
        self.activity_time = []  # store the active hours of the user
        self.language_preference = ''  # store the language preference of the user

    def update_history(self, interaction: str):
        """
        Updates the interaction history.
        Args:
        interaction (str): interaction string to be appended in the history.
        """
        self.history.append(interaction)  # Update history after each interaction

    def update_user_preferences_bulk(self, preferences: Dict[str, Any]):
        """
        Bulk update of user preferences.
        Args:
        preferences (str, Any): Dictionary of preference key-value pairs.
        """
        self.preferences.update(preferences)  # bulk update of user preferences

    def update_user_preferences(self, preference: str, value: str):
        """
        Adds new preference or update an existing preference of the user.
        Args:
        preference (str): preference to add/update
        value (str): preference value
        """
         
        self.preferences[preference] = value  # add new preference or update existing one

    def get_user_preference(self, preference: str):
        """
        Returns the value of a specific preference.
        Args:
        preference (str): preference to fetch the value of.
        Returns:
        The prefernce value if exists, else None.
        """
        return self.preferences.get(preference)  # get the value of a specific preference

    def get_all_preferences(self):
        """
        Returns all user preferences.
        Returns:
        The dictionary containing all preferences.
        """
        return self.preferences  # get all user preferences

    def add_user_phrase(self, phrase: str):
        """
        Records a user-specific phrase.
        Args:
        phrase (str): phrase to be added.
        """
        self.user_specific_phrases.append(phrase)  # record a user-specific phrase

    def show_history(self):
        """
        Returns the history of all user interactions.
        Returns:
        List with all user interactions history.
        """
        return self.history  # Get the history of all user interactions


    # Habit tracking methods
    def update_frequent_commands(self, command: str):
        """
        Updates the frequency of a command.
        If command exists in frequent_commands, its count is increased by one
        If command does not exist in frequent_commands, it is added with count of 1
        Args:
        command (str): command to be updated.
        """
        if command in self.frequent_commands:
            self.frequent_commands[command] += 1
        else:
            self.frequent_commands[command] = 1
    
    def update_activity_time(self):
        """
        Updates the activity time.
        Appends the current hour to activity_time.
        """
        self.activity_time.append(datetime.datetime.now().hour)
    
    def set_language_preference(self, language: str):
        """
        Sets the language preference.
        Args:
        language (str): preferred language for user
        """
        self.language_preference = language
