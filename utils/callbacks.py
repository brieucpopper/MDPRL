# -*- coding: utf-8 -*-
"""
Author: John Mansfield
"""


class Callbacks:
    """
    Base class.
    """
    def __init__(self):
        pass

    def on_episode_begin(self, caller):
        print("tst")
        pass

    def on_episode_end(self, caller):
        pass

    def on_episode(self, caller, episode):
        pass

    def on_env_step(self, caller):
        pass


class MyCallbacks(Callbacks):
    """
    To create a callback, override one of the callback functions in the child class MyCallbacks.
    """
    def __init__(self):
        pass

    def on_episode(self, caller, episode):

        if episode % 10000 == 0:
            print(f"Episode: {episode}")

           
        """
        Parameters
        ----------------------------
        caller (RL type): Calling object

        episode {int}: Current episode from caller
        """
        

    def on_episode_begin(self, caller):
        """
        Parameters
        ----------------------------
        caller (RL type): Calling object
        """
        # do things on episode begin
        pass

    def on_episode_end(self, caller):
        """
        Parameters
        ----------------------------
        caller (RL type): Calling object
        """
        # do things on episode end
        pass

    def on_env_step(self, caller):
        """
        Parameters
        ----------------------------
        caller (RL type): Calling object
        """
        # do things on env. step
        pass
    