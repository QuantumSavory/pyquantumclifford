# pyquantumclifford

Thin Python wrapper for [`QuantumClifford.jl`](https://qc.quantumsavory.org/stable/) and [`QuantumClifford.ECC`](https://qc.quantumsavory.org/stable/ECC_API/) using the JuliaPy stack.
Supports extremely fast Stabilizer state simulations, weakly non-Clifford dynamics, and generation of many modern quantum error correcting codes.

## Usage

```python
import numpy as np
from pyquantumclifford import QuantumClifford, ECC

# Optional, for calling arbitrary Julia code
from juliacall import Main as jl

# Simple ECC code
code = ECC.Shor9()

# Access parity checks and matrices
ECC.parity_checks(ECC.Shor9())
ECC.parity_matrix(ECC.Shor9())
np.array(ECC.parity_matrix(ECC.Shor9()))
```

## Notes

- Windows is not supported due to the Oscar computer algebra system being unavailable on it.
- Julia dependencies are declared in `juliapkg.json` and installed by JuliaPkg.
- `juliacall` provides access to Julia modules from Python.
