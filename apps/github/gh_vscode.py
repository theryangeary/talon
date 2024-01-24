import re
from pathlib import Path
from talon import Context, Module, actions
import subprocess
from ...core.user_settings import get_list_from_csv


mod = Module()
apps=mod.apps
apps.github = """
title: /Pull Request #[0-9]+/
app: vscode
"""

ctx = Context()
ctx.matches = r"""
app: github
"""

def get_pull_request_number():
    title = ui.active_window().title
    return re.search(r"#(\d+)", title).group(1)

@ctx.action_class("user")
class Actions:
    def submit_queue(command: str):
        # TODO
        pr_number = get_pull_request_number()
        if not pr_number:
            return
        _ = actions.user.gh_command(f"pr comment {pr_number} --body \"/{command}\"")



    def approve_pull_request():
        # TODO
        pass
        #_ = actions.user.gh_command(f"pr review {url} --approve")
