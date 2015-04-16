import re

nikon = {}

def main():
	breakFlag = False
	continueFlag = False
	tLine = ''
	for i in range(435):
		try:
			data = open('data/cam_' + str(i) + '.xml', 'r')
		except IOError:
			print 'file: cam_' + str(i) + '.xml', ' not found!'
			continue
		nikon[i] = {}
		nikon[i]['review'] = []
		for line in data:
			if continueFlag:
				if '</specsKey>' in line:
					continueFlag = False
					tLine = tLine + line.strip()
					# print tLine
				else:
					tLine = tLine + line.strip()
					continue
			else:
				wasContinueSet = False
				tLine = line.strip()
				if 'View More' in line:
					continueFlag = True
					wasContinueSet = True
					continue
			if wasContinueSet:
				m = re.search(r'<specsKey="(.*)">(.*)\.\.\.View More(.*)</specsKey>', tLine)
				if m is None:
					print 'Set : ' + tLine
					break
				else:
					index = m.group(1)
					value = m.group(3)
			else:
				m = re.search(r'<specsKey="(.*)">(.*)</specsKey>', tLine)
				if m is None:
					print 'Set : ' + tLine
					break
				else:
					index = m.group(1)
					value = m.group(2)
			#print index, " : ", value
			if 'review' not in index:
				nikon[i][index] = value
			else:
				if 'number_of_reviews' == index:
					nikon[i][index] = value
				else:
					nikon[i]['review'].append(value)
		if breakFlag:
			break

	attrList=['link', 'color', 'img_url', 'price', 'title', 'number_of_reviews', 'number_of_ratings', 'avg_rating', 'type', 'sentiment_score', 'Sensor Type']
	x=[]
	for n in nikon:
		for y in nikon[n].keys():
			if y not in x:
				x.append(y)

	# for a in x:
	# 	print(a)
	for n in range(len(nikon)):
		print "add_cam(\'",
		print nikon[n][attrList[0]],
		for j in range(1, len(attrList)):
			if attrList[j] in nikon[n]:
				print "\',\'"+nikon[n][attrList[j]],
		print "\')"
if __name__ == '__main__':
	main()