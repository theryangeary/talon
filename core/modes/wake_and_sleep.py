from talon import Context, Module, actions

mod = Module()

@mod.action_class
class KeyActions:
    def toggle_speech():
        """toggle speech on and off"""
        if not actions.speech.enabled():
            actions.speech.enable()
        else:
            actions.speech.disable()
