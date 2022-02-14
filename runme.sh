#!/usr/bin/env bash

HOTSPOTS=${HOTSPOTS:-"$(pwd)/hotspots.txt"}


docker build -t denylist_checker .

docker run --rm \
	-v ${HOTSPOTS}:/scripts/hotspots.txt \
	denylist_checker

