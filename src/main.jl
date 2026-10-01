using JSON, NPZ, OrderedCollections, Tar
const _A="_REF_"
const _D="_._"

_dump(_, x) = x
function _dump(p, d::Union{AbstractDict,NamedTuple},)
    OrderedDict(map(keys(d)) do k
        v=d[k]
        k => _dump("$(p)$_D$k", v)
    end)
end
function _dump(p, a::AbstractArray{<:Number})
    name = "$(p).npy"
    npzwrite(name, a)
    basename(name)
end
function _dump(p, a::Union{Tuple,AbstractVector})
    map(enumerate(a)) do (i, a)
        _dump("$p$_D$(i-1)", a)
    end
end
function dump(p, d::Union{AbstractDict,NamedTuple},)
    tar=false
    if endswith(p, ".tar")
        p=p[1:(end-4)]
        tar=true
    end

    DAT = "$p.dat"
    rm(DAT; recursive=true, force=true)
    mkpath(DAT)

    open(p, "w") do io
        write(io, JSON.json(NamedTuple(map(keys(d)) do k
            v=d[k]
            k = Symbol(k)
            k => _dump(joinpath(DAT, "$_A$k"), v)
        end)))
    end

    if tar
        TAR = "$p.tar"
        TMP=mktempdir()
        mv(p, joinpath(TMP, p))
        mv(DAT, joinpath(TMP, DAT))
        Tar.create(TMP, TAR)
        rm(TMP; recursive=true, force=true)
    end
end

_load(p, x) = x
function _load(p, x::String)
    if startswith(x, _A)
        # x=x[6:end]
        endswith(x, ".npy") && return npzread(joinpath(p, x))
    end
    x
end
_load(p, x::AbstractVector) = _load.((p,), x)
_load(p, x::Union{AbstractDict,NamedTuple}) = OrderedDict([k => _load(p, v) for (k, v) in pairs(x)])


function load(p)
    tar=false
    if endswith(p, ".tar")
        TAR=p
        p=p[1:(end-4)]
        tar=true
    end

    if tar
        TMP=mktempdir()
        Tar.extract(TAR, TMP)
        p=joinpath(TMP, p)
    end
    DAT = "$p.dat"

    d=JSON.parse(read(p, String); dicttype=OrderedDict)
    r = OrderedDict(map(keys(d)|>collect) do k
        v=d[k]
        k => _load(DAT, v)
    end)
    tar && rm(TMP; force=true, recursive=true)
    r
end

