#!/bin/sh

while true; do
	echo "obase=2;$(date +%s)" | bc | sed y/01/▯▮/
	sleep 1
done
