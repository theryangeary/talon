import re
from pathlib import Path
from talon import Context, Module, actions
import subprocess
from ...core.user_settings import get_list_from_csv


mod = Module()
apps=mod.apps
apps.github = """
tag: browser
browser.host: github.com
"""

ctx = Context()
ctx.matches = r"""
app: github
"""

@ctx.action_class("user")
class Actions:
    def submit_queue(command: str):
        url=actions.browser.address()
        if not url or not url.startswith("https://github.com/lyft/"):
            return
        _ = actions.user.gh_command(f"pr comment {url} --body \"/{command}\"")



    def approve_pull_request():
        url=actions.browser.address()
        if not url or not url.startswith("https://github.com/lyft/"):
            return
        _ = actions.user.gh_command(f"pr review {url} --approve")
