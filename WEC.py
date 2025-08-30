import pandas as pd
#load data
df= pd.read_csv("World Energy Consumption.csv")
print(df.head(10))

print(df.columns)
#Cleaning data
# Remove multiple columns
# Keep only the key columns for analysis
columns_to_keep = [
    # Biofuel / renewables
   "country", "year", "population", "gdp", "biofuel_electricity", "biofuel_share_elec", "biofuel_share_energy",
    "low_carbon_consumption", "low_carbon_electricity", "low_carbon_share_elec",
    "renewables_consumption", "renewables_electricity", "renewables_share_elec",
    "solar_consumption", "solar_electricity",
    "wind_consumption", "wind_electricity",
    "other_renewable_consumption",

    # Fossil fuels
    "coal_consumption", "coal_electricity",
    "gas_consumption", "gas_electricity",
    "oil_consumption", "oil_electricity",
    "fossil_fuel_consumption", "fossil_electricity",

    # Total energy / efficiency
    "primary_energy_consumption", "energy_cons_change_pct", "energy_cons_change_twh",
    "energy_per_capita", "energy_per_gdp",
    "electricity_generation", "electricity_demand",

    # Environmental impact
    "carbon_intensity_elec", "greenhouse_gas_emissions",

    # Optional: imports
    "net_elec_imports", "net_elec_imports_share_demand"
]

df_clean = df[columns_to_keep]

# handle missing data
df_clean = df_clean.dropna() 

print(df_clean.columns)

#remove duplicates
df_clean1 = df_clean.drop_duplicates

print(df_clean1.head(10))

# Save cleaned dataset
#df_clean.to_csv("energy_data_cleaned_no_nan.csv", index=False)

#df = pd.read_csv("energy_data_cleaned_no_nan.csv")
#print(df.info())
#print(df.describe())