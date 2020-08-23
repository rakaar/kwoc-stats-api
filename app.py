from flask import Flask
import json
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app)

@app.route("/stats/students")
def students():
    students = []
    with open ("stats.json") as stats:
        stats = json.load(stats)
        for username in stats:
            user = {
                "name" : stats[username]["name"],
                "username" : username,
                "prs" : str(stats[username]["pr_open"]) + "/" + str(stats[username]["pr_closed"]),
                "commits" : stats[username]["no_of_commits"],
                "lines" : "+" + str(stats[username]["lines_added"]) + "/-" + str(stats[username]["lines_removed"])
            }
            students.append(user)
    return {"stats":students}, 200

@app.route("/stats/student/<user_name>")
def student(user_name):
    user_name = user_name.lower()
    with open ("stats.json") as stats:
        stats = json.load(stats)
        if user_name in stats:
            return {user_name:stats[user_name]}, 200
        else:
            return "user not found", 404

@app.route("/stats/projects")
def mentors():
    projects =[]
    with open ("mentor_stats.json") as stats:
        stats = json.load(stats)
        for mentor_handle in stats["stats"]:
            for key in stats["stats"][mentor_handle]:

                if key != "mentor_name":
                    commits = 0
                    lines_added = 0
                    lines_removed = 0
                    for contrib in stats["stats"][mentor_handle][key]:
                        if contrib != "title":
                            commits += len(stats["stats"][mentor_handle][key][contrib])
                            for commit in stats["stats"][mentor_handle][key][contrib]:
                                lines_added += commit["lines_added"]
                                lines_removed += commit["lines_removed"]
                    project = {
                        "project": stats["stats"][mentor_handle][key]["title"],
                        "mentor" :mentor_handle,
                        "contris" : len(stats["stats"][mentor_handle][key].keys()) - 1,
                        "commits" : commits,
                        "lines" : "+" + str(lines_added) + "/-" + str(lines_removed)
                    }
                    projects.append(project)
    return({"stats":projects}, 200)


@app.route("/stats/mentor/<user_name>")
def mentor(user_name):
    with open ("mentor_stats.json") as stats:
        stats = json.load(stats)
        if user_name in stats["stats"]:
            return {user_name:stats["stats"][user_name]}, 200
        else:
            return "mentor not found", 404

if __name__ == "__main__":
    app.run()