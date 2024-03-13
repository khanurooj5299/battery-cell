from impedance import preprocessing
from impedance.models.circuits import CustomCircuit
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objs as go

def getContext(datasetFile):
    context = {}

    # IMPORT THE DATA
    frequencies, Z = preprocessing.readCSV(datasetFile)
    # keep only the impedance data in the first quandrant
    frequencies, Z = preprocessing.ignoreBelowX(frequencies, Z)

    # DEFINE IMPEDANCE MODEL
    circuit = 'R0-p(R1,C1)-p(R2-Wo1,C2)'
    initial_guess = [.01, .01, 100, .01, .05, 100, 1]
    circuit = CustomCircuit(circuit, initial_guess=initial_guess)

    # FIT THE IMPEDANCE DATA TO MODEL
    circuit.fit(frequencies, Z)

    # log_frequencies = np.log10(frequencies)
    # log_impedance_values = np.log10(Z)
    # magnitude_trace = go.Scatter(x=log_frequencies, y=log_impedance_values, mode='lines', name='Magnitude (dB)')
    return context
