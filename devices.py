def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""
with file("out.txt") as f:
		old = f.read()
x=[]
while True:
	with file("out.txt") as f:
		s = f.read()
	olds=s
	s=s.replace(old,"")
	if( s):
		if("detected" in s):
			x.append(["connected at "+s[:15],find_between(s,"Vendor=",","),find_between(s,"idProduct=","\n"),find_between(s,"Product: ","\n"),find_between(s,"SerialNumber: ","\n"),find_between(s,"device number "," ")])
			print x
		if("disconnect" in s):
			x.append(["disconnected at "+s[:15],find_between(s,"device number ","\n")])
			print x
	f.close()
	old=olds
	time.sleep(1)
