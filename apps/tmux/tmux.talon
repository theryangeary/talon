tag: user.tmux
-
tag(): user.splits

# pane management - these commands use the word split to match with the splits
# tag defined in tags/splits/splits.talon
split move <user.arrow_key>: user.do_tmux_keybind(arrow_key)
+#Say a number after this command to switch to pane
+go split: user.execute_tmux_command("display-panes -d 0")
