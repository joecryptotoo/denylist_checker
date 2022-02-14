from github import Github
import time, os

# Get a token from https://github.com/settings/tokens
# You can do 30 requests per minute (2 second sleep time) when authenticating with a token
# Without authentication you can do 10 requests per minute(6 second sleep time)
github_token=os.getenv('GITHUB_TOKEN', None)
g = Github(github_token)

sleep_time = 2 if github_token else 6

print("Loading hotspots")
with open("hotspots.txt") as file:
    hotspots = [line.rstrip() for line in file if not line.isspace()]

for addr in hotspots:
    print("Checking " + addr)
    issues = g.search_issues("repo:helium/denylist " + addr)
    for issue in issues:
        print("Found {addr} in {issue_url}".format(addr = addr, issue_url=issue.html_url))
    if addr != hotspots[-1]: time.sleep(sleep_time)
