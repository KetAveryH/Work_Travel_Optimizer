import config
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key=config.GOOGLE_API_KEY)

now = datetime.now()



print(config.GOOGLE_API_KEY)

