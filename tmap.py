from tinder_api_sms import *
import gmplot

recs = get_recommendations()["results"];
mymap = gmplot.GoogleMapPlotter(13.0817, 80.2230, 16)
#mymap.apikey="AIzaSyA-kXbq7gPaNlmCLyTZ09sAO3sD-HcIczQ"
mymap.marker(13.0817, 80.2230)
mymap.text(13.0817, 80.2230, 'Me')
colors=['red','blue','yellow','green','orange','cyan','gray','purple','teal']
i=0

for person in recs:
    #print(person)#for debugging and raw analysis
    person_name=person["name"];
    #person_picture_list=person["photos"]#work on this list to separate url only
    #person_picture=person_picture_list["url"]#work on this too
    person_id = person["_id"];
    person_bio = person["bio"];
    person_distance=person["distance_mi"];
    person_birthday=person["birth_date"];
    if(person_distance>100):
    	continue
    mymap.circle(13.0817, 80.2230,radius=int(person_distance)*1000, color=colors[i],title=person_name)
    mymap.draw('tinder_visualization.html')
    print("Name: "+person_name)
    print("Bio is: ",end="")
    print(str(person_bio))
    print("is "+str(person_distance)+" km away and is highlighted in "+colors[i])
    print("her birthday is "+str(person_birthday))
    #print("Check her picture out at "+person_picture)#once you work the above image bit remove this
    print("*******************************")
    i=i+1
