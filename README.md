# git Merge Conflicts

How to not be afraid of merge conflicts

## Why do merge conflicts happen?

Merge conflicts happen when trying to merge a branch into another one, and git doesn't know which changes to use in the merged version. The main reasons (and only ones I'm familiar with) this could happen are:

1. When two commits, in different branches, have changes to the same file, specifically, to the same line
2. When a commit has files that have been deleted from the repo in another commit

## Before solving merge conflicts

One super important thing to note is that merge conflicts can only be solved locally, with our current Azure DevOps stack. Other things like GitHub or Gitlab have GUI tools to help solve merge conflicts in the remote repo.

One quick refesher before solving merge conflicts. Remember that there are, basically, three stages files can be in a git repo:

* workspace/working directory: the current state of your git files
* staging area: once changes are flagged as ready to be submitted to the history (result of `git add`)
* repo: history of all registered changes (result of `git commit`)

The current (most times "latest") commit in the "repo" stage for the current branch is also known as `HEAD`. Note that if you change branches, then `HEAD` might be a different commit.

## How to solve merge conflicts?

Suppose you've implemented a feature in your version of the `main` branch, and are ready to push. But when trying to push your change you get a scary message:

```
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'some remote repo'
```

This message only means that the changes in one of your commits, include changes to the same file/line that was already changed by another commit and pushed previously. The thing is that you don't have that change in your version of the repo. To get those changes let's do the responsible thing and do a `git fetch`, and a `git status` to look at where we're at.

```
On branch main
Your branch and 'origin/main' have diverged,
and have 1 and 1 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)
```

Let's follow git's instructions, lets do a pull, but with an extra flag to tell git we want to merge the changes.

```
$ git pull --no-rebase

Auto-merging some_file.py
CONFLICT (content): Merge conflict in some_file.py
Automatic merge failed; fix conflicts and the commit the result.
```

> **NOTE:** There's more than one way to get to this point (when git indicates that there's a conflict), the important thing about solving merge conflicts comes after we get to this point, then it's always the same steps.

Let's type `git status` to get some info on our situation.

```
On branch main
Your branch and 'origin/main' have diverged,
and have 1 and 1 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)

You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
	both modified:   some_file.py
```

Now you manually have to pick the change that you want to keep in order to solve the merge conflict. You can do this in any text editor. The beginning of a merge conflict section is specified by:

```
<<<<<<< HEAD
```

The end of a merge conflict section is specified by:

```
>>>>>>> {some commit hash}
```

And the different versions are separated by:

```
=======
```

A complete merge conflict section looks something like this:

```
<<<<<<< HEAD
current commit
=======
Conflicting version in the target branch
>>>>>>> 4d7764dfbe0b173f997a64a3d52b07693d9da068
```

You choose manually which section of the code gets to be commited as the "official version" by deleting the other one. After you've chosen the right version, commit the change and try to push again.

Congrats! you've solved a merge conflict! 🎉

## Final notes

Solving merge conflicts mean to choose one of the conflicting changes over the other one. This might not alwas be what we want. Some times those merge coflics come from new features being implemented, we wouldn't want to loose a prevously implemented feature. In those cases rebasing might be the thing we actually want.
