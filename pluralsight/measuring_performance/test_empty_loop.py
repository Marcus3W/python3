from empty_loop import heavy_work


def test_benchmark_empty_loop(benchmark):
    benchmark(heavy_work)

