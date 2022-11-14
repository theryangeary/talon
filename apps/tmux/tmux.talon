tag: user.tmux
-
tag(): user.splits

# pane management - these commands use the word split to match with the splits
# tag defined in tags/splits/splits.talon
<<<<<<< HEAD
go split <user.arrow_key>: user.tmux_keybind(arrow_key)
#Say a number after this command to switch to pane
go split: user.tmux_execute_command("display-panes -d 0")
=======
split move <user.arrow_key>: user.do_tmux_keybind(arrow_key)
#Say a number after this command to switch to pane
go split: user.execute_tmux_command("display-panes -d 0")

>>>>>>> 6ab2eef (fix go split command)
