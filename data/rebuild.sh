#!/bin/sh

D=$(dirname $0)
OUT_INDEX=index.js
OUT_DIR=out
mkdir -p $OUT_DIR

set -e

echo "module.exports = {" > $OUT_INDEX
ls $D/{czml,movebank}/*.czml |while read f; do
	name=$(basename $f .czml)
	header="$(head -n1 $f |grep '// zoak: ' |cut -c 10-)"
	out="$OUT_DIR/$name.czml"
	if [ -z "$header" ]; then
		header="$name, no info"
		cp $f $out
	else
		tail -n +2 $f > $f.tmp
		mv $f.tmp $out
	fi
	echo "adding $name - $header"
	echo -e "\t\"${name}\": \"${header}\"," >> $OUT_INDEX
done
echo "};" >> $OUT_INDEX
echo "DONE czml files copied to $OUT_DIR"
echo "DONE $OUT_INDEX created"
