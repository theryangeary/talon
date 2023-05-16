tag: terminal
and not tag: vim
-

clear word left:
    key(ctrl-w)

copy:
    user.copy()
move:
    user.move()
remove: insert("rm ")
cd: insert("cd ")
grep:
    user.grep()
grep list:
    user.grep()
    insert("-l ")
ps:
    user.ps()
ps grep:
    user.ps_grep()
diff: user.diff()
lyft cube: insert("lyftkube ")
