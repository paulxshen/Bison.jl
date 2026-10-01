# Bison
JSON superset with efficient storage of arrays and objects. Dumps and loads dictionary as *.json file which stores primitives as is and arrays as references (to serialized .npa in *.json.dat folder). Handles arbitrary array and object nesting in dictionaries, tuples and lists.

Available in Python, Julia (C++, Rust todo). Works on Linux, Windows and MacOS.

Paul Shen <pxshen@alumni.stanford.edu>

## Julia
```julia
using Bison

T=Float32
m=(;
    name="Claudette",
    params=ones(T, 5, 5, 5),
    activations=[ones(T, 5, 5), ones(T, 5, 5)],
    meta=(; runs=7, signature="abc")
)

dump("m.json", m)
m1=load("m.json")

@assert eltype(m1["params"])==T #
@assert size(m1["activations"][1])==(5, 5)
```