import imp
from dagster import repository

from jobs.cereal_job import diamond


@repository
def docs():
    """
    The repository definition for this docs Dagster repository.

    For hints on building your Dagster repository, see our documentation overview on Repositories:
    https://docs.dagster.io/overview/repositories-workspaces/repositories
    """
    jobs = [diamond]
    schedules = []
    sensors = []

    return jobs + schedules + sensors
