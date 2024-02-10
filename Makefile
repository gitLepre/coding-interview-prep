# create a new branch with name of the date in forma YYYY-MM-DD
# and push it to the remote repository
branch:
	git checkout -b $(shell date +%Y-%m-%d)
	git push -u origin $(shell date +%Y-%m-%d)

challenge:
	@echo "Creating a new challenge"
	@echo "-------------------------"
	@echo "Enter the name of the challenge: "
	@read challenge; \
	echo "Creating a new challenge: $$challenge"; \
	mkdir -p challenges/$$challenge; \
	touch challenges/$$challenge/README.md; \
	touch challenges/$$challenge/solution.py; \
	touch challenges/$$challenge/solution.ts; \
	echo "# $$challenge. " >> challenges/$$challenge/README.md; \
	echo "Created challenges/$$challenge/README.md";
	