from talon import Context, Module, actions

mod = Module()
apps=mod.apps
apps.google_docs = """
tag: browser
browser.host: docs.google.com
"""

ctx = Context()
ctx.matches = r"""
app: google_docs
"""

@ctx.action_class("edit")
class EditActions:
    def paragraph_start():
        actions.edit.extend_paragraph_start()
        actions.edit.left()

    def paragraph_end():
        actions.edit.extend_paragraph_end()
        actions.edit.right()

    def select_paragraph():
        actions.key("ctrl-shift-up")
        actions.key("ctrl-shift-down")

    def extend_paragraph_start():
        actions.key("alt-shift-up")

    def extend_paragraph_end():
        actions.key("alt-shift-down")

    def delete_paragraph():
        actions.edit.select_paragraph()
        actions.edit.delete()