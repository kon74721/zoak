#!/bin/sh

D=$(dirname $0)
OUT=index.js

echo "module.exports = {" > $OUT
ls $D/*.czml |while read f; do
	name=$(basename $f .czml)
	header="$(head -n1 $f |grep '// zoak: ' |cut -c 10-)"
	[ -z "$header" ] && header="$name, no info" || (tail -n +2 $f > $f.tmp && mv $f.tmp $f)
	echo "adding $name - $header"
	echo -e "\t\"${name}\": \"${header}\"," >> $OUT
done
echo "};" >> $OUT
echo "DONE $OUT created"
