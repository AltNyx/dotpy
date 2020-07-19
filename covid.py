import requests
from bs4 import BeautifulSoup
from collections import namedtuple
from win10toast import ToastNotifier


Data = namedtuple("Data", ['location', 'confirmed',
                           'case_per_mil', 'recovered', 'deaths'])


class Covid:
    def __init__(self, url):
        self.url = url
        self.values = []

    def scrape_website(self):
        response = requests.get(self.url).text
        soup = BeautifulSoup(response, 'lxml')
        table = soup.find('table')
        trows = table.find_all('tr')
        rows = trows[1:]
        return rows

    def get_data(self, rows):
        for row in rows:
            loc = row.find(attrs={'class': "pcAJd"})
            confirmed, _, cpm, recovered, deaths = row.find_all(
                'td', attrs={'class': "l3HOY"})

            data = Data(loc.string, confirmed.string, cpm.string,
                        recovered.string, deaths.string)
            self.values.append(data)

    def display_notification(self):
        toast = ToastNotifier()
        for val in self.values:
            note = f"Location: {val.location}\nConfirmed: {val.confirmed}\nRecovered: {val.recovered}\nDeaths: {val.deaths}\n"
            toast.show_toast("Covid 19 Overview", note, duration=10)


def main():
    url = "https://news.google.com/covid19/map?hl=en-IN&mid=%2Fm%2F049lr&gl=IN&ceid=IN%3Aen"
    cvd19 = Covid(url)
    rows = cvd19.scrape_website()
    cvd19.get_data(rows)
    cvd19.display_notification()


if __name__ == "__main__":
    main()
