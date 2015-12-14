import os
import getpass
user = getpass.getuser()



DIR = '/home/'+user+'/TripieServer/Plan/itineraries'
if not os.path.exists(DIR):
    os.makedirs(DIR)

print len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])