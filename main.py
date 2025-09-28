import os
from dotenv import load_dotenv

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