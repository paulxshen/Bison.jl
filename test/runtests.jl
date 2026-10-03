# include("../src/main.jl")
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