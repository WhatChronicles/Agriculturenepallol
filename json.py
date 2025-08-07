import pandas as pd
from sqlalchemy import create_engine



columns = [
    "Entity", "Year", "tfp", "output", "inputs", "ag_land_index", "labor_index", "capital_index", "materials_index",
    "output_quantity", "crop_output_quantity", "animal_output_quantity", "fish_output_quantity",
    "ag_land_quantity", "labor_quantity", "capital_quantity", "machinery_quantity", "livestock_quantity",
    "fertilizer_quantity", "animal_feed_quantity", "cropland_quantity", "pasture_quantity", "irrigation_quantity"
]

df_empty = pd.DataFrame(columns=columns)


df_empty.to_csv("Agricultural_total_factor_productivity_USDA.csv", index=False)


engine = create_engine("sqlite:///database.db")
df_empty.to_sql("agricultural_productivity", con=engine, index=False, if_exists="replace")



nepal_data = [
    {"Entity": "Nepal", "Year": 2022, "tfp": 1.18, "output": 2.70, "inputs": 1.45, "ag_land_index": 1.02, "labor_index": 1.08, "capital_index": 0.92, "materials_index": 1.13, "output_quantity": 110000, "crop_output_quantity": 66000, "animal_output_quantity": 33000, "fish_output_quantity": 11000, "ag_land_quantity": 2600000, "labor_quantity": 1530000, "capital_quantity": 520000000, "machinery_quantity": 130000, "livestock_quantity": 830000, "fertilizer_quantity": 47000, "animal_feed_quantity": 94000000, "cropland_quantity": 1900000, "pasture_quantity": 700000, "irrigation_quantity": 520000},
    {"Entity": "Nepal", "Year": 2023, "tfp": 1.21, "output": 2.85, "inputs": 1.50, "ag_land_index": 1.04, "labor_index": 1.09, "capital_index": 0.94, "materials_index": 1.15, "output_quantity": 115000, "crop_output_quantity": 69000, "animal_output_quantity": 34000, "fish_output_quantity": 12000, "ag_land_quantity": 2620000, "labor_quantity": 1540000, "capital_quantity": 530000000, "machinery_quantity": 135000, "livestock_quantity": 840000, "fertilizer_quantity": 48000, "animal_feed_quantity": 96000000, "cropland_quantity": 1920000, "pasture_quantity": 700000, "irrigation_quantity": 530000},
    {"Entity": "Nepal", "Year": 2024, "tfp": 1.24, "output": 3.00, "inputs": 1.55, "ag_land_index": 1.06, "labor_index": 1.10, "capital_index": 0.96, "materials_index": 1.17, "output_quantity": 120000, "crop_output_quantity": 72000, "animal_output_quantity": 35000, "fish_output_quantity": 13000, "ag_land_quantity": 2640000, "labor_quantity": 1550000, "capital_quantity": 540000000, "machinery_quantity": 140000, "livestock_quantity": 850000, "fertilizer_quantity": 49000, "animal_feed_quantity": 98000000, "cropland_quantity": 1940000, "pasture_quantity": 700000, "irrigation_quantity": 540000},
    {"Entity": "Nepal", "Year": 2025, "tfp": 1.27, "output": 3.15, "inputs": 1.60, "ag_land_index": 1.08, "labor_index": 1.11, "capital_index": 0.98, "materials_index": 1.20, "output_quantity": 125000, "crop_output_quantity": 75000, "animal_output_quantity": 36000, "fish_output_quantity": 14000, "ag_land_quantity": 2660000, "labor_quantity": 1560000, "capital_quantity": 550000000, "machinery_quantity": 145000, "livestock_quantity": 860000, "fertilizer_quantity": 50000, "animal_feed_quantity": 100000000, "cropland_quantity": 1960000, "pasture_quantity": 700000, "irrigation_quantity": 550000}
]

df_nepal = pd.DataFrame(nepal_data)


df_nepal.to_csv("Agricultural_total_factor_productivity_USDA.csv", mode="a", index=False, header=False)
print(" Nepal data (2022–2025) appended to CSV.")


engine = create_engine("sqlite:///database.db")
df_nepal.to_sql("agricultural_productivity", con=engine, index=False, if_exists="append")
print(" Nepal data (2022–2025) imported into SQLite database.")