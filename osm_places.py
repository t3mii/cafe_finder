"""Utilities to find cafes using OpenStreetMap (Nominatim + Overpass API).

This module geocodes a location string to coordinates using geopy.Nominatim
and then queries Overpass to find nearby nodes/ways tagged as amenity=cafe.
"""
from typing import List, Dict
import requests
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


geolocator = Nominatim(user_agent="cafe_finder_app")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)


def geocode_location(location: str):
    loc = geocode(location)
    if not loc:
        raise ValueError(f"Could not geocode location: {location}")
    return loc.latitude, loc.longitude


def query_overpass(lat: float, lon: float, radius: int = 2000) -> List[Dict]:
    """Query Overpass API for amenity=cafe within radius (meters).

    Returns a list of elements from the Overpass response.
    """
    overpass_url = "https://overpass-api.de/api/interpreter"
    # Overpass QL: search for nodes and ways with amenity=cafe
    query = f"""
    [out:json][timeout:25];
    (
      node[amenity=cafe](around:{radius},{lat},{lon});
      way[amenity=cafe](around:{radius},{lat},{lon});
      relation[amenity=cafe](around:{radius},{lat},{lon});
    );
    out center tags;
    """
    resp = requests.post(overpass_url, data=query.strip())
    resp.raise_for_status()
    data = resp.json()
    return data.get("elements", [])


def find_cafes(location: str, radius: int = 2000, limit: int = 20) -> List[Dict]:
    lat, lon = geocode_location(location)
    elements = query_overpass(lat, lon, radius=radius)
    cafes = []
    for el in elements:
        tags = el.get("tags", {})
        name = tags.get("name") or tags.get("ref") or "(unnamed)"
        # For ways/relations Overpass returns a 'center' dict with lat/lon
        if el.get("type") == "node":
            el_lat = el.get("lat")
            el_lon = el.get("lon")
        else:
            center = el.get("center") or {}
            el_lat = center.get("lat")
            el_lon = center.get("lon")

        cafes.append({
            "id": el.get("id"),
            "osm_type": el.get("type"),
            "name": name,
            "tags": tags,
            "lat": el_lat,
            "lon": el_lon,
        })
        if len(cafes) >= limit:
            break
    return cafes
