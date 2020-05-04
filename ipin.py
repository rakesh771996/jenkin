import geoip2.database
from flask import Flask,render_template,request
import folium
import webbrowser
app = Flask(__name__)
print("post-commit is going on ............. yes dene")
reader=geoip2.database.Reader('./GeoLite2-City_20200428/GeoLite2-City.mmdb')
@app.route("/")
def index():
	return render_template('input.html')

@app.route('/profile1/',methods=['post','get'])
def profile1():
	ip=request.form['ip']
	response=reader.city(ip)
	lat=response.location.latitude
	lang=response.location.longitude


	m=folium.Map(location=[lat,lang],zoom_start = 15)
	folium.Marker(location=[lat,lang],icon=folium.Icon(color='red'),popup="<h4> country "+response.country.name+"<br>City: "+response.city.name+"<br></h4>").add_to(m)
	m.save('C:\\Users\\Rakesh\\Desktop\\project\\templates\\index.html')
	return render_template('index.html')



if __name__=="__main__":
	app.run()
