# denylist_checker
Check to see if your hotspot is on the [helium denylist](https://github.com/helium/denylist)

## This _fancy_ python script will:
- search https://github.com/helium/denylist/issues for issues containing your hotspot address
- search https://raw.githubusercontent.com/helium/denylist/main/denylist.csv to see if any of your hospots are already on the denylist
- Print out some things like this:
```Getting denylist
Loading hotspots
Checking 11wFoMxkWg85SCp4yaZvjKkb2j3aP5tuokCQ4Ka16dH3YoA2axs
Found 11wFoMxkWg85SCp4yaZvjKkb2j3aP5tuokCQ4Ka16dH3YoA2axs in https://github.com/helium/denylist/issues/735
Found 11wFoMxkWg85SCp4yaZvjKkb2j3aP5tuokCQ4Ka16dH3YoA2axs in https://github.com/helium/denylist/issues/436
Checking 11178QLaM9Ue5JpvSJvehKZHk2XGLi381sku2HeStFkbMswirw9
Found 11178QLaM9Ue5JpvSJvehKZHk2XGLi381sku2HeStFkbMswirw9 in published denylist https://raw.githubusercontent.com/helium/denylist/main/denylist.csv
```

## Instructions

- Install requirements ```pip3 install pygithub```
- Add all of your hotspot b58 addresses to a hotspots.txt file
- ```python3 ./check_denylist.py```

### Running faster
 - This script can run faster with larger lists by using a github token which can be obtained here: https://github.com/settings/tokens
 - Only repo.public_repo permission is required.
 - ```GITHUB_TOKEN="my token" python3 ./check_denylist.py```

### Running with Docker
 - You can also run this script using [Docker](https://www.docker.com/) so that you don't have to install any dependencies
 - Use the runme.sh script to build and execute the docker container.
