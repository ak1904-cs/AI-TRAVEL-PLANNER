"""
Generate a realistic travel dataset simulating Kaggle's:
- 'Travel Dataset' (destinations, ratings, costs)
- 'Tourism Dataset' (activities, types, durations)
Combined into a student-friendly travel ML training dataset.
"""
import pandas as pd
import numpy as np
import json, random, os

random.seed(42)
np.random.seed(42)

# ─── Destination data ───────────────────────────────────────────────────
destinations = [
    {"city":"Goa","state":"Goa","type":"Beach","avg_cost_per_day":800,"rating":4.5,"student_friendly":1,"best_season":"Winter","lat":15.2993,"lon":74.1240},
    {"city":"Manali","state":"Himachal Pradesh","type":"Hills","avg_cost_per_day":700,"rating":4.6,"student_friendly":1,"best_season":"Summer","lat":32.2396,"lon":77.1887},
    {"city":"Jaipur","state":"Rajasthan","type":"Heritage","avg_cost_per_day":600,"rating":4.4,"student_friendly":1,"best_season":"Winter","lat":26.9124,"lon":75.7873},
    {"city":"Rishikesh","state":"Uttarakhand","type":"Adventure","avg_cost_per_day":500,"rating":4.7,"student_friendly":1,"best_season":"Summer","lat":30.0869,"lon":78.2676},
    {"city":"Darjeeling","state":"West Bengal","type":"Hills","avg_cost_per_day":650,"rating":4.5,"student_friendly":1,"best_season":"Spring","lat":27.0360,"lon":88.2627},
    {"city":"Hampi","state":"Karnataka","type":"Heritage","avg_cost_per_day":400,"rating":4.6,"student_friendly":1,"best_season":"Winter","lat":15.3350,"lon":76.4600},
    {"city":"Coorg","state":"Karnataka","type":"Nature","avg_cost_per_day":900,"rating":4.4,"student_friendly":1,"best_season":"Monsoon","lat":12.3375,"lon":75.8069},
    {"city":"Varanasi","state":"Uttar Pradesh","type":"Spiritual","avg_cost_per_day":500,"rating":4.3,"student_friendly":1,"best_season":"Winter","lat":25.3176,"lon":82.9739},
    {"city":"Munnar","state":"Kerala","type":"Hills","avg_cost_per_day":750,"rating":4.5,"student_friendly":1,"best_season":"Monsoon","lat":10.0889,"lon":77.0595},
    {"city":"Spiti Valley","state":"Himachal Pradesh","type":"Adventure","avg_cost_per_day":600,"rating":4.8,"student_friendly":1,"best_season":"Summer","lat":32.2458,"lon":78.0317},
    {"city":"Andaman Islands","state":"Andaman","type":"Beach","avg_cost_per_day":1500,"rating":4.7,"student_friendly":0,"best_season":"Winter","lat":11.7401,"lon":92.6586},
    {"city":"Udaipur","state":"Rajasthan","type":"Heritage","avg_cost_per_day":800,"rating":4.6,"student_friendly":1,"best_season":"Winter","lat":24.5854,"lon":73.7125},
    {"city":"Kasol","state":"Himachal Pradesh","type":"Adventure","avg_cost_per_day":450,"rating":4.5,"student_friendly":1,"best_season":"Summer","lat":32.0097,"lon":77.3143},
    {"city":"Pondicherry","state":"Tamil Nadu","type":"Beach","avg_cost_per_day":700,"rating":4.3,"student_friendly":1,"best_season":"Winter","lat":11.9416,"lon":79.8083},
    {"city":"Leh Ladakh","state":"Jammu & Kashmir","type":"Adventure","avg_cost_per_day":1000,"rating":4.9,"student_friendly":1,"best_season":"Summer","lat":34.1526,"lon":77.5771},
]

activities_map = {
    "Beach":     [("Swimming",2,0),("Snorkeling",3,300),("Beach Volleyball",2,0),("Sunset Walk",1,0),("Water Sports",4,500)],
    "Hills":     [("Trekking",5,0),("Paragliding",3,800),("Camping",8,600),("Photography",3,0),("Local Market Visit",2,0)],
    "Heritage":  [("Fort Visit",4,200),("Museum Tour",3,150),("City Walk",3,0),("Local Cuisine Tour",2,0),("Cultural Show",2,300)],
    "Adventure": [("River Rafting",4,800),("Rock Climbing",3,500),("Zip-lining",2,600),("Bungee Jumping",1,1500),("Camping",8,600)],
    "Nature":    [("Wildlife Safari",5,500),("Waterfall Hike",4,0),("Bird Watching",3,0),("Coffee Plantation Tour",3,200),("Cycling",3,100)],
    "Spiritual": [("Ghat Walk",2,0),("Aarti Ceremony",2,0),("Temple Tour",4,0),("Yoga Class",2,200),("Boat Ride",1,150)],
}

rows = []
for dest in destinations:
    acts = activities_map.get(dest["type"], activities_map["Nature"])
    for act_name, duration, act_cost in acts:
        for budget_tier in ["low","medium","high"]:
            budget_num = {"low":500,"medium":1000,"high":2000}[budget_tier]
            feasible = 1 if dest["avg_cost_per_day"] <= budget_num else 0
            rows.append({
                "destination": dest["city"],
                "state": dest["state"],
                "destination_type": dest["type"],
                "avg_cost_per_day": dest["avg_cost_per_day"],
                "destination_rating": dest["rating"],
                "student_friendly": dest["student_friendly"],
                "best_season": dest["best_season"],
                "latitude": dest["lat"],
                "longitude": dest["lon"],
                "activity": act_name,
                "activity_duration_hrs": duration,
                "activity_cost": act_cost,
                "budget_tier": budget_tier,
                "daily_budget": budget_num,
                "recommended": feasible,
            })

df = pd.DataFrame(rows)
df.to_csv("travel_dataset.csv", index=False)
print(f"Dataset created: {len(df)} rows, {len(df.columns)} columns")
print(df.head(3).to_string())
