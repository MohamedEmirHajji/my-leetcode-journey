import json
import os
import requests


def generate_file_table():
    solved_problems_directory = "solved_problems"
    solved_problems_list = [f for f in os.listdir(solved_problems_directory) if os.path.isdir(os.path.join(solved_problems_directory, f))]
    rows = ["| Problem | Solution                                                        | Difficultly | Tags | Submission | Date         |",
            "|---------|-----------------------------------------------------------------|-------------|------|------------|--------------|"]
    for solved_problem in solved_problems_list:
        metadata_file = solved_problems_directory + "/" +solved_problem + "/metadata.json"
        with open(metadata_file, "r", encoding="utf-8") as f:
            metadata = json.load(f)
        problem_details = get_problem_details(metadata['name'])
        name = f"[{metadata['name']}]({metadata['url']})"
        solution = f"[{metadata['language']}](./solved_problems/{solved_problem}/solution.py)"
        difficulty = problem_details['difficulty']
        tags = ', '.join(problem_details['tags'])
        submission = f"[Link]({metadata['submission']})"
        date = "✅ " + metadata['date']
        rows.append(f"| {name} | {solution} | {difficulty} | {tags} | {submission} | {date} |")
    return "\n".join(rows)


def get_problem_details(name):
    title_slug = name.lower().replace(" ", "-")
    request = {
        "operationName": "getQuestionDetail",
        "query": "query getQuestionDetail($titleSlug: String!) { question(titleSlug: $titleSlug) { questionId title content difficulty likes dislikes exampleTestcases topicTags { name } } }",
        "variables": { "titleSlug": title_slug }
    }
    data = requests.post('https://leetcode.com/graphql', json=request).json()
    return {
        "difficulty": data['data']['question']['difficulty'],
        "tags": [tag['name'] for tag in data['data']['question']['topicTags']]
    }


def update_readme(table_content):
    start_marker = "<!-- SOLVED_PROBLEMS_TABLE_START -->"
    end_marker = "<!-- SOLVED_PROBLEMS_TABLE_END -->"
    readme_file = "README.md"

    with open(readme_file, "r", encoding="utf-8") as f:
        content = f.read()

    start = content.find(start_marker)
    end = content.find(end_marker)

    if start == -1 or end == -1:
        raise ValueError("Markers not found in the file")

    new_content = (
            content[:start + len(start_marker)] + "\n" +
            table_content + "\n" +
            content[end:]
    )

    with open(readme_file, "w", encoding="utf-8") as f:
        f.write(new_content)


table_content = generate_file_table()
update_readme(table_content)
