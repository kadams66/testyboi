#   t e s t y b o i : For testing how to use git and github
 
## Git commands
https://git-scm.com/docs

## Step 0 - Giting Good
Install git if you haven't already.
https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
This link shows how to install git depending on your OS. There are many options, and even some GUI versions (also there under downloads and GUI clients on the left) that make things more convenient. Additionally, some IDEs and text editors alos have git support in the application itself, which is also quite easy (I know from experience VS-Code and Atom both have really nice git integrations).
Also you'll obviously need a github account.

## Step 1 -
First you should fork this repo onto your own account. You can do this on github by clicking the 'fork' button on the top right. This will add a copy of this repo (specifically the branch you're on, which should be 'main') to your personal github account. If you didn't fork, when you clone, modify, then push changes later on you would be pushing those changes to the same repo as the original, and if you don't have permission to modify that repo (like this case), you wouldn't be able to push the changes upstream. Forking allows you to copy the cody to your own repo and modify it however you like there, and later on you can make a 'pull request' to merge your fork with the original and the owner of the original can look over your PR and decided to allow the merge or not.

## Step 2
After forking this repo, now we need to clone it onto your machine. Cloning is when you download a repo onto your local machine for editing. You can clone any repo, but as mentioned earlier, you can only push changes to repos and branches where you have permission. To clone the repo, on your machine create a folder for this repo somewhere and navigate to that folder in your terminal. From there, obtain the URL for the repo on github (like 'https://github.com/kadams66/testyboi') and in your terminal type:
`git clone <URL>.git .`
This will copy all the files in that repo into your current folder. The '.' at the end indicates that the clone will place the files into the current directory. Without the '.' it would create a new directory and place the files there.

##Step 3
