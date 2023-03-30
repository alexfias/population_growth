import yaml
import numpy as np

# Load input data from YAML file
with open('input_data.yaml', 'r') as stream:
    input_data = yaml.safe_load(stream)

# Extract input data from dictionary
base_year = input_data['base_year']
projection_years = input_data['projection_years']
starting_population = input_data['starting_population']
tfr = input_data['tfr']
age_specific_birth_rates = np.array(input_data['age_specific_birth_rates'])
age_specific_death_rates = np.array(input_data['age_specific_death_rates'])
net_migration = np.array(input_data['net_migration'])

# Calculate population by age and sex for base year
male_population = starting_population * 0.5 * np.exp(-np.cumsum(age_specific_death_rates))
female_population = starting_population * 0.5 * np.exp(-np.cumsum(age_specific_death_rates))
total_population = male_population + female_population

# Project future births and deaths
future_births = np.zeros(projection_years)
future_deaths = np.zeros(projection_years)

for i in range(projection_years):
    # Calculate expected number of births for each age group
    expected_births = tfr * age_specific_birth_rates * female_population / 1000
    
    # Calculate expected number of deaths for each age group
    expected_deaths = age_specific_death_rates * total_population / 1000
    
    # Add net migration to population
    total_population += net_migration[i]
    male_population = total_population * 0.5 * np.exp(-np.cumsum(age_specific_death_rates))
    female_population = total_population * 0.5 * np.exp(-np.cumsum(age_specific_death_rates))
    
    # Calculate number of births and deaths for this projection year
    future_births[i] = expected_births.sum()
    future_deaths[i] = expected_deaths.sum()

# Calculate future population
future_population = np.zeros(projection_years+1)
future_population[0] = starting_population

for i in range(projection_years):
    future_population[i+1] = future_population[i] + future_births[i] - future_deaths[i] + net_migration[i]

print("Projected population for base year", base_year, "is", int(future_population[0]))
for i in range(projection_years):
    print("Projected population for year", base_year+i+1, "is", int(future_population[i+1]))
