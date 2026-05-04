import matplotlib.pyplot as plt

def generate_graph():
    t = range(1, 50)
    stress = [1000 / (20 * x) for x in t]

    plt.plot(t, stress)
    plt.savefig("graph.png")
