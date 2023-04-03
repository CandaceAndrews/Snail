Back-end day #1:

git checkout main
git pull
git checkout <branch>
git merge main

git add .
git commit -m ""
git push origin <branch>


*hard to change initial settings once the first migration is made*
- Don’t make migrations until at Auth_user part
——————————————————————————————————
pipenv install —————> to have same environment

git checkout  setup ——>  move branches

git fetch  ————————> updates branch names

git status ————————> view status

git branch ———————> to see what branches you have

git remote -v —————> see link to push

git stash ———————> temporary save what you’re doing in branch so you can switch

git stash apply ————-> apply stashed save

git checkout -b [name][initials to id] ———> create new branch

git log --oneline -------> view log of commit history with id

* Rm -rf 
(Remove directory)

-----------------------------------

* git reset —hard origin/main
	(Make changes go away and make yours look like git hub)

* git clean -xdf
	(Delete files in directory)

* pipenv install
	(To have same dependencies that the original branch has that you pulled)



DO EACH TIME WHEN YOU PULL GITHUB MAIN:
* Pipenv install
* Python manage.py migrate

----------------------------------

