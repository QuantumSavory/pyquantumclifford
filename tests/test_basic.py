import numpy as np
from juliacall import Main as jl

from pyquantumclifford import ECC, QuantumClifford


def test_imports():
    assert QuantumClifford is not None
    assert ECC is not None


def test_basic_types():
    empty_tab = QuantumClifford.Tableau(
        jl.zeros(jl.UInt8, 0),
        0,
        jl.zeros(jl.UInt8, 0, 0),
    )
    stabilizer = QuantumClifford.Stabilizer(empty_tab)
    assert QuantumClifford.nqubits(stabilizer) == 0

    code = ECC.Shor9()
    assert ECC.code_n(code) == 9

    checks = ECC.parity_checks(code)
    assert QuantumClifford.nqubits(checks) == 9

    parity = ECC.parity_matrix(code)
    parity_np = np.array(parity)
    assert parity_np.shape[1] == 18
