var_names = ['mu', 'tau']+['eta{}'.format(i) for i in range(J)]
emcee_data = az.from_emcee(sampler, var_names=var_names)
