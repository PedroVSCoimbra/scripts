mport os
import numpy
import matplotlib
from matplotlib import pyplot as plt
matplotlib.rcParams['text.usetex'] = True

eta = ['30','45','60','75','85','95']


for i in range(0,6):
    exp = 'exp' + str(i); ax = 'ax' + str(i)
    cfd = 'cfd' + str(i);
    exp = numpy.genfromtxt("data/cp-L0A4M0840-%d.csv"%i, delimiter=",", names=["x", "y"])
    cfd = numpy.genfromtxt("data/data_eta%s.csv"%eta[i], skip_header=1, skip_footer=1, delimiter=",", names=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Nu_Tilde", "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x", "Points:1", "Points:2"])
    fig, ax = plt.subplots()
    ax.plot(exp['x'], -exp['y'], 'or',markersize=2, label="Experimental")
    ax.plot(cfd['x']/0.19, -cfd['Pressure_Coefficient'], 'o',markersize=3, label="Numerical")
    ax.set_title(r'Cp vs x/c at $\eta=%s$'%eta[i])
    ax.set_xlabel("x/c")
    ax.set_ylabel("Cp")
    ax.legend()
    #  plt.figtext(.8, .5, r'Cp vs x/c para $\alpha=0$ $\lambda=0$ $\eta=%s$ Re = 2.500.000 Ma 0.840'%eta[i])
    plt.savefig('plots/cp%s-final.pdf'%eta[i])

# Make a pdf of With the plots
os.system('pdfunite plots/*final.pdf plots/simple_report.pdf')
