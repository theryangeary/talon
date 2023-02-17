app: vim
-
file save: insert(':w\n')

quit: insert(':q')
quit all: insert(':qa')

split left: insert(' wv')
split close: insert(' wc')
window only: insert(' wo')

change inside: insert('ci')

clipboard copy inside dubquote: insert('"+yi"')

file search: insert(' ff')
text search: insert(' fr')

blank below:
    insert('o')
    key(escape)

blank above:
    insert('O')
    key(escape)

config edit: insert(':e ~/.vimrc\n')
config source: insert(':source $MYVIMRC\n')

# golang specific
go alternate: insert(':GoAlternate\n')

buffer list: insert(' bl')

copy lock spec: insert(' dcl')

quick fix next: insert(']q')
quick fix last: insert('[q')
go quick fix <number>: insert(':{number}cc\n')
