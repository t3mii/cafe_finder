import os
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify
import overpy

app = Flask(__name__)
api = overpy.Overpass()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cafes")
def get_cafes():
    result = api.query("""
      node
        ["amenity"="cafe"]
        (around:1000,38.9807,-76.9368);  // College Park
      out;
    """)
    cafes = [
        {
            "name": node.tags.get("name", "Unnamed Café"),
            "lat": node.lat,
            "lng": node.lon
        }
        for node in result.nodes
    ]
    return jsonify(cafes)

if __name__ == "__main__":
    app.run(debug=True)


load_dotenv()


def main():
        from osm_places import find_cafes

        location = os.getenv("SEARCH_LOCATION", "College Park, MD")
        print(f"Searching OpenStreetMap for cafes near: {location}")
        cafes = find_cafes(location, radius=2000, limit=20)
        for c in cafes:
            print(c.get("name"), "-", f"{c.get('lat')}, {c.get('lon')}")


if __name__ == "__main__":
    main()