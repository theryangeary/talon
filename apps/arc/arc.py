from talon import Context, Module, actions, app

ctx = Context()
mod = Module()
apps = mod.apps
apps.arc = "app.name: Arc"
apps.arc = "app.name: arc"

apps.arc = """
os: mac
and app.bundle: company.thebrowser.Browser
"""



# Make the context match more specifically than anything else. This is important, eg. to
# override the browser.go_home() implementation in tags/browser/browser_mac.py.
ctx.matches = r"""
os: windows
os: linux
os: mac
tag: browser
app: arc
"""


@mod.action_class
class Actions:
    def arc_command(command: str, enter: bool = True):
        """perform command"""


@ctx.action_class("user")
class UserActions:
    def tab_close_wrapper():
        actions.sleep("180ms")
        actions.app.tab_close()



@ctx.action_class("browser")
class BrowserActions:
    def focus_page():
        actions.browser.focus_address()
        actions.edit.find()
        actions.sleep("180ms")
        actions.key("escape")

    def go_home():
        actions.key("alt-home")
