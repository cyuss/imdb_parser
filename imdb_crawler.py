#from bs4 import BeautifulSoup
import urllib2
import json

def find_movie(title, year, format="json"):
	"""
	find a movie using imdb api with the title and the year
	"""
	# http://www.omdbapi.com/?t=legend&y=2015&plot=short&r=json
	t = title.replace(" ", "+")
	url = "http://www.omdbapi.com/?t="+t+"&y="+str(year)+"&plot=full&r="+format

	request = urllib2.Request(url)
	response = json.load(urllib2.urlopen(request))
	data = json.dumps(response, indent=2)
	print data
	return data


if __name__ == "__main__":
	title = raw_input("Please enter a movie title: ")
	year = raw_input("Which year? ")
	description = find_movie(title, year)
	#find_movie("close range", 2015)
