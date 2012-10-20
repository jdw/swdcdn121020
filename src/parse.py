import sys
from BeautifulSoup import BeautifulSoup as Soup

class SolarSystem(object):
    def __init__(self):
        self.name = None
        self.planets = []
        self.has_starport = False
        self.has_navalbase = False

    def __str__(self):
        ret = ""
        ret += "System name: " + self.name
        ret += "\nPlanets:\n"
        for p in self.planets:
            ret += "\tName: " + p["name"] + ", property: " + p["prop"] + "\n"

        return ret

def parse(soup):
    system = SolarSystem()
    system.name = soup.find("th", {"id": "system_name"}).text

    # Finding planets
    resulting_planet = {"name": "", "prop": ""}
    for row in soup.find("tbody", {"id": "system"}):
        tds = row.findAll("td")
        if len(tds) == 3:
            resulting_planet = {"name": "", "prop": ""}
            system.planets.append(resulting_planet)
            resulting_planet["name"] = tds[1].find("b").text
        elif len(tds) == 1:
            resulting_planet["prop"] = tds[0].text

    return system


def main():
    file = "/home/jdw/src/swdcdn121020/assets/source.html"
    handler = open(file).read()
    soup = Soup(handler)
    system = parse(soup)
    print system

if __name__ == "__main__":
    main()
