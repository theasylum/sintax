import datetime
import json


class json_format:
    @staticmethod
    def writer(benchmarks, output):
        benchmark_dict = {
            "context": {
                "date": datetime.datetime.utcnow().isoformat(sep="-"),
                "num_cpus": "unknown",
                "mhz_per_cpu": "unknown",
                "cpu_scaling_enabled": "unknown",
                "build_type": "unknown",
            },
            "benchmarks": [
                {
                    "cpu_time": benchmark["cpu_time"],
                    "iterations": benchmark["iterations"],
                    "name": benchmark["name"],
                    "real_time": benchmark["real_time"],
                    "run_type": benchmark["run_type"],
                    "time_unit": benchmark["time_unit"],
                }
                for benchmark in benchmarks
            ],
        }

        output.write(json.dumps(benchmark_dict))

    @staticmethod
    def reader(path, *, aggregate=False):
        raise NotImplementedError()


class csv_format:
    @staticmethod
    def writer(benchmarks, output):
        raise NotImplementedError()

    @staticmethod
    def reader(path, *, aggregate=False):
        raise NotImplementedError()
