burnin, thin = 500, 10
blobs = np.swapaxes(np.array(sampler_blobs.blobs), 0, 1)[:, burnin::thin, :]
chain = sampler_blobs.chain[:, burnin::thin, :]
posterior_dict = {"mu": chain[:, :, 0], "tau": chain[:, :, 1], "eta": chain[:, :, 2:]}
stats_dict = {"log_likelihood": blobs}
emcee_data = az.from_dict(
    posterior=posterior_dict,
    sample_stats=stats_dict,
    coords={"school": range(8)},
    dims={"eta": ["school"], "log_likelihood": ["school"]}
)
