#!/bin/sh

for f in *.csv; do
	name="$(basename $f .csv)"
	echo "converting $name"
	./convert_movebank.py $f > ../$name.czml
done
