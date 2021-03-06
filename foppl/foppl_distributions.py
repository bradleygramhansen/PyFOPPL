#
# (c) 2017, Tobias Kohn
#
# 21. Dec 2017
# 22. Dec 2017
#
discrete_distributions = {
    "Bernoulli",
    "Categorical",
    "Discrete",
    "Multinomial",
    "Poisson"
}

continuous_distributions = {
    "Beta",
    "Cauchy",
    "Dirichlet",
    "Exponential",
    "Gamma",
    "HalfCauchy",
    "LogNormal",
    "MultivariateNormal",
    "Normal",
    "Uniform"
}

distribution_map = {
    "bernoulli": "Bernoulli",
    "beta": "Beta",
    "categorical": "Categorical",
    "cauchy": "Cauchy",
    "dirichlet": "Dirichlet",
    "exponential": "Exponential",
    "gamma": "Gamma",
    "half_cauchy": "HalfCauchy",
    "log_normal": "LogNormal",
    "multinomial": "Multinomial",
    "mvn": "MultivariateNormal",
    "normal": "Normal",
    "poisson": "Poisson",
    "uniform": "Uniform"
}

distribution_params = {
    "Bernoulli": ["ps"],
    "Beta": ["alpha", "beta"],
    "Categorical": ["ps"],
    "Cauchy": ["mu", "gamma"],
    "Dirichlet": ["alpha"],
    "Exponential": ["lambda"],
    "LogNormal": ["mu", "sigma"],
    "Gamma": ["alpha", "beta"],
    "HalfCauchy": ["mu", "gamma"],
    "Multnomial": ["ps", "n"],
    "MultivariateNormal": ["mu", "cov"],
    "Normal": ["mu", "sigma"],
    "Poisson": ["lam"],
    "Uniform": ["a", "b"]
}