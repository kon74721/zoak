all:
	npm install
	make -C data
	npm run build
