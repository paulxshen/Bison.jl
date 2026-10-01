module MASON

"""
    hello(who::String)

Return "Hello, `who`".
"""
hello(who::String) = "Hello, $who"

include("main.jl")
export dump, load, spill
end # module MASON
