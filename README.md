# kwoc-stats-api
---
## Local setup :
 - `python3 -m venv env` - create a virtual environment
 - `source env/bin/activate` - activate the virtual environment
 - `pip install -r requirements.txt` - install the requirements
 - `pre-commit install` - install pre-commit
 - `python app.py` - run the server
---
## Endpoints :
students :
 - `/stats/students` - get stats of all students
 - `/stats/student/<user_name>` - get student stats for <user_name>
 projects :
 - `/stats/projects` - get stats of all projects
 mentors :
 - `/stats/mentor/<user_name>` - get mentor stats for <user_name>
 ---
 deployed [here](https://kwoc-stats-test-api.herokuapp.com/) .
 ---
## Scripts :
Short description :
 - `no_commits.py` - generate `no_commits.csv` (name, email) with students having no commits
 ---
## Code structure with pre-commit, black, bandit, flake8, isort :
 - When a git commit is done your code get automatically re-formatted
 - You will have to check the proposed modifications and re-add them in a continuous process of `git add`/`git commit`
 - When your code passes the pre-commit checks, you will be able to finally commit your code and push to GitHub
 - Various imports are automatically sorted for you
 - Automatic checks verify that unused libraries and variables can't get committed
 - Contributors are expected to follow this code of conduct as it guarantees code formatting quality
