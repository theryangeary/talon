#custom vscode commands go here
app: vscode
-

bar [book] marks: user.vscode("workbench.view.extension.bookmarks")
[book] mark next: user.vscode("bookmarks.jumpToNext")
[book] mark [last | prev]: user.vscode("bookmarks.jumpToPrevious")

bar [reference | ref]: user.vscode("workbench.view.extension.references-view")
[reference | ref] next: user.vscode("references-view.next")
[reference | ref] [last | prev]: user.vscode("references-view.prev")

