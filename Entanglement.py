from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0,1)
qc.measure_all()
qc.draw('mpl', filename='circuit.png')

sim = AerSimulator()
qc_transpiled = transpile(qc)
job = sim.run(qc_transpiled)
results = job.result()
counts = results.get_counts()
plot_histogram(counts)

