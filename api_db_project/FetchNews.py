import requests
import datetime


class News():
    # Your API key is: ####################
    key = "###########################"
    base_url = 'https://newsapi.org/v2/everything'
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    d = {'language':'en','apiKey':key,'from':yesterday,'to':today}
    body_string = ''

    def __init__(self, name, email, interest):
        self.name = name
        self.interest = interest
        self.email = email

    def fetch_data(self):
        self.d['qInTitle'] = self.interest
        req = requests.get(self.base_url, self.d)
        req_json = req.json()
        #print(req_json['articles'][0]['title'])

        for article in req_json['articles']:
            self.body_string = self.body_string + article['title'] + "\n" + article['url'] + "\n\n"


if __name__ == "__main__":
    u = News('abhi', 'NASA', 'abhi@a.com')

