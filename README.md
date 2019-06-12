# Choropleth map of India using Folium
This is an example to create choropleth of India based on any stat, using folium and geojson. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites


```
virtualenv
python3
```

### Installing



```
cd <directory of your choice>
git clone https://github.com/rajesh241/foliumIndiaChoropleth
cd foliumIndiaChoropleth
```

Creating Virtual Env and downloading packages

```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```
Just run the python code
```
python foliumIndiaChoropleth.py
```
This would output indiaChoropleth.html which can be opened in browser and it would have Choropleth Map of India.  
##Example Output
![Choropleth](exampleMap.png?raw=true "India Choropleth")
## Acknowledgments

* [geohacker](https://github.com/geohacker/india/blob/master/state/india_telengana.geojson) - The geojson file was used from here and modified. 

