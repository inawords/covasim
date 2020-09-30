import cruise_ship as cova

if __name__ == '__main__':
    seed = 1
    verbose = 1

    sim = cova.Sim()
    sim.set_seed(seed)
    sim.run(verbose=verbose)

    sim.plot()

    print('Done.')
