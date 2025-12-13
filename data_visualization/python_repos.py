import requests
import plotly.express as px


url = "https://api.github.com/search/repositories"
params = {
    "q": "language:python stars:>10000",
    "sort": "stars",
    "per_page": 30,
}
r = requests.get(url, headers={"Accept": "application/vnd.github.v3+json"}, params=params)
print(f"Status code:{r.status_code}")

response_dict = r.json()
print(f"Total repositories:{response_dict['total_count']}")
print(f"Complete results:{not response_dict['incomplete_results']}")

repo_dicts = response_dict["items"]
repo_links, stars, hover_texts = [], [], []
print(f"Repositories returned:{len(repo_dicts)}")

# repo_dict = repo_dicts[0]
# print(f"\nKeys:{len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)
print("\nSelected information about each repositories")
# print("\nSelected information about first repositories")
for repo_dict in repo_dicts:
    # print(f"Name:{repo_dict['name']}")
    # print(f"Owner:{repo_dict['owner']['login']}")
    # print(f"Stars:{repo_dict['stargazers_count']} ")
    # print(f"Repositories:{repo_dict['html_url']}")
    # print(f"Created:{repo_dict['created_at']}")
    # print(f"Updated:{repo_dict['updated_at']}")
    # print(f"description:{repo_dict['description']}")
    repo_name = repo_dict["name"]
    repo_url = repo_dict["html_url"]
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    # repo_names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])
    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

title = "Most-Standard Python Project on Gitgub"
labels = {"x": "repository", "y": "stars"}
fig = px.bar(
    x=repo_links,
    y=stars,
    title=title,
    labels=labels,
    hover_name=hover_texts,  # provide per-bar hover text
)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.update_traces(marker_color="SteelBlue", marker_opacity=0.6)
fig.show()
