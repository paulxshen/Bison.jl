include("main.jl")
model=(;
    name="Claudette",
    params=ones(5, 5, 5),
    activations=[ones(5), ones(5)],
    meta=(; runs=7, signature="abc")
)
dump("model.tar", model)
model2=load("model.tar")