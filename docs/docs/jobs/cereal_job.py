
from dagster import job
from docs.docs.ops.cereals_ops import (
    download_cereals,
    find_highest_calorie_cereal,
    find_highest_protein_cereal,
    display_results
)

@job
def diamond():
    cereals = download_cereals()
    display_results(
        find_highest_calorie_cereal(cereals),
        find_highest_protein_cereal(cereals)
    )
