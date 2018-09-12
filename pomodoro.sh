#!/bin/env bash
t() {
	for ((i=$1*1;i>=0;i--)); do 
		printf '\r%02d:%02d' $(($i%3600/60)) $(($i%60))
		sleep 1
	done
	echo -ne "\r\a"
}

c=0
while true; do
	t 25
	((c++))
	if [ $((c%4)) -eq 0 ]; then
		t 30
	else
		t 5
	fi
done
