import requests 
import pandas as pd
import streamlit as st
# Step 1: API credentials and endpoint
api_key = "b7c50ab0"

base_url = "https://www.omdbapi.com/"


def Find_movie(movie_name):
    params = {"apikey": api_key, "s": movie_name}

    # Step 2: Send GET request
    response = requests.get(base_url, params = params)

    # Step 3: Check for successful response
    if response.status_code == 200:
        results = response.json().get("Search", [])
        movies_list = [
            {
                "Title": m.get("Title"),
                "Year": m.get("Year"),
                "ID": m.get("imdbID"),
                "Type": m.get("Type"),
                "Poster" : m.get("Poster")
            }
            for m in results
        ] 
        return pd.DataFrame(movies_list)
    else:
        st.error(f"API Error: {response.status_code}")
        return pd.DataFrame()
    


movie_df = Find_movie("star wars")
print(movie_df)

"""     else: print("Error")
    output_json_path = "search_feed_raw.json"
    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    Find_movie("star wars") """

