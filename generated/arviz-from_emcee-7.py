if emcee.__version__[0] == '3':
    ess=(draws-burnin)/sampler.get_autocorr_time(quiet=True, discard=burnin, thin=thin)
else:
    # to avoid error while generating the docs, the ess value is hard coded, it
    # should be calculated with:
    # ess = chain.shape[1] / emcee.autocorr.integrated_time(chain)
    ess = (draws-burnin)/30
reff = np.mean(ess) / (nwalkers * chain.shape[1])
