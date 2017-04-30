#!/bin/sh

D=$(dirname $0)
OUT=index.js

echo "module.exports = {" > $OUT
ls $D/*.czml |while read f; do
	name=$(basename $f .czml)
	echo "adding $name"
	echo -e "\t${name}: 0," >> $OUT
done
echo "};" >> $OUT
echo "DONE $OUT created"
