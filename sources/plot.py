from matplotlib import pyplot as plt


def plot(data, ticks, title=None, xlabel=None, ylabel=None, png=None, graphics=True):

    plt.plot(ticks, data, "o-")

    plt.title(title)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # plt.xlim(left=0)
    # plt.ylim(bottom=0)

    plt.grid(True)

    if png != None:
        plt.savefig(png)

    if graphics:
        plt.show()

    plt.close()
