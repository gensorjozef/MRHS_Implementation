from ctypes import POINTER,c_longlong

class SolverReport:
    def __init__(self, results: POINTER(c_longlong),
                 run_time: float,
                 xors: POINTER(c_longlong),
                 solutions_count: POINTER(c_longlong),
                 save_results: int = 0):
        self.results: list[int] = []

        save_count = 0
        if save_results < solutions_count.contents.value:
            save_count = save_results
        else:
            save_count = solutions_count.contents.value
        if save_count > 0:
            self.results = [results[i].value for i in range(save_count)]

        self.run_time: float = run_time
        self.xor_count: int = xors.contents.value
        self.found_solutions: int = solutions_count.contents.value

    def print_results(self):
        print("Found solutions: {}".format(self.found_solutions))
        print("Xors used: {}".format(self.xor_count))
        print("Runtime (s): {}".format(self.run_time))

    def get_solution(self) -> int:
        if len(self.results) <= 0:
            return None

        while True:
            for solution in self.results:
                yield solution
            return None
