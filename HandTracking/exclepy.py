import csv
n = 0
# f=open("demo.txt","r")
# while True:
#     line=f.readline()
#     if not line:
#         break
#     line=line[:-2]
#     l.extend(line.lstrip())
#
# print(l)
def something():
	with open('demo.txt','r+') as f:
		listl=[]
		for line in f:
			strip_lines=line.strip()
			listli=strip_lines.split()
			print(listli)
			listl.append(listli)
	#f.truncate(0)

	# skip=[2,5,8,11,14,17,20,23,26,29,32,35,38,41,44,47,50,53,56,59,62]
	skip=[2]
	for i in range(2,189,3):
		skip.append(i)



	final=[]
	print(len(listl))
	for i in range(0,len(listl)):
		if i in skip:
			continue
		final.append(listl[i])
	print(final)

	#print(listl)

	column = ["x0", "y0","x1","y1","x2", "y2", "x3", "y3", "x4", "y4", "x5", "y5", "x6", "y6", "x7", "y7", "x8", "y8", "x9",
			  "y9", "x10", "y10", "x11", "y11", "x12", "y12", "x13", "y13", "x14", "y14", "x15", "y15", "x16", "y16",
			  "x17", "y17", "x18", "y18", "x19", "y19", "x20", "y20"]
	#its okay yaaa run the prev code it will work
	with open("demodata.csv", 'w') as csvfile:
		# creating a csv writer object
		csvwriter = csv.writer(csvfile)

		# writing the fields
		csvwriter.writerow(column)
		# writing the data rows
		csvwriter.writerow(final[0:42])
		csvwriter.writerow(final[42:84])
		#csvwriter.writerow(final[84:126])
		#row=next(csvwriter)

