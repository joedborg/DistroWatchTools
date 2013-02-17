import urllib2, json
from bs4 import BeautifulSoup

class DistroWatchTopTen(object):
    """
    Get the top 10 Linux distros from DistroWatch
    and make some exportable formats for it.

    This was written by Joseph Borg - http://github.com/joedborg - and
    is completely free (libre) to do what you want with; please just 
    reference my git page in any copy.
    It requires BeautifulSoup which can be found at http://www.crummy.com/software/BeautifulSoup
    """
    def __init__(self):
        """
        On init, create the soup.
        """
        url = "http://distrowatch.com/dwres.php?resource=major"
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page.read())
        page.close()

        self.top_ten = list()
        dists = soup.find_all(attrs={'class':'News1'})
        for dist in dists:
            try:
                obj = dict()
                obj['name'] = str(dist.find(attrs={'class':'NewsHeadline'}).getText())
                obj['icon'] = str("http://distrowatch.com/"+dist.find("img").attrs['src'])
                obj['desc'] = str(dist.find(attrs={'class':'NewsText'}).getText())
                self.top_ten.append(obj)
            except:
                continue

    def toJson(self):
        """
        Convert the top 10 to a JSON object.
        """
        return json.dumps(self.top_ten)

    def toPython(self):
        """
        Return the Python list of dicts.
        """
        return self.top_ten
