import gspread
from google.auth.transport.requests import AuthorizedSession
from google.oauth2 import service_account
from pprint import pprint
from random import shuffle 



def teamTag(team,entries):
	names = []
	for i in (entries):
		i.append(team)
		names.append(i)
	return names

def collectData(link,teams):
	# scope = ['https://spreadsheets.google.com/feeds']
	# creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
	creds = service_account.Credentials.from_service_account_file('client_secret.json')
	scoped_credentials = creds.with_scopes(['https://spreadsheets.google.com/feeds'])
	gc = gspread.Client(auth=scoped_credentials)
	gc.session = AuthorizedSession(scoped_credentials)
	sh = gc.open_by_url(link)
	all_entries = []
	for i in teams:
		worksheet = sh.worksheet(i)
		list_of_entries = worksheet.get_all_values()
		header_row = list_of_entries[0]
		events = header_row[1:]
		swimmer_details = list_of_entries[1:]
		entries_by_team = teamTag(i,swimmer_details)
		all_entries.append(entries_by_team)
	return events,all_entries

def list_correction(entries):
	all_entries = []
	for i in entries:
		for j in i:
			all_entries.append(j)
	return(all_entries)

def eventlist(link,entries,events):
	# scope = ['https://spreadsheets.google.com/feeds']
	# creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
	creds = service_account.Credentials.from_service_account_file('client_secret.json')
	scoped_credentials = creds.with_scopes(['https://spreadsheets.google.com/feeds'])
	gc = gspread.Client(auth=scoped_credentials)
	gc.session = AuthorizedSession(scoped_credentials)
	sh = gc.open_by_url(link)
	for i,x in enumerate(events):
		namelist = []
		for l in entries:
			name = []
			if l[i+1] == 'x':
				name.extend((l[0],l[-1],''))
				namelist.append(name)
		shuffle(namelist)
		namelist.insert(0,['NAME','TEAM','TIME'])
		worksheet = sh.add_worksheet(title=x, rows="100", cols="20")
		sh.values_update(x+'!A1',params={'valueInputOption':'RAW'},body={'values': namelist})


link = raw_input("Enter entry sheet url:")
teams = raw_input("Enter teams:")
teams2=teams.split(",")
enventlocation = raw_input("Enter destination url:")


events,entries=collectData(link,teams2)
all_entries = list_correction(entries)
eventlist(enventlocation,all_entries,events)
