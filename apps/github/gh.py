import re
from talon import Context, Module, actions
import subprocess

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

@mod.action_class
class Actions:
    def gh_command(command: str):
        """execute gh command"""
        out=subprocess.check_output(f"/opt/homebrew/bin/gh {command}", stderr=subprocess.STDOUT, shell=True)
        print(out)

    def submit_queue(command: str):
        """send submit queue command""" 

    def approve_pull_request():
        """approve pull request"""

@ctx.action_class("user")
class Actions:
    def submit_queue(command: str):
        url=actions.browser.address()
        if not url or not url.startswith("https://github.com/lyft/"):
            return
        actions.user.gh_command(f"pr comment {url} --body \"/{command}\"")


    def approve_pull_request():
        url=actions.browser.address()
        if not url or not url.startswith("https://github.com/lyft/"):
            return
        actions.user.gh_command(f"pr review {url} --approve")
