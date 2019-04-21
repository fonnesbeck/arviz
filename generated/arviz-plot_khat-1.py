import arviz as az
centered_eight = az.load_arviz_data('centered_eight')
pareto_k = az.loo(centered_eight, pointwise=True)['pareto_k']
az.plot_khat(pareto_k)
