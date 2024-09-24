from antennae import test_antennae
from mars_planner import *
from routefinder import test_route_finder
import antennae

if __name__ == "__main__":
    test_mars_planner()
    print("-----------------------------")
    test_route_finder()
    print("-----------------------------")
    test_antennae()
    pass