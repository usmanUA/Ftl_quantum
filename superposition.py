# NOTE: Import libraries

from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
import numpy as np

# NOTE: intialize a circuit with a single-qubit
qc = QuantumCircuit(1)
# NOTE: apply hadamard gate on the single qubit's state
qc.h(0)
# NOTE: measure the state of the qubit in superposition
qc.measure_all()
# NOTE: Draw the circuit in a file
qc.draw('mpl', filename='circuit.png') # NOTE: The circuit contains a qubit and hadamard gate

# NOTE: Init the simulaotr
sim = AerSimulator()
# NOTE: transpile (compile in classical computer codes) the circuit
# NOTE: transpilation optimizes the circuit and makes it compatible with the hardware
# NOTE: the programming level stays the same, gates remain the same.
# NOTE: In classical programs compliation translates the higher-level code into low-level assembly code?
qc_transpiled = transpile(qc, sim)
# NOTE: run the circtuit on the simulator for 500 shots
job = sim.run(qc_transpiled, shots=500)
results = job.result()
counts = results.get_counts()
plot_histogram(counts)
