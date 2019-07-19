"""
Reads Criterion "raw.csv" files, and returns the resulting input into a
dictionary that can be further manipulated.

Criterion stores results as follows:

    $PROJECT/target/criterion/{benchmark group}/{function name}/
        {value passed to function (parameters)}/

    Inside that folder there are two other folders, named:

    - base: This is the results from the previous or first run
    - new: This is the most current results from the current run

    We basically have to walk the directory tree, find each of the raw.csv
    files inside the new folder, and then parse that.

    Criterion runs the same benchmark function multiple times, with multiple
    iteration counts, mainly to get a good statistical sampling. This means the
    .csv files contain 1 or more entries.
"""

import csv
import os
from pathlib import Path


def _name(group, function, value):
    if value:
        return f"{group}/{function}/{value}"

    return f"{group}/{function}"


def _build_results(path, *, aggregate=False):
    """
    Reads a CSV file and returns the results as dictionaries one by one, if the
    file is not a valid Criterion .csv we ignore it, and return None
    """
    with open(path, newline="") as raw_csv:
        header = raw_csv.readline()

        if header.strip() != "group,function,value,sample_time_nanos,iteration_count":
            return

        criterion_csv = csv.DictReader(
            raw_csv,
            fieldnames=(
                "group",
                "function",
                "value",
                "sample_time_nanos",
                "iteration_count",
            ),
        )

        for row in criterion_csv:
            yield {
                "name": _name(row["group"], row["function"], row["value"]),
                "iterations": row["iteration_count"],
                # Criterion doesn't differentiate between real time that has
                # expired vs the amount of CPU time used, so we just set them
                # to be the same
                "real_time": row["sample_time_nanos"],
                "cpu_time": row["sample_time_nanos"],
                "time_unit": "ns",
                "run_type": "iteration",
            }


def reader(path, *, aggregate=False):
    """
    Yields results for reach of the raw.csv files found in the path provided.
    Unfortunately the files are not collected together into a single location
    by default.
    """

    for root, dirs, files in os.walk(path):
        if {"new", "base"} <= set(dirs):
            # We are now inside a test directory where we want to read new/raw.csv
            yield from _build_results(
                Path(root) / "new" / "raw.csv", aggregate=aggregate
            )
        else:  # pragma: nocover (bug in coverage)
            continue
