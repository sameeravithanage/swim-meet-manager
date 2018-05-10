import gspread
from google.auth.transport.requests import AuthorizedSession
from google.oauth2 import service_account
from pprint import pprint


def collectEventResults():
	creds = service_account.Credentials.from_service_account_file('client_secret.json')
	scoped_credentials = creds.with_scopes(['https://spreadsheets.google.com/feeds'])
	gc = gspread.Client(auth=scoped_credentials)
	gc.session = AuthorizedSession(scoped_credentials)
	sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1G1BzfuKTy3OjOex0r8WVohtgfWqXJlvxscc0tQQD0lQ/edit#gid=880015919')
	worksheet = sh.worksheet("25 free")
	list_of_entries = worksheet.get_all_values()
	list_of_entries.pop(0)
	return list_of_entries

def timehandler(list_item):
	time_list=list_item[-1].split('.')
	list_item.append(time_list)


def timeconverter(result_list):
	for i in result_list:
		timehandler(i)
	return result_list

def caltime(result_list):
	for i in result_list:
		if len(i[-1]) == 2:
			miliseconds = int(i[-1][1])
			seconds = int(i[-1][0])
			sectomil = seconds*100
			timemil = sectomil + miliseconds
			i[-1] = timemil
		elif len(i[-1]) == 3:
			miliseconds = int(i[-1][2])
			seconds = int(i[-1][1])
			sectomil = seconds * 100
			minutes = int(i[-1][0])
			mintomil = minutes * 60 * 100 
			timemil = mintomil + sectomil + miliseconds
			i[-1] = timemil
	return result_list


def sortresults(result_list):
	result_list.sort(key=lambda x:x[-1])
	for i in result_list:
		del i[-1]
	return(result_list)

result_list = collectEventResults()
updated_results=timeconverter(result_list)
results_to_sort = caltime(updated_results)
sortresults(results_to_sort)