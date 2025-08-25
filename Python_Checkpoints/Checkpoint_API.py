""" In this checkpoint, we are going to practice consuming public APIs through the NASA public APIs portal.

Portal description : The objective of this portal is to make NASA data, including imagery, eminently accessible to application developers and data professionals. Before starting to use its APIs endpoints, it's mandatory that you generate your API KEY and store it somewhere for later use. The API key acts as the user identifier when requesting the API. To get your KEY, fill in the provided form with your personal information, and then we shall receive an email containing your personal API KEY.

➡️ NASA API PORTAL

https://i.imgur.com/hisTmpk.png

 

Go to the NASA API portal and generate your API KEY
Import the requests package and store your API KEY in variable
Go back to portal website and click on 'browse APIs'
Click on the first dropdown menu, named 'APOD' and read its documentation
Follow the provided documentation to ask the API endpoint for the astronomy picture of the day. Get then display the image on your notebook.
Go through the list of the provided API endpoints once again and select 'Asteroids - NeoWs' option. Store the results in a pandas dataframe.
Do the necessary data pre-processing tasks on the previous result in order to get a clean dataframe with the following columns :
Asteroid ID
Asteroid name
The Minimal estimated diameter in Kilometre
Absolute_magnitude
Relative_velocity(km/s)
Try to export the new dataframe into a CSV file and share it with your colleagues """
import json
import requests
import pandas as pd

Api_key = "60zpMZ1YNWausnP08IJtPqYammOZIAZcf3I7ECSX"
base_url = "https://api.nasa.gov/planetary/apod"
params = {"api_key":Api_key,"thumbs":True}

# Step 2: Send GET request
response = requests.get(base_url, params = params)

# Step 3: Check for successful response
if response.status_code == 200:
    results = response.json()
    print("Title:", results["title"])
    print("Date:", results["date"])
    print("Explanation:", results["explanation"])
    print("Image URL:", results["url"])
else:
    print("Error",response.status_code)


print("\n")

print(json.dumps(results, indent=2))  # Shows full structure nicely

print("\n" \
"---------------------------------------")

response_AST = requests.get(
    "https://api.nasa.gov/neo/rest/v1/feed",
    params={"start_date": "2025-07-19", "end_date": "2025-07-19", "api_key": Api_key}
)
start_date = "2025-07-19"
if response_AST.status_code == 200:
    feed_data = response_AST.json()["near_earth_objects"]
   
else:
    print("Error",response_AST.status_code)

output_json_path = "neo_feed_2025-07-19_raw.json"
with open(output_json_path, "w", encoding="utf-8") as f:
    json.dump(feed_data, f, indent=2)

print(f"Raw JSON saved to {output_json_path}")

print("\n" \
"---------------------------------------")

records = []
for date, neos in feed_data.items():
    for neo in neos:
        records.append({
            "Asteroid ID": neo["id"],
            "Asteroid Name": neo["name"],
            "Min Diameter (km)": neo["estimated_diameter"] ["kilometers"] ["estimated_diameter_min"],
            "Absolute Magnitude": neo["absolute_magnitude_h"],
            "Relative Velocity (km/s)": float( neo["close_approach_data"][0] ["relative_velocity"] ["kilometers_per_second"])
        })

# 4. Build DataFrame with desired column order
df = pd.DataFrame(records, columns=[
    "Asteroid ID",
    "Asteroid Name",
    "Min Diameter (km)",
    "Absolute Magnitude",
    "Relative Velocity (km/s)"
])

# 5. Preview the cleaned DataFrame
print(df.head(3))

# 6. Export to CSV
output_file = f"neo_feed_{start_date}_clean.csv"
df.to_csv(output_file, index=False)
print("Data successfully exported to", output_file)