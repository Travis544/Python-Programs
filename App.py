import random
import webbrowser
import time

while True:
    sites = random.choice(['google.com', 'mastercode.online', 'youtube.com', 'weather.gov'])
    visit = "http://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(5, 20)
    time.sleep(seconds)

