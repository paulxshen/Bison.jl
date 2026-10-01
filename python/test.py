from main import load

m = load("model.tar")  # file written by the Julia code
assert m["params"].shape == (5, 5, 5)  # True
