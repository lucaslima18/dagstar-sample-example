import requests, csv
from dagster import op, get_dagster_logger

logger = get_dagster_logger()

@op
def download_cereals():
    try:
        response = requests.get("https://docs.dagster.io/assets/cereal.csv")
        lines = response.text.split("\n")
        return [row for row in csv.DictReader(lines)]
    
    except Exception as err:
        logger.error(err)

@op
def find_sugariest(cereals):
    sorted_by_sugar = sorted(cereals, key=lambda cereal: cereal["sugars"])
    logger.info(f'{sorted_by_sugar[-1]["name"]} is the sugariest cereal')

@op
def find_highest_calorie_cereal(cereals):
    sorted_cereals = list(sorted(cereals, key=lambda cereal: cereal["calories"]))
    return sorted_cereals[-1]["name"]

@op
def find_highest_protein_cereal(cereals):
    sorted_cereals = list(sorted(cereals, key=lambda cereal: cereal["protein"]))
    return sorted_cereals[-1]["name"]

@op
def display_results(most_calories, most_protein):
    logger.info(f"Most caloric cereal: {most_calories}")
    logger.info(f"Most protein-rich cereal: {most_protein}")



