# pyquantumclifford

Thin Python wrapper for `QuantumClifford.jl` and `QuantumClifford.ECC` using the JuliaPy stack.

## Usage

```python
import numpy as np
from pyquantumclifford import QuantumClifford, ECC

# Create an empty tableau and stabilizer
from juliacall import Main as jl

empty_tab = QuantumClifford.Tableau(
    jl.zeros(jl.UInt8, 0),
    0,
    jl.zeros(jl.UInt8, 0, 0),
)
stabilizer = QuantumClifford.Stabilizer(empty_tab)

# Simple ECC code
code = ECC.Shor9()

# Access parity checks and matrices
ECC.parity_checks(ECC.Shor9())
ECC.parity_matrix(ECC.Shor9())
np.array(ECC.parity_matrix(ECC.Shor9()))
```

## Notes

- Julia dependencies are declared in `juliapkg.json` and installed by JuliaPkg.
- `juliacall` provides access to Julia modules from Python.
