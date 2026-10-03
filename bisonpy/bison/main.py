import json, os, shutil, tarfile, tempfile
import numpy as np

_A = "_REF_"
_D = "_._"
PRIMITIVE_TYPES = (int, float, str, bool, bytes, type(None))

def _dump(p, x):
    if isinstance(x, dict):
        return {k: _dump(f"{p}{_D}{k}", v) for k, v in x.items()}
    if isinstance(x, np.ndarray):
        if np.issubdtype(x.dtype, np.number) or np.issubdtype(x.dtype, np.bool_):
            name = f"{p}.npy"
            np.save(name, x)
            return os.path.basename(name)
        return [_dump(f"{p}{_D}{i}", a) for i, a in enumerate(x)]
    if isinstance(x, (list, tuple)):
        return [_dump(f"{p}{_D}{i}", a) for i, a in enumerate(x)]
    return x



def dump(p, d):
    archive = p.endswith(".tar")
    if archive:
        p = p[:-4]

    data = f"{p}.dat"
    shutil.rmtree(data, ignore_errors=True)
    os.makedirs(data)

    out = {k: _dump(os.path.join(data, f"{_A}{k}"), v) for k, v in d.items()}
    with open(p, "w") as f:
        json.dump(out, f)

    if archive:
        with tempfile.TemporaryDirectory() as tmp:
            shutil.move(p, os.path.join(tmp, os.path.basename(p)))
            shutil.move(data, os.path.join(tmp, os.path.basename(data)))
            with tarfile.open(f"{p}.tar", "w") as t:
                for fn in sorted(os.listdir(tmp)):
                    t.add(os.path.join(tmp, fn), arcname=fn)
    elif os.path.exists(f"{p}.tar"):
        os.remove(f"{p}.tar")


def _load(d, x):
    if isinstance(x, str):
        if x.startswith(_A) and x.endswith(".npy"):
            return np.load(os.path.join(d, x))
        return x
    if isinstance(x, list):
        return [_load(d, v) for v in x]
    if isinstance(x, dict):
        return {k: _load(d, v) for k, v in x.items()}
    return x


def load(p):
    archive = p.endswith(".tar")
    if archive:
        p = p[:-4]

    if archive:
        with tempfile.TemporaryDirectory() as tmp:
            with tarfile.open(f"{p}.tar") as t:
                t.extractall(tmp)
            extracted = os.path.join(tmp, os.path.basename(p))
            data = f"{extracted}.dat"
            with open(extracted) as f:
                d = json.load(f)
            return {k: _load(data, v) for k, v in d.items()}

    with open(p) as f:
        d = json.load(f)
    return {k: _load(f"{p}.dat", v) for k, v in d.items()}


def spill(p, d):
    1


jload = load
