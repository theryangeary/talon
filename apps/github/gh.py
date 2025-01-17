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

mod.list("git_command", desc="Git commands.")
mod.list("git_argument", desc="Command-line git options and arguments.")

dirpath = Path(__file__).parent
github_users_csv_path = str(dirpath / "github_users.csv")

ctx = Context()
ctx.matches = r"""
app: github
"""

github_users = get_list_from_csv(
    "github_users.csv",
    headers=("handle", "spoken"),
)

mod.list("github_users", desc="GitHub user names")
ctx.lists["self.github_users"] = github_users

@mod.action_class
class Actions:
    def gh_command(command: str):
        """execute gh command"""
        try:
            out = subprocess.check_output(f"/opt/homebrew/bin/gh {command}", stderr=subprocess.STDOUT, shell=True)
            actions.app.notify("GitHub", f"submitted `{command}`")
            return out
        except subprocess.CalledProcessError as e:
            actions.app.notify("GitHub", f"failed to submit `{command}`. Check logs for details.")
            print(e)

    def submit_queue(command: str):
        """send submit queue command""" 

    def approve_pull_request():
        """approve pull request"""


@mod.capture(rule="{self.github_users}+")
def github_users(m) -> str:
    "One or more GitHub user names"
    return " ".join(m.github_users_list)
