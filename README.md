# testyboi: For testing how to use git and github

## Git commands

https://git-scm.com/docs - List of common commands and syntax

https://ndpsoftware.com/git-cheatsheet.html#loc=index; - Cool interactive visualization of how the commands all interact

https://training.github.com/downloads/github-git-cheat-sheet/ - GitHub official cheat sheet with more a smaller set of common commands and explanations

Additionally, you can type --help at the end of any command to bring up docs for that command

## Step 0 - Giting Git

Install git if you haven't already.

https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

This link shows how to install git depending on your OS. There are many options, and even some GUI versions (also there under downloads and GUI clients on the left) that make things more convenient. Additionally, some IDEs and text editors alos have git support in the application itself, which is also quite easy (I know from experience VS-Code and Atom both have really nice git integrations). Also, you'll obviously need a github account.

## Step 1 - Forking

First you should fork this repo onto your own account. You can do this on github by clicking the 'fork' button on the top right. This will add a copy of this repo (specifically the branch you're on, which should be 'main') to your personal github account. If you didn't fork, when you clone, modify, then push changes later on you would be pushing those changes to the same repo as the original, and if you don't have permission to modify that repo (like this case), you wouldn't be able to push the changes upstream. Forking allows you to copy the cody to your own repo and modify it however you like there, and later on you can make a 'pull request' to merge your fork with the original and the owner of the original can look over your PR and decided to allow the merge or not.

## Step 2 - Cloning

After forking this repo, now we need to clone it onto your machine. Cloning is when you download a repo onto your local machine for editing. You can clone any repo, but as mentioned earlier, you can only push changes to repos and branches where you have permission. To clone the repo, on your machine create a folder for this repo somewhere and navigate to that folder in your terminal. From there, obtain the URL for your fork of the repo on github (like 'https://github.com/kadams66/testyboi') and in your terminal type:
```
git clone <URL>.git .
```
This will copy all the files in that repo into your current folder. The '.' at the end indicates that the clone will place the files into the current directory. Without the '.' it would create a new directory and place the files there.

## Step 3 - Adding, Committing, and Pushing

Now that you have the repo on your local machine, we can begin to mess with the most useful commands in git: add, commit, and push. All three commands are part of the commiting chain. First, open the python script and modify it somehow. Next, save the modification and type:
```
git add -u
```
into the terminal. The '-u' parameter means to update all current tracked files and stage those changes. Alternatively, you could've replaced the '-u' with the name of a file in the current directory, and that would've only stages the changes for that *specific* file. Next, after adding/staging the changes, run:
```
git commit -m '<Message Here>'
```
Replace <Message Here> with the commit message for this commit. This will 'commit' or save all staged changes onto the local copy of your repo (stored elsewhere on your machine), but not to the server version on github. To update the server with these changes, run:
```
git push
```
to push all current commits to the server. Git will figure out all the changes from the server stored files made (based on the commit history) and make those changes there. If there are any conflicts (i.e. someone else pushed changes for the same area of code to you and you hadn't fetched/pulled those changes when you made commits) and git can't figure out how to manage them, it will *probably* complain.
  
One last thing, all three of these are also handled easily by IDEs and editors, which make things very easy as these commands would be by far the most used commands.

## Step 4 - Branching and handling conflicts

Time to get into the tricky stuff. Up until now we have been working in the 'main' branch of the code, which is easy and convenient when you're the only one working in this code base, but if other people are involved or you want to try modifying and implementing something without breaking functionality for something else in the meantime, branching becomes important. In the terminal type:
```
git branch <branch name>
```
and this will create a new branch with the given name. Now, type
```
git branch
```
and this will display all current branches on your repo. You should notice two entries listed: 'main' and the one you just created. Additionally, the 'main' branch will be highlighted, indicating that is the current branch you are working in. To switch to the new branch, type:
```
git checkout <branch name>
```
Checkout will check if the current branch has any unsaved changes that should be committed first, and if not, it will switch to the new branch. if you retype `git branch` the new branch should be highlighted now and 'main' unhighlighted.

Now comes the interesting stuff. Open back up the file from before, make a new change, and stage, commit, and push the changes to the server as before, but under the new branch. UH OH! If things happened correctly, when you tried to push your commits to the server, there should've been an error that pops up saying `fatal: The current branch <branch name> has no upstream branch`. This error is caused by creating the branch only on your local machine. If you created the branch through github instead the upstream branch would be there and whenever you next fetched and pulled you would be able to access the branch on your local machine. But, since we created the branch locally, we need to now tell the server that it needs to also track this branch. Type out:
```
git push --set-upstream origin <branch name>
```
as shown in the error output to tell the server to generate an upstream branch by the same name. After that, the push should've worked successfully, and if you check on github you should see that there are now **2** branches under your repo rather than 1. If you switch to the other branch (click the drop down where it says main) you can see how the files are different under each branch.

Now it's time to mess with pull requests. From the new branch, click the 'Make pull request' button at the top. Since there weren't any changes made to the main branch after modifying the new branch, it should say on the new screen that the branches can be merged without conflict. For now, don't submit the pull request and back out to the previous page. Go back to your terminal and switch back to the main branch using checkout. Open the file and modify **the same line** as what you modified on the branch version (in a way to make a conflict). Add, commit, and push this change to the server. Now, refresh your github page and try to make the pull request again. If the conflict was made correctly, the page should now point out that there will be a conflict with merging this PR. Submit the PR anyway, and open up conflict handle on github. This interactive editor allows you to directly modify the code and shows you what each version specifically had that was conflicting with the other. To finish the merge and handle the conflict, you have to remove all the `<<<<<` markers that indicate where there was a conflict. You can also delete and reorganize lines, or type directly into the file too. After handling the conflict, save the changes in the top right and finish the merge request.

## Step 5 - Fetch and Pull

Since we handled the merge request on github rather than through git on our current machine, our current machine's main branch is outdated. To tell our machine to update, we must first run:
```
git fetch
```
which will tell git to check if anything has changed between the server and our machine's code. Now run:
```
git pull
```
which will 'pull' or download the modified files off of the server onto our machine. Git will try to then merge the server version of the files with your local version accounting for any commits you have made since your last pull. If there are no conflicts, great no issue and the merge happens fine, but if there are conflicts you'll need to handle the conflict. Open the conflicting file in a text editor and you'll notice a similar format as before marking the merge conflicts. To resolve the conflict, delete the `<<<<<` indicators and fix the code accordingly, then commit the changes onto your current branch again. 

And that's it!
