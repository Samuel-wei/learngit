senmudeMBP:learngit senmu$ git cherry-pick 4c805e2
fatal: bad revision '4c805e2'
senmudeMBP:learngit senmu$ git cherry-pick ae976bf
[dev 83e287e] fix bug 101
 Date: Mon Feb 17 21:55:41 2020 +0800
 1 file changed, 20 insertions(+)
 create mode 100644 readme.txt
senmudeMBP:learngit senmu$ git switch -c feature-vulcan
git: 'switch' is not a git command. See 'git --help'.
senmudeMBP:learngit senmu$ git checkout -b feature-vulcan
M	readme.txt
Switched to a new branch 'feature-vulcan'
senmudeMBP:learngit senmu$ git branch