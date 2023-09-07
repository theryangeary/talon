from talon import Context,Module, noise, actions

ctx = Context()
mod = Module()

ctx.matches = r"""
mode: sleep
"""


@ctx.action("user.noise_trigger_pop")
def on_pop():
    """wake up on pop if sleeping"""
    if not actions.speech.enabled():
        actions.speech.enable()
