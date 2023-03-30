# Population Growth Model
This program is a Python implementation of a cohort-component method for projecting population growth based on vital statistics and total fertility rate (TFR).

## Usage
To run the population growth model, simply run the population_growth_model.py script using Python 3:

python population_growth_model.py

The script will read input data from a YAML file called input_data.yaml, which should be located in the same directory as the script. The output will be printed to the console.

## Input Data
The input_data.yaml file should contain the following input data:

base_year: The base year for the projection

projection_years: The number of years to project population growth

starting_population: The population at the beginning of the projection period

tfr: The total fertility rate for the projection period

age_specific_birth_rates: An array of age-specific birth rates for the base year

age_specific_death_rates: An array of age-specific death rates for the base year

net_migration: An array of net migration numbers for each projection year

##  Output
The script will output the projected population for each year of the projection period to the console.

##  Future Improvements
This program is a simple example of a population growth model and could be improved in several ways. For example, future versions could incorporate more advanced demographic modeling techniques, such as age-specific migration rates or variable TFRs. Additionally, the program could be expanded to incorporate data visualization tools to make it easier to interpret and present the results.
