from github import Github
import time, os, requests, csv

# Get a token from https://github.com/settings/tokens
# You can do 30 requests per minute (2 second sleep time) when authenticating with a token
# Without authentication you can do 10 requests per minute(6 second sleep time)
GITHUB_TOKEN=os.getenv('GITHUB_TOKEN', None)
g = Github(GITHUB_TOKEN)
sleep_time = 2 if GITHUB_TOKEN else 6

HOTSPOTS_TXT=os.getenv('HOTSPOTS', "hotspots.txt")
DENYLIST_URL='https://raw.githubusercontent.com/helium/denylist/main/denylist.csv'

print("Getting denylist")

res = requests.get(DENYLIST_URL)
decoded_content = res.content.decode('utf-8')
cr = csv.reader(decoded_content.splitlines(), delimiter=',')
deny_list = [hotspot[0] for hotspot in cr]

print("Loading hotspots")
with open(HOTSPOTS_TXT) as file:
    hotspots = [line.rstrip() for line in file if not line.isspace()]

for addr in hotspots:
    print("Checking " + addr)
    if (addr in deny_list): print ("Found {addr} in published denylist {url}".format(addr = addr, url=DENYLIST_URL))
    issues = g.search_issues("repo:helium/denylist " + addr)
    for issue in issues:
        print("Found {addr} in {url}".format(addr = addr, url=issue.html_url))
    if addr != hotspots[-1]: time.sleep(sleep_time)
