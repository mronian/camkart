import re
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'facerec.settings')

import django
django.setup()

from jobs.models import Camera
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
	i=0

	for n in range(len(nikon)):
		for j in range(len(attrList)):
			if attrList[j] not in nikon[n]:
				if j in [3, 5, 6,7,9]:
					nikon[n][attrList[j]]="0"
				else:
					nikon[n][attrList[j]]=""
			elif nikon[n][attrList[j]]=="":
				if j in [3, 5, 6,7,9]:
					nikon[n][attrList[j]]="0"
		i=i+1
		if i%20==0:
			print(i)
		try:
			add_cam(nikon[n][attrList[0]],nikon[n][attrList[1]],nikon[n][attrList[2]],int(nikon[n][attrList[3]]),nikon[n][attrList[4]],int(nikon[n][attrList[5]]),int(nikon[n][attrList[6]]),float(nikon[n][attrList[7]]),nikon[n][attrList[8]],float(nikon[n][attrList[9]]),nikon[n][attrList[10]])
		except(Exception):
			for j in range(len(attrList)):
				print str(j) + " " + nikon[n][attrList[j]]
			break


def add_cam(link, color, url, pri, tit, nr, nrat, avg, ctype, senti, stype):
    j=Camera.objects.get_or_create(link=link, color=color, img_url=url, price=pri, title=tit, number_of_reviews=nr, number_of_ratings=nrat, avg_rating=avg, cameratype=ctype, sentiment_score=senti, sensor_type=stype)[0]
    return j

if __name__ == '__main__':
	main()