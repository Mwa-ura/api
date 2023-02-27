import requests

# Make github API call.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store the API response in a variable
response_dict = r.json()

# process results
print(response_dict.keys())
print(response_dict['total_count'])

#Explore information about repositories
repo_dicts = response_dict['items']
print(F"Repositories returned: {len(repo_dicts)}")

# Examine the first repository
repo_1 = repo_dicts[0]
print(F"\nKeys: {len(repo_1)}")
for key in sorted(repo_1.keys()):
	print(key)
