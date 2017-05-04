#!/bin/sh

D="$(dirname $0)"

for f in $D/*.csv; do
	name="$(basename $f .csv)"
	echo "converting $name"
	./convert_movebank.py $f > $D/$name.czml
done
