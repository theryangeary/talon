# requires gh utility to be installed
tag: browser
browser.host: github.com
app: github
-

submit queue test: user.submit_queue("test")
submit queue merge: user.submit_queue("merge")
submit queue merge skip checks: user.submit_queue("merge-skip-checks")
submit queue retest: user.submit_queue("retest")
submit queue rebase: user.submit_queue("rebase")
submit queue revert: user.submit_queue("revert")
submit queue lock: user.submit_queue("lock")
submit queue unlock: user.submit_queue("unlock")
submit queue offload: user.submit_queue("offload")
submit queue PTAL <user.github_users>: user.submit_queue("ptal {github_users}")

pull request approve: user.approve_pull_request()
