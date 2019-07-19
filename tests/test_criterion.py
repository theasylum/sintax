from pathlib import Path

from sintax.formats import criterion


def test_build_results(fixture_directory):
    test_csv = Path(fixture_directory) / "valid_criterion.csv"

    output = list(criterion._build_results(test_csv))

    assert len(output) == 3
    assert output[0] == {
        "cpu_time": "915000",
        "iterations": "110740",
        "name": "Fibonacci/Iterative",
        "real_time": "915000",
        "run_type": "iteration",
        "time_unit": "ns",
    }


def test_build_results_invalid_file(fixture_directory):
    test_csv = Path(fixture_directory) / "invalid_criterion.csv"

    output = list(criterion._build_results(test_csv))

    assert output == []


def test_reader_calls_build_results(fixture_directory, monkeypatch):
    paths = []

    def _build_results(path, *, aggregate=False):
        paths.append(path)
        yield {}

    test_criterion = Path(fixture_directory) / "criterion"
    monkeypatch.setattr(criterion, "_build_results", _build_results)

    output = list(criterion.reader(test_criterion))

    assert len(output) == 4
    assert len(paths) == 4


def test_reader(fixture_directory):
    test_criterion = Path(fixture_directory) / "criterion"

    output = list(criterion.reader(test_criterion))

    assert len(output) == 400
