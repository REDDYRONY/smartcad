import matplotlib.pyplot as plt

def generate_graph():
    t = range(1, 50)
    stress = [1000 / (20 * x) for x in t]

    plt.plot(t, stress)
    plt.xlabel("Thickness")
    plt.ylabel("Stress")
    plt.title("Stress vs Thickness")
    plt.savefig("graph.png")
