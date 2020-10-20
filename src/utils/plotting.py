import covasim as cv


def simple_plot(sim):
    """create simple plot after running simulation with sim.run()"""
    sim.plot()


def interactive_browser_plots(sim):
    """create interactive browser plots after running simulation with sim.run()"""
    cv.plotting.plotly_sim(sim, do_show=True)
    cv.plotting.plotly_people(sim, do_show=True)
