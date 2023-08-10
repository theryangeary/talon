from talon import Context, actions

ctx = Context()

ctx.matches = r"""
os: mac
tag: browser
app: firefox
"""


@ctx.action_class("app")
class AppActions:
    # talon app actions
    def tab_previous():
        actions.key("ctrl-pageup")

    def tab_next():
        actions.key("ctrl-pagedown")
