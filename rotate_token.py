import requests

# GitLabの設定
GITLAB_URL = "https://gitlab.com"
PROJECT_ID = "your_project_id"
PRIVATE_TOKEN = "your_admin_private_token"


# トークンの生成
def create_project_access_token(project_id, name, scopes, expires_at):
    url = f"{GITLAB_URL}/api/v4/projects/{project_id}/access_tokens"
    headers = {
        "PRIVATE-TOKEN": PRIVATE_TOKEN
    }
    data = {
        "name": name,
        "scopes": scopes,
        "expires_at": expires_at
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 201:
        return response.json()["token"]
    else:
        raise Exception(f"Failed to create access token: {response.content}")


def set_project_variable(project_id, key, value):
    url = f"{GITLAB_URL}/api/v4/projects/{project_id}/variables"
    headers = {
        "PRIVATE-TOKEN": PRIVATE_TOKEN
    }
    data = {
        "key": key,
        "value": value
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code != 201:
        raise Exception(f"Failed to set project variable: {response.content}")


# リポジトリリスト
repository_ids = ["repo_id_1", "repo_id_2", "repo_id_3"]

# トークンの再生成
new_token = create_project_access_token(PROJECT_ID,
                                        "project_access_token",
                                        ["api"],
                                        "2025-01-01")
print(f"New token: {new_token}")

# トークンを各リポジトリに適用
for repo_id in repository_ids:
    set_project_variable(repo_id, "PROJECT_ACCESS_TOKEN", new_token)
    print(f"Set new token for project {repo_id}")
