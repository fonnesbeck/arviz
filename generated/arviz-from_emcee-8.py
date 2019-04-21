loo_stats = az.loo(emcee_data, reff=reff, pointwise=True)
az.plot_khat(loo_stats.pareto_k)
