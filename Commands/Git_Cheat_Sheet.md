# Getting Started with Git-


- `𝗴𝗶𝘁 𝗶𝗻𝗶𝘁` : This is the very first command you'll need to use when starting a new project. It initializes a new Git repository in your current directory.

- `𝗴𝗶𝘁 𝗰𝗹𝗼𝗻𝗲 <𝗿𝗲𝗽𝗼>` : To work on an existing project, you'll want to clone (copy) it to your local machine. This command does that.
___

### 𝗠𝗮𝗸𝗲 𝗖𝗵𝗮𝗻𝗴𝗲𝘀

- `𝗴𝗶𝘁 𝘀𝘁𝗮𝘁𝘂𝘀` : Before making or after making changes, it's good practice to check the status of your files. This command will show you any changes that are currently unstaged.

- `𝗴𝗶𝘁 𝗮𝗱𝗱 <𝗳𝗶𝗹𝗲𝗻𝗮𝗺𝗲>` : After you've made some changes to your files, you'll want to stage them for a commit. This command adds a specific file to the stage.

- `𝗴𝗶𝘁 𝗮𝗱𝗱 . 𝗼𝗿 𝗴𝗶𝘁 𝗮𝗱𝗱 -𝗔` : Instead of adding files one by one, you can add all your changed files to the stage with one command.

- `𝗴𝗶𝘁 𝗰𝗼𝗺𝗺𝗶𝘁 -𝗺 "𝗖𝗼𝗺𝗺𝗶𝘁 𝗺𝗲𝘀𝘀𝗮𝗴𝗲"` : Now that your changes are staged, you can commit them with a descriptive message.
___

### 𝗕𝗿𝗮𝗻𝗰𝗵𝗶𝗻𝗴

- `𝗴𝗶𝘁 𝗯𝗿𝗮𝗻𝗰𝗵` : This command will list all the local branches in your current repository.

- `𝗴𝗶𝘁 𝗯𝗿𝗮𝗻𝗰𝗵 <𝗯𝗿𝗮𝗻𝗰𝗵𝗻𝗮𝗺𝗲>` : This command creates a new branch.

- `𝗴𝗶𝘁 𝗰𝗵𝗲𝗰𝗸𝗼𝘂𝘁 <𝗯𝗿𝗮𝗻𝗰𝗵𝗻𝗮𝗺𝗲>` : If you want to switch to a different branch, use this command.

- `𝗴𝗶𝘁 𝗺𝗲𝗿𝗴𝗲 <𝗯𝗿𝗮𝗻𝗰𝗵𝗻𝗮𝗺𝗲>` : Once you've finished making changes in a branch, you'll want to bring those changes into your main branch (usually master). This command does that.
___

### 𝗥𝗲𝗺𝗼𝘁𝗲 𝗥𝗲𝗽𝗼𝘀𝗶𝘁𝗼𝗿𝗶𝗲𝘀

- `𝗴𝗶𝘁 𝗽𝘂𝘀𝗵 𝗼𝗿𝗶𝗴𝗶𝗻 <𝗯𝗿𝗮𝗻𝗰𝗵𝗻𝗮𝗺𝗲>` : This command sends your commits to the remote repository.

- `𝗴𝗶𝘁 𝗽𝘂𝗹𝗹` : If other people are also working on your project, you'll want to keep your local repo up-to-date with their changes. This command fetches and merges any changes from the remote repository.

- `𝗴𝗶𝘁 𝗿𝗲𝗺𝗼𝘁𝗲 -𝘃` : To check which remote servers are connected with your local repository.
___

### 𝗞𝗲𝘆 𝗗𝗶𝗳𝗳𝗲𝗿𝗲𝗻𝗰𝗲𝘀

- `𝗴𝗶𝘁 𝗳𝗲𝘁𝗰𝗵 𝘃𝘀 𝗴𝗶𝘁 𝗽𝘂𝗹𝗹`: Both download data from a remote repository. However, git fetch just downloads it without integrating it, while git pull also merges it into your local files.

- `𝗴𝗶𝘁 𝗺𝗲𝗿𝗴𝗲 𝘃𝘀 𝗴𝗶𝘁 𝗿𝗲𝗯𝗮𝘀𝗲`: Both incorporate changes from one branch to another. git merge combines the source and target branches via a new commit, whereas git rebase moves or combines commits to a new base, making a cleaner history.

- `𝗴𝗶𝘁 𝗿𝗲𝘀𝗲𝘁 𝘃𝘀 𝗴𝗶𝘁 𝗿𝗲𝘃𝗲𝗿𝘁`: Both are used to undo changes. git reset discards local changes completely, while git revert undoes public changes by creating a new reversing commit, thereby preserving history.
___

Git is an extremely powerful tool with plenty more commands and options.

However, this guide gives you a good start and reference point as you continue to explore and leverage Git for your version control needs.



___

# More Git Commands


- git checkout main
- git pull
- git checkout <branch>
- git merge main

- git add .
- git commit -m ""
- git push origin <branch>

___


*hard to change initial settings once the first migration is made*
- Don’t make migrations until at Auth_user part

___

### pipenv install 
	to have same environment

### git checkout  setup 
	move branches

### git fetch 
	updates branch names

### git status
	view status

### git branch
	to see what branches you have

### git remote -v
	see link to push

### git stash 
	temporary save what you’re doing in branch so you can switch

### git stash apply 
	apply stashed save

### git checkout -b [name][initials to id] 
	create new branch

### git log --oneline 
	view log of commit history with id

___

### git reset —hard origin/main
	Make changes go away and make yours look like git hub

### git clean -xdf
	Delete files in directory
