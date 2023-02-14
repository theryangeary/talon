app: dlv
tag: terminal
-

rebuild: insert('rebuild\n')
reload: insert('r\n')
continue: insert('c\n')
break clipboard:
    insert('b ')
    edit.paste()
    insert('\n')
breakpoints: "bp\n"
clear: "clear "
clear <number>: "clear {number}\n"
next: insert('n\n')
step in: insert('s\n')
step out: insert('so\n')
print: "p "
display add: "display -a "
display delete: "display -d "
display delete <number>: "display -d {number}\n"
