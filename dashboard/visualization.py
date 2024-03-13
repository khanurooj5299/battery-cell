from impedance import preprocessing
from impedance.models.circuits import CustomCircuit
import matplotlib.pyplot as plt
import io
import base64

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
    circuit.plot(f_data=frequencies, Z_data=Z, kind='bode')
    context['parameters'] = circuit.parameters_

    # CREATE BODE PLOT
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)
    plot_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()
    context['plot']="data:image/png;base64,"+plot_base64

    #assume max Rb to be 0.2 ohms
    R_b_max = 0.2
    context['health_percentage'] = (circuit.parameters_[0]/R_b_max)*100
    context['degraded_percentage'] = 100 - context['health_percentage']
    return context
