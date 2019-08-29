# model-studio
Flask web app with user authentication and database connection for Plotly dash app development and supply chain engineering.

### Instructions
- ```python -m pip install -r requirements.txt```
- On windows:
  - ```set FLASK_APP=cartesian_routes```
  - ```set FLASK_ENV=development```
  - ```set SQL_SERVER=server-name-here```
- On other:
  - ```export FLASK_APP=cartesian_routes```
  - ```export FLASK_ENV=development```
  - ```export SQL_SERVER=server-name-here```
- ```python -m flask run```
- [click here](http://127.0.0.1:5000/routes/)

#### Other
- ```python -m flask init-db``` to initialize the database using models.py. **Note**: geocodes table is a copy of geo and does not have a SQLAlchemy model.


#### v0.1 Functionality
- Standardized cleaned shipment data SQL upload.
  - Requirements: [see shipments.csv](https://github.com/christopherpryer/model-studio/blob/master/model_studio/static/shipments.csv)
- Standardized processed shipment data:
  - geocoded origins and destinations.
  - distances between origins and destinations ([haversine](https://en.wikipedia.org/wiki/Haversine_formula)).
 - Standardized processed shipment data SQL/Dash download.

 #### Wishlist
- Standardized lane visualization.
- Standardized geocode data storage.
- Standardized process for publishing plots of shipment data.
- Standardized location visual scaling.
- Standardized location hover-text.
- Location data SQL abstraction.
- Shipment data SQL abstraction.
- PC Miler distance calculation.
- Data error handling (shipment_id assumptions, etc.).
