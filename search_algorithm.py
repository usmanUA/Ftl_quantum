from qiskit import QuantumCircuit, transpile, ClassicalRegister, QuantumRegister
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit_aer import AerSimulator
import math

# NOTE: Oracle to mark |0000>
def oracle_0000():
    '''
    Creates Oracle to find state |0000>.
    Parameters
    ----------
    register: Register of input qubits.
    solution: The true marked state.
    Return
    ------
    Quanttum Circuit based on the oracle.
    '''
    n = 4
    oracle = QuantumCircuit(n)
    oracle.x(range(n))
    oracle.h(n-1)
    oracle.mcx(list(range(n-1)), n-1)
    oracle.h(n-1)
    oracle.x(range(n))
    return oracle

# NOTE: Oracle to mark |101>
def oracle_101():
    '''
    Creates Oracle to find state |101>.
    Parameters
    ----------
    register: Register of input qubits.
    solution: The true marked state.
    Return
    ------
    Quantum Circuit based on the oracle.
    '''
    n = 3
    oracle = QuantumCircuit(n)
    oracle.x(1)
    oracle.h(2)
    oracle.mcx([0,1], 2)
    oracle.h(2)
    oracle.x(1)
    return oracle

# NOTE: Diffusor to amplify the solution state
def diffuser(n):
    '''

    '''
    diffuser = QuantumCircuit(n)
    diffuser.h(range(n))
    diffuser.x(range(n))
    diffuser.h(n-1)
    diffuser.mcx(list(range(n-1)), n-1)
    diffuser.h(n-1)
    diffuser.x(range(n))
    diffuser.h(range(n))
    return diffuser

# NOTE: Apply the algorithm 
def search_algorithm(n, oracle, diffuser):
    '''

    '''
    qc = QuantumCircuit(n,n)
    qc.h(range(n))
    N = 2 ** n
    iters = (math.pi / 4) * math.sqrt(N)
    iters = math.floor(iters)
    for _ in range(iters):
        qc.append(oracle, range(n))
        qc.append(diffuser, range(n))
    qc.measure(range(n),range(n))
    return qc

# NOTE: Quantum Circuit to manipulate the search algorithm
oracle = oracle_101().to_gate()
diffuser = diffuser(3).to_gate()
qc = search_algorithm(3, oracle, diffuser)

# NOTE: Simulate the quantum measurements
aer = AerSimulator()
transpiled = transpile(qc,aer)

# NOTE: Results and counts of the states
results = aer.run(transpiled).result()
counts = results.get_counts()

plot_histogram(counts)
