from talon import Context, actions
from talon.mac import applescript

ctx = Context()

ctx.matches = r"""
os: mac
tag: browser
app: Arc
"""

@ctx.action_class("browser")
class BrowserActions:
    def address():
        address = applescript.run(
            """
            tell application id "{bundle}"
                return the URL of the active tab of the front window
            end tell""".format(
                bundle=actions.app.bundle()
            )
        )  
        return address

@ctx.action_class("user")
class UserActions:
    def arc_command(command: str, enter: bool = True):
        actions.key("cmd-t")
        actions.insert(command)
        if enter:
            actions.key("enter")

@ctx.action_class("app")
class AppActions:
    def tab_previous():
        actions.key("cmd-alt-up")

    def tab_next():
        actions.key("cmd-alt-down")

@ctx.action_class("user")
class UserActions:
    def split_window_vertically():
        actions.key("ctrl-shift-plus")

    def split_clear():
        actions.key("ctrl-shift-minus")



@ctx.action_class("browser")
class BrowserActions:
    def bookmarks():
        actions.key("cmd-shift-o")

    def open_private_window():
        actions.key("cmd-shift-p")

    def show_downloads():
        actions.key("cmd-j")

    def show_extensions():
        actions.key("cmd-shift-a")
