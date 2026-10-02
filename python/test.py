import main as ms
import numpy as np

model={
    "name": "Claudette",
    "params": np.ones((5, 5, 5)),
    "activations": [np.ones((5, 5)), np.ones((5, 5))],
    "meta": {"runs": 7, "signature": "abc"}
}

ms.dump("model.tar", model)
m = ms.load("model.tar")  

assert m["activations"][0].shape == (5, 5)  # nested numpy arrays are loaded correctly
assert m["meta"]["runs"] == 7
