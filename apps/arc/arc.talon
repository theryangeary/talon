app: arc
-
tag(): browser
tag(): user.tabs
tag(): user.splits

(our | arc | R) command [<user.text>]: user.arc_command(text or "", false)
(our | arc | R) space [<user.text>]: user.arc_command("focus on {text}", true)
(our | arc | R) space next: key(cmd-alt-right)
(our | arc | R) space previous: key(cmd-alt-left)

bar toggle: key(cmd-s)

tab commit: key(cmd-o)
tab pin: key(cmd-d)

