import urllib.request

BASE_URL = "http://guitarlist.net/bandscore/hoshinogen/koi/img/"
img = []
for i in range(1, 59):
	link_name = "%s%d.png" % (BASE_URL, i)
	img.append(link_name)

for item in img:
	file_name = "00%s" % (item.split('/')[-1])
	u = urllib.request.urlopen(item)
	f = open(file_name, 'wb')
	meta = u.info()
	file_size = int(meta.get_all("Content-Length")[0])
	print("Downloading: %s Bytes: %s" % (file_name, file_size))

	file_size_dl = 0
	block_sz = 8192
	while True:
		buffer = u.read(block_sz)
		if not buffer:
			break
		file_size_dl += len(buffer)
		f.write(buffer)
		status = r"%10d [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
		status = status + chr(8)*(len(status)+1)
		print(status)

	f.close()