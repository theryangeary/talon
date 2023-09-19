# requires gh utility to be installed
tag: browser
browser.host: github.com
-
app: github

submit queue test: user.submit_queue("test")
submit queue merge: user.submit_queue("merge")
submit queue retest: user.submit_queue("retest")
submit queue rebase: user.submit_queue("rebase")
submit queue revert: user.submit_queue("revert")

(submit queue | pull request) approve: user.approve_pull_request()
