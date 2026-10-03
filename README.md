# Bison
JSON superset with efficient storage of arrays and objects. Dumps and loads dictionary as *.json file which stores primitives as is and arrays as references (to serialized .npa in *.json.dat folder). Handles arbitrary array and object nesting in dictionaries, tuples and lists.

Cross-language: Python, Julia 

Todo
- C++, Rust 
- object pickling in python

## Python
`pip install bisonpy`
```python
import bison as bs
import numpy as np

m = {
    "name": "Claudette",
    "params": np.ones((5, 5, 5), dtype=np.float32),
    "activations": [np.ones((5, 5), dtype=np.float32)],
    "meta": {"runs": 7, "signature": "abc"},
}

bs.dump("m.json", m)
m1 = bs.load("m.json")

assert m1["params"].dtype == np.float32 # arrays are loaded with their original dtypes
assert m1["activations"][0].shape == (5, 5) # nested arrays are loaded correctly
assert m1["meta"]["runs"] == 7
```

Alternatively, use a `.tar` filename to store the JSON file and its serialized data together in a tar archive:
```python
bs.dump("m.tar", m)
m1 = bs.load("m.tar")
```


## Julia
`]add Bison`
```julia
using Bison

T=Float32
m=(;
    name="Claudette",
    params=ones(T, 5, 5, 5),
    activations=[ones(T, 5, 5), ones(T, 5, 5)],
    meta=(; runs=7, signature="abc")
)

Bison.dump("m.json", m)
m1=Bison.load("m.json")

@assert eltype(m1["params"])==T #
@assert size(m1["activations"][1])==(5, 5)
```

Paul Shen <pxshen@alumni.stanford.edu>
