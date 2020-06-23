from tinder_api_sms import *
import gmplot 

recs = get_recommendations()["results"];
mymap = gmplot.GoogleMapPlotter(13.0817, 80.2230, 16)
mymap.apikey="AIzaSyA-kXbq7gPaNlmCLyTZ09sAO3sD-HcIczQ"
for person in recs:
    person_name=person["name"];
    person_id = person["_id"];
    person_bio = person["bio"];
    person_distance=person["distance_mi"];
    mymap.circle(13.0695, 80.2318,radius=int(person_distance)*1000)#, color='yellow')
    mymap.draw('tinder_visualization.html')
    print("Name: "+person_name)
    print("Bio is: "+str(person_bio));
    print("is "+str(person_distance)+" miles away")
    print("*******************************")
