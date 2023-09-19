from talon import Context,Module, noise, actions

ctx = Context()
mod = Module()

@ctx.action("user.noise_trigger_pop")
def on_pop():
    """repeat on pop"""
    actions.core.repeat_command(1)
