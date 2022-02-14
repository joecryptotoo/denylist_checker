# denylist_checker
Check to see if your hotspot is on the [helium denylist](https://github.com/helium/denylist)

This script will scan https://github.com/helium/denylist/issues for issues containing your hotspot.

## Instructions

- Install requirements ```pip3 install pygithub```
- Add all of your hotspot b58 addresses to a hotspots.txt file
- ```python3 ./check_denylist.py```

### Running faster
  This script can run faster with larger lists by using a github token which can be obtained here: https://github.com/settings/tokens
 - ```GITHUB_TOKEN="my token" python3 ./check_denylist.py```

### Running with Docker
  You can also run this script using [Docker](https://www.docker.com/) so that you don't have to install any dependencies
  Use the runme.sh script to build and execute the docker container.
