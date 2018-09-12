/bin/env bash
t() {
	sleep $(($1*60))
	echo -e "\a"
}

c=0
while true; do
	t 25
	((c++))
	if [ $(( $c % 4 )) -eq 0 ]; then
		t 30
	else
		t 5
	fi
done
