#!/bin/env bash

t() {
	for ((i=$1*60;i>=0;i--)); do 
		printf '\r%02d:%02d' $((i%3600/60)) $((i%60))
		sleep 1
	done
	echo -ne "\r\a"
}

c=0
for ((;;c++)); do
	t 25
	if ((c%4==0)); then
		t 30
	else
		t 5
	fi
done
