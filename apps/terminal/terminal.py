from talon import app, Module, Context, actions, ui, imgui, settings, app, registry

ctx = Context()
mod = Module()
ctx.matches = r"""
tag: terminal
"""

@mod.action_class
class TerminalActions:
    # implements the function from terminal.talon for shells

    def copy():
        """copy file"""
        actions.insert("cp ")

    def move():
        """move file"""
        actions.insert("mv ")

    def grep():
        """grep file"""
        actions.insert("rg ")

    def ps():
        """ps file"""
        actions.insert("ps aux ")

    def ps_grep():
        """ps_grep file"""
        actions.insert("ps aux | rg ")

    def diff():
        """diff file"""
        actions.insert("diff ")

    def gh():
        """use GitHub cli"""
        actions.insert("gh ")
