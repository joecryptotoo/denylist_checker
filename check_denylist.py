from github import Github
import time, os, requests, csv

# Get a token from https://github.com/settings/tokens
# You can do 30 requests per minute (2 second sleep time) when authenticating with a token
# Without authentication you can do 10 requests per minute(6 second sleep time)
GITHUB_TOKEN=os.getenv('GITHUB_TOKEN', None)
g = Github(GITHUB_TOKEN)
sleep_time = 2 if GITHUB_TOKEN else 6

HOTSPOTS_TXT=os.getenv('HOTSPOTS', "hotspots.txt")

print("Loading hotspots")
with open(HOTSPOTS_TXT) as file:
    hotspots = [line.rstrip() for line in file if not line.isspace()]

repo = g.get_repo("helium/denylist")
branches = repo.get_branches()

#Check all branches
for branch in branches:
    DENYLIST_URL='https://raw.githubusercontent.com/helium/denylist/' + branch.name + '/denylist.csv'
    print("Getting denylist from branch " + branch.name)

    res = requests.get(DENYLIST_URL)
    decoded_content = res.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    deny_list = [hotspot[0] for hotspot in cr]

    for addr in hotspots:
        print("Checking " + addr)
        if (addr in deny_list):
            print("Found {addr} in published denylist {url} in branch {branch}".format(addr=addr, url=DENYLIST_URL, branch=branch.name))

#Check issues
for addr in hotspots:
    print("Checking " + addr)
    if (addr in deny_list): print ("Found {addr} in published denylist {url}".format(addr = addr, url=DENYLIST_URL))
    issues = g.search_issues("repo:helium/denylist " + addr)
    for issue in issues:
        print("Found {addr} in {url}".format(addr = addr, url=issue.html_url))
    if addr != hotspots[-1]: time.sleep(sleep_time)
