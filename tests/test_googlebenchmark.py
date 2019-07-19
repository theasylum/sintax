import io
import json

from sintax.formats import googlebenchmark


def test_json_writer():
    sample_benchmark_list = [
        {
            "cpu_time": "915000",
            "iterations": "110740",
            "name": "Fibonacci/Iterative",
            "real_time": "915000",
            "run_type": "iteration",
            "time_unit": "ns",
        }
    ]

    outfile = io.StringIO()

    googlebenchmark.json_format.writer(sample_benchmark_list, outfile)

    as_dict = json.loads(outfile.getvalue())

    assert as_dict
    assert "context" in as_dict
    assert "benchmarks" in as_dict
