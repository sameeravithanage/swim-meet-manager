import csv

teams = ['UCSC','science','law']
events = ['25 free', '25 breast', '25 back ', '25 fly', '50 free', '50 fly ', '50 back ', '50 breast ', '100im']

#read the entry files from each team and create a single list
def inputdata(teams,events):
	entries =[]
	for x in teams:
		with open('../data/'+x+'.csv', 'rb') as inputfile:
			data = list(csv.reader(inputfile, delimiter=','))
			for i in data:
				i.append(x)
				entries.append(i)
	return entries
		
#read the full entry list and create csv file for each event		
def eventlist(entries,events):
	for i,x in enumerate(events):
		namelist = []
		for l in entries:
			name = []
			if l[i+1] == 'x':
				name.extend((l[0],l[-1]))
				namelist.append(name)
		filepath = '../events/'+x+'.csv'
		with open(filepath,'w') as output:
			writer = csv.writer(output, lineterminator='\n')
			writer.writerows(namelist)

			
	






meet_entries = inputdata(teams,events)
eventlist(meet_entries,events)