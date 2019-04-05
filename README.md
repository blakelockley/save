# Save

Save is basic script to automatically manage 'DEV commits'. 'DEV commits' are intended to be temporary WIP commits to push code to an intermediate remote repo.

The current use case in this instance is that a shared Linux box is used for testing that contains the intermediate repo. Using 'save' development work can be done locally in an IDE and automatically pushed to the remote repo on the box. 

DEV commits are specified by the commit message starting with the word 'DEV' in capitals followed by the date and time of the commit.

The script follows to paths of action:
- If the previous commit was **not** a DEV commit, a new DEV commit is created.
- If the previous commit was a DEV commit, the previous commit is amended, this prevents bloating of continuous commits.

Once a commit is finalised in the traditional sense, the current DEV commit can be amended. Save will create a new DEV commit moving forward.

**Save is not intended to be used to push to shared remote repos!**

## Usage

1. Add the 'save' folder to your path.

2. Run `save` from your current project directory.

## Useful Git Commands

Stage all files of the current DEV commit:
```
git reset --soft HEAD^
```
    
Convert current DEV commit to an actual commit:
```
git commit --amend -m <message>
git push -f
```
