# create a new branch with name of the date in forma YYYY-MM-DD
# and push it to the remote repository
branch:
	git checkout -b $(shell date +%Y-%m-%d)
	git push -u origin $(shell date +%Y-%m-%d)