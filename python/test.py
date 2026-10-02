from python.bison.main import *
import numpy as np

model={
    "name": "Claudette",
    "params": np.ones((5, 5, 5), dtype=np.float32),
    "activations": [np.ones((5, 5), dtype=np.float32), np.ones((5, 5), dtype=np.float32)],
    "meta": {"runs": 7, "signature": "abc"}
}

dump("model.json", model)
m = load("model.json")

assert m["params"].dtype == np.float32 #  arrays are loaded with their original dtypes
assert m["activations"][0].shape == (5, 5)  # nested arrays are loaded correctly
assert m["meta"]["runs"] == 7
