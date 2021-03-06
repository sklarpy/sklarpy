# Contains univariate probability distributions
import scipy.stats

from sklarpy.univariate._dist_wrappers import *
from sklarpy.univariate._fit import *

########################################################################################################################
# Continuous (Parametric)
########################################################################################################################
continuous_parametric_names: tuple = ('alpha', 'anglit', 'arcsine', 'argus', 'beta', 'betaprime', 'bradford', 'burr', 'burr12', 'cauchy', 'chi', 'chi2', 'cosine', 'crystalball', 'dgamma', 'dweibull', 'erlang', 'expon', 'exponnorm', 'exponpow', 'exponweib', 'f', 'fatiguelife', 'fisk', 'foldcauchy', 'foldnorm', 'gamma', 'gausshyper', 'genexpon', 'genextreme', 'gengamma', 'genhalflogistic', 'genhyperbolic', 'geninvgauss', 'genlogistic', 'gennorm', 'genpareto', 'gilbrat', 'gompertz', 'gumbel_l', 'gumbel_r', 'halfcauchy', 'halfgennorm', 'halflogistic', 'halfnorm', 'hypsecant', 'invgamma', 'invgauss', 'invweibull', 'johnsonsb', 'johnsonsu', 'kappa3', 'kappa4', 'ksone', 'kstwo', 'kstwobign', 'laplace', 'laplace_asymmetric', 'levy', 'levy_l', 'levy_stable', 'loggamma', 'logistic', 'loglaplace', 'lognorm', 'loguniform', 'lomax', 'maxwell', 'mielke', 'moyal', 'nakagami', 'ncf', 'nct', 'ncx2', 'normal', 'norminvgauss', 'pareto', 'pearson3', 'powerlaw', 'powerlognorm', 'powernorm', 'rayleigh', 'rdist', 'recipinvgauss', 'reciprocal', 'rice', 'semicircular', 'skewcauchy', 'skewnorm', 't', 'trapezoid', 'trapz', 'triang', 'truncexpon', 'truncnorm', 'tukeylambda', 'uniform', 'vonmises', 'vonmises_line', 'wald', 'weibull_max', 'weibull_min', 'wrapcauchy')
common_continuous_parametric_names: tuple = ('cauchy', 'chi2', 'expon', 'gamma', 'lognorm', 'normal', 'powerlaw', 'rayleigh', 't', 'uniform')
continuous_multimodal_parametric_names: tuple = ('arcsine', 'beta')

alpha = PreFitParametricContinuousUnivariate('alpha', scipy.stats.alpha.pdf, scipy.stats.alpha.cdf, scipy.stats.alpha.ppf, scipy.stats.alpha.support, scipy.stats.alpha.fit, scipy.stats.alpha.rvs)
anglit = PreFitParametricContinuousUnivariate('anglit', scipy.stats.anglit.pdf, scipy.stats.anglit.cdf, scipy.stats.anglit.ppf, scipy.stats.anglit.support, scipy.stats.anglit.fit, scipy.stats.anglit.rvs)
arcsine = PreFitParametricContinuousUnivariate('arcsine', scipy.stats.arcsine.pdf, scipy.stats.arcsine.cdf, scipy.stats.arcsine.ppf, scipy.stats.arcsine.support, scipy.stats.arcsine.fit, scipy.stats.arcsine.rvs)
argus = PreFitParametricContinuousUnivariate('argus', scipy.stats.argus.pdf, scipy.stats.argus.cdf, scipy.stats.argus.ppf, scipy.stats.argus.support, scipy.stats.argus.fit, scipy.stats.argus.rvs)
beta = PreFitParametricContinuousUnivariate('beta', scipy.stats.beta.pdf, scipy.stats.beta.cdf, scipy.stats.beta.ppf, scipy.stats.beta.support, scipy.stats.beta.fit, scipy.stats.beta.rvs)
betaprime = PreFitParametricContinuousUnivariate('betaprime', scipy.stats.betaprime.pdf, scipy.stats.betaprime.cdf, scipy.stats.betaprime.ppf, scipy.stats.betaprime.support, scipy.stats.betaprime.fit, scipy.stats.betaprime.rvs)
bradford = PreFitParametricContinuousUnivariate('bradford', scipy.stats.bradford.pdf, scipy.stats.bradford.cdf, scipy.stats.bradford.ppf, scipy.stats.bradford.support, scipy.stats.bradford.fit, scipy.stats.bradford.rvs)
burr = PreFitParametricContinuousUnivariate('burr', scipy.stats.burr.pdf, scipy.stats.burr.cdf, scipy.stats.burr.ppf, scipy.stats.burr.support, scipy.stats.burr.fit, scipy.stats.burr.rvs)
burr12 = PreFitParametricContinuousUnivariate('burr12', scipy.stats.burr12.pdf, scipy.stats.burr12.cdf, scipy.stats.burr12.ppf, scipy.stats.burr12.support, scipy.stats.burr12.fit, scipy.stats.burr12.rvs)
cauchy = PreFitParametricContinuousUnivariate('cauchy', scipy.stats.cauchy.pdf, scipy.stats.cauchy.cdf, scipy.stats.cauchy.ppf, scipy.stats.cauchy.support, scipy.stats.cauchy.fit, scipy.stats.cauchy.rvs)
chi = PreFitParametricContinuousUnivariate('chi', scipy.stats.chi.pdf, scipy.stats.chi.cdf, scipy.stats.chi.ppf, scipy.stats.chi.support, scipy.stats.chi.fit, scipy.stats.chi.rvs)
chi2 = PreFitParametricContinuousUnivariate('chi2', scipy.stats.chi2.pdf, scipy.stats.chi2.cdf, scipy.stats.chi2.ppf, scipy.stats.chi2.support, scipy.stats.chi2.fit, scipy.stats.chi2.rvs)
cosine = PreFitParametricContinuousUnivariate('cosine', scipy.stats.cosine.pdf, scipy.stats.cosine.cdf, scipy.stats.cosine.ppf, scipy.stats.cosine.support, scipy.stats.cosine.fit, scipy.stats.cosine.rvs)
crystalball = PreFitParametricContinuousUnivariate('crystalball', scipy.stats.crystalball.pdf, scipy.stats.crystalball.cdf, scipy.stats.crystalball.ppf, scipy.stats.crystalball.support, scipy.stats.crystalball.fit, scipy.stats.crystalball.rvs)
dgamma = PreFitParametricContinuousUnivariate('dgamma', scipy.stats.dgamma.pdf, scipy.stats.dgamma.cdf, scipy.stats.dgamma.ppf, scipy.stats.dgamma.support, scipy.stats.dgamma.fit, scipy.stats.dgamma.rvs)
dweibull = PreFitParametricContinuousUnivariate('dweibull', scipy.stats.dweibull.pdf, scipy.stats.dweibull.cdf, scipy.stats.dweibull.ppf, scipy.stats.dweibull.support, scipy.stats.dweibull.fit, scipy.stats.dweibull.rvs)
erlang = PreFitParametricContinuousUnivariate('erlang', scipy.stats.erlang.pdf, scipy.stats.erlang.cdf, scipy.stats.erlang.ppf, scipy.stats.erlang.support, scipy.stats.erlang.fit, scipy.stats.erlang.rvs)
expon = PreFitParametricContinuousUnivariate('expon', scipy.stats.expon.pdf, scipy.stats.expon.cdf, scipy.stats.expon.ppf, scipy.stats.expon.support, scipy.stats.expon.fit, scipy.stats.expon.rvs)
exponnorm = PreFitParametricContinuousUnivariate('exponnorm', scipy.stats.exponnorm.pdf, scipy.stats.exponnorm.cdf, scipy.stats.exponnorm.ppf, scipy.stats.exponnorm.support, scipy.stats.exponnorm.fit, scipy.stats.exponnorm.rvs)
exponpow = PreFitParametricContinuousUnivariate('exponpow', scipy.stats.exponpow.pdf, scipy.stats.exponpow.cdf, scipy.stats.exponpow.ppf, scipy.stats.exponpow.support, scipy.stats.exponpow.fit, scipy.stats.exponpow.rvs)
exponweib = PreFitParametricContinuousUnivariate('exponweib', scipy.stats.exponweib.pdf, scipy.stats.exponweib.cdf, scipy.stats.exponweib.ppf, scipy.stats.exponweib.support, scipy.stats.exponweib.fit, scipy.stats.exponweib.rvs)
f = PreFitParametricContinuousUnivariate('f', scipy.stats.f.pdf, scipy.stats.f.cdf, scipy.stats.f.ppf, scipy.stats.f.support, scipy.stats.f.fit, scipy.stats.f.rvs)
fatiguelife = PreFitParametricContinuousUnivariate('fatiguelife', scipy.stats.fatiguelife.pdf, scipy.stats.fatiguelife.cdf, scipy.stats.fatiguelife.ppf, scipy.stats.fatiguelife.support, scipy.stats.fatiguelife.fit, scipy.stats.fatiguelife.rvs)
fisk = PreFitParametricContinuousUnivariate('fisk', scipy.stats.fisk.pdf, scipy.stats.fisk.cdf, scipy.stats.fisk.ppf, scipy.stats.fisk.support, scipy.stats.fisk.fit, scipy.stats.fisk.rvs)
foldcauchy = PreFitParametricContinuousUnivariate('foldcauchy', scipy.stats.foldcauchy.pdf, scipy.stats.foldcauchy.cdf, scipy.stats.foldcauchy.ppf, scipy.stats.foldcauchy.support, scipy.stats.foldcauchy.fit, scipy.stats.foldcauchy.rvs)
foldnorm = PreFitParametricContinuousUnivariate('foldnorm', scipy.stats.foldnorm.pdf, scipy.stats.foldnorm.cdf, scipy.stats.foldnorm.ppf, scipy.stats.foldnorm.support, scipy.stats.foldnorm.fit, scipy.stats.foldnorm.rvs)
gamma = PreFitParametricContinuousUnivariate('gamma', scipy.stats.gamma.pdf, scipy.stats.gamma.cdf, scipy.stats.gamma.ppf, scipy.stats.gamma.support, scipy.stats.gamma.fit, scipy.stats.gamma.rvs)
gausshyper = PreFitParametricContinuousUnivariate('gausshyper', scipy.stats.gausshyper.pdf, scipy.stats.gausshyper.cdf, scipy.stats.gausshyper.ppf, scipy.stats.gausshyper.support, scipy.stats.gausshyper.fit, scipy.stats.gausshyper.rvs)
genexpon = PreFitParametricContinuousUnivariate('genexpon', scipy.stats.genexpon.pdf, scipy.stats.genexpon.cdf, scipy.stats.genexpon.ppf, scipy.stats.genexpon.support, scipy.stats.genexpon.fit, scipy.stats.genexpon.rvs)
genextreme = PreFitParametricContinuousUnivariate('genextreme', scipy.stats.genextreme.pdf, scipy.stats.genextreme.cdf, scipy.stats.genextreme.ppf, scipy.stats.genextreme.support, scipy.stats.genextreme.fit, scipy.stats.genextreme.rvs)
gengamma = PreFitParametricContinuousUnivariate('gengamma', scipy.stats.gengamma.pdf, scipy.stats.gengamma.cdf, scipy.stats.gengamma.ppf, scipy.stats.gengamma.support, scipy.stats.gengamma.fit, scipy.stats.gengamma.rvs)
genhalflogistic = PreFitParametricContinuousUnivariate('genhalflogistic', scipy.stats.genhalflogistic.pdf, scipy.stats.genhalflogistic.cdf, scipy.stats.genhalflogistic.ppf, scipy.stats.genhalflogistic.support, scipy.stats.genhalflogistic.fit, scipy.stats.genhalflogistic.rvs)
genhyperbolic = PreFitParametricContinuousUnivariate('genhyperbolic', scipy.stats.genhyperbolic.pdf, scipy.stats.genhyperbolic.cdf, scipy.stats.genhyperbolic.ppf, scipy.stats.genhyperbolic.support, scipy.stats.genhyperbolic.fit, scipy.stats.genhyperbolic.rvs)
geninvgauss = PreFitParametricContinuousUnivariate('geninvgauss', scipy.stats.geninvgauss.pdf, scipy.stats.geninvgauss.cdf, scipy.stats.geninvgauss.ppf, scipy.stats.geninvgauss.support, scipy.stats.geninvgauss.fit, scipy.stats.geninvgauss.rvs)
genlogistic = PreFitParametricContinuousUnivariate('genlogistic', scipy.stats.genlogistic.pdf, scipy.stats.genlogistic.cdf, scipy.stats.genlogistic.ppf, scipy.stats.genlogistic.support, scipy.stats.genlogistic.fit, scipy.stats.genlogistic.rvs)
gennorm = PreFitParametricContinuousUnivariate('gennorm', scipy.stats.gennorm.pdf, scipy.stats.gennorm.cdf, scipy.stats.gennorm.ppf, scipy.stats.gennorm.support, scipy.stats.gennorm.fit, scipy.stats.gennorm.rvs)
genpareto = PreFitParametricContinuousUnivariate('genpareto', scipy.stats.genpareto.pdf, scipy.stats.genpareto.cdf, scipy.stats.genpareto.ppf, scipy.stats.genpareto.support, scipy.stats.genpareto.fit, scipy.stats.genpareto.rvs)
gilbrat = PreFitParametricContinuousUnivariate('gilbrat', scipy.stats.gilbrat.pdf, scipy.stats.gilbrat.cdf, scipy.stats.gilbrat.ppf, scipy.stats.gilbrat.support, scipy.stats.gilbrat.fit, scipy.stats.gilbrat.rvs)
gompertz = PreFitParametricContinuousUnivariate('gompertz', scipy.stats.gompertz.pdf, scipy.stats.gompertz.cdf, scipy.stats.gompertz.ppf, scipy.stats.gompertz.support, scipy.stats.gompertz.fit, scipy.stats.gompertz.rvs)
gumbel_l = PreFitParametricContinuousUnivariate('gumbel_l', scipy.stats.gumbel_l.pdf, scipy.stats.gumbel_l.cdf, scipy.stats.gumbel_l.ppf, scipy.stats.gumbel_l.support, scipy.stats.gumbel_l.fit, scipy.stats.gumbel_l.rvs)
gumbel_r = PreFitParametricContinuousUnivariate('gumbel_r', scipy.stats.gumbel_r.pdf, scipy.stats.gumbel_r.cdf, scipy.stats.gumbel_r.ppf, scipy.stats.gumbel_r.support, scipy.stats.gumbel_r.fit, scipy.stats.gumbel_r.rvs)
halfcauchy = PreFitParametricContinuousUnivariate('halfcauchy', scipy.stats.halfcauchy.pdf, scipy.stats.halfcauchy.cdf, scipy.stats.halfcauchy.ppf, scipy.stats.halfcauchy.support, scipy.stats.halfcauchy.fit, scipy.stats.halfcauchy.rvs)
halfgennorm = PreFitParametricContinuousUnivariate('halfgennorm', scipy.stats.halfgennorm.pdf, scipy.stats.halfgennorm.cdf, scipy.stats.halfgennorm.ppf, scipy.stats.halfgennorm.support, scipy.stats.halfgennorm.fit, scipy.stats.halfgennorm.rvs)
halflogistic = PreFitParametricContinuousUnivariate('halflogistic', scipy.stats.halflogistic.pdf, scipy.stats.halflogistic.cdf, scipy.stats.halflogistic.ppf, scipy.stats.halflogistic.support, scipy.stats.halflogistic.fit, scipy.stats.halflogistic.rvs)
halfnorm = PreFitParametricContinuousUnivariate('halfnorm', scipy.stats.halfnorm.pdf, scipy.stats.halfnorm.cdf, scipy.stats.halfnorm.ppf, scipy.stats.halfnorm.support, scipy.stats.halfnorm.fit, scipy.stats.halfnorm.rvs)
hypsecant = PreFitParametricContinuousUnivariate('hypsecant', scipy.stats.hypsecant.pdf, scipy.stats.hypsecant.cdf, scipy.stats.hypsecant.ppf, scipy.stats.hypsecant.support, scipy.stats.hypsecant.fit, scipy.stats.hypsecant.rvs)
invgamma = PreFitParametricContinuousUnivariate('invgamma', scipy.stats.invgamma.pdf, scipy.stats.invgamma.cdf, scipy.stats.invgamma.ppf, scipy.stats.invgamma.support, scipy.stats.invgamma.fit, scipy.stats.invgamma.rvs)
invgauss = PreFitParametricContinuousUnivariate('invgauss', scipy.stats.invgauss.pdf, scipy.stats.invgauss.cdf, scipy.stats.invgauss.ppf, scipy.stats.invgauss.support, scipy.stats.invgauss.fit, scipy.stats.invgauss.rvs)
invweibull = PreFitParametricContinuousUnivariate('invweibull', scipy.stats.invweibull.pdf, scipy.stats.invweibull.cdf, scipy.stats.invweibull.ppf, scipy.stats.invweibull.support, scipy.stats.invweibull.fit, scipy.stats.invweibull.rvs)
johnsonsb = PreFitParametricContinuousUnivariate('johnsonsb', scipy.stats.johnsonsb.pdf, scipy.stats.johnsonsb.cdf, scipy.stats.johnsonsb.ppf, scipy.stats.johnsonsb.support, scipy.stats.johnsonsb.fit, scipy.stats.johnsonsb.rvs)
johnsonsu = PreFitParametricContinuousUnivariate('johnsonsu', scipy.stats.johnsonsu.pdf, scipy.stats.johnsonsu.cdf, scipy.stats.johnsonsu.ppf, scipy.stats.johnsonsu.support, scipy.stats.johnsonsu.fit, scipy.stats.johnsonsu.rvs)
kappa3 = PreFitParametricContinuousUnivariate('kappa3', scipy.stats.kappa3.pdf, scipy.stats.kappa3.cdf, scipy.stats.kappa3.ppf, scipy.stats.kappa3.support, scipy.stats.kappa3.fit, scipy.stats.kappa3.rvs)
kappa4 = PreFitParametricContinuousUnivariate('kappa4', scipy.stats.kappa4.pdf, scipy.stats.kappa4.cdf, scipy.stats.kappa4.ppf, scipy.stats.kappa4.support, scipy.stats.kappa4.fit, scipy.stats.kappa4.rvs)
ksone = PreFitParametricContinuousUnivariate('ksone', scipy.stats.ksone.pdf, scipy.stats.ksone.cdf, scipy.stats.ksone.ppf, scipy.stats.ksone.support, scipy.stats.ksone.fit, scipy.stats.ksone.rvs)
kstwo = PreFitParametricContinuousUnivariate('kstwo', scipy.stats.kstwo.pdf, scipy.stats.kstwo.cdf, scipy.stats.kstwo.ppf, scipy.stats.kstwo.support, scipy.stats.kstwo.fit, scipy.stats.kstwo.rvs)
kstwobign = PreFitParametricContinuousUnivariate('kstwobign', scipy.stats.kstwobign.pdf, scipy.stats.kstwobign.cdf, scipy.stats.kstwobign.ppf, scipy.stats.kstwobign.support, scipy.stats.kstwobign.fit, scipy.stats.kstwobign.rvs)
laplace = PreFitParametricContinuousUnivariate('laplace', scipy.stats.laplace.pdf, scipy.stats.laplace.cdf, scipy.stats.laplace.ppf, scipy.stats.laplace.support, scipy.stats.laplace.fit, scipy.stats.laplace.rvs)
laplace_asymmetric = PreFitParametricContinuousUnivariate('laplace_asymmetric', scipy.stats.laplace_asymmetric.pdf, scipy.stats.laplace_asymmetric.cdf, scipy.stats.laplace_asymmetric.ppf, scipy.stats.laplace_asymmetric.support, scipy.stats.laplace_asymmetric.fit, scipy.stats.laplace_asymmetric.rvs)
levy = PreFitParametricContinuousUnivariate('levy', scipy.stats.levy.pdf, scipy.stats.levy.cdf, scipy.stats.levy.ppf, scipy.stats.levy.support, scipy.stats.levy.fit, scipy.stats.levy.rvs)
levy_l = PreFitParametricContinuousUnivariate('levy_l', scipy.stats.levy_l.pdf, scipy.stats.levy_l.cdf, scipy.stats.levy_l.ppf, scipy.stats.levy_l.support, scipy.stats.levy_l.fit, scipy.stats.levy_l.rvs)
levy_stable = PreFitParametricContinuousUnivariate('levy_stable', scipy.stats.levy_stable.pdf, scipy.stats.levy_stable.cdf, scipy.stats.levy_stable.ppf, scipy.stats.levy_stable.support, scipy.stats.levy_stable._fitstart, scipy.stats.levy_stable.rvs)  # using fit is extremely slow for levy_stable
loggamma = PreFitParametricContinuousUnivariate('loggamma', scipy.stats.loggamma.pdf, scipy.stats.loggamma.cdf, scipy.stats.loggamma.ppf, scipy.stats.loggamma.support, scipy.stats.loggamma.fit, scipy.stats.loggamma.rvs)
logistic = PreFitParametricContinuousUnivariate('logistic', scipy.stats.logistic.pdf, scipy.stats.logistic.cdf, scipy.stats.logistic.ppf, scipy.stats.logistic.support, scipy.stats.logistic.fit, scipy.stats.logistic.rvs)
loglaplace = PreFitParametricContinuousUnivariate('loglaplace', scipy.stats.loglaplace.pdf, scipy.stats.loglaplace.cdf, scipy.stats.loglaplace.ppf, scipy.stats.loglaplace.support, scipy.stats.loglaplace.fit, scipy.stats.loglaplace.rvs)
lognorm = PreFitParametricContinuousUnivariate('lognorm', scipy.stats.lognorm.pdf, scipy.stats.lognorm.cdf, scipy.stats.lognorm.ppf, scipy.stats.lognorm.support, scipy.stats.lognorm.fit, scipy.stats.lognorm.rvs)
loguniform = PreFitParametricContinuousUnivariate('loguniform', scipy.stats.loguniform.pdf, scipy.stats.loguniform.cdf, scipy.stats.loguniform.ppf, scipy.stats.loguniform.support, scipy.stats.loguniform.fit, scipy.stats.loguniform.rvs)
lomax = PreFitParametricContinuousUnivariate('lomax', scipy.stats.lomax.pdf, scipy.stats.lomax.cdf, scipy.stats.lomax.ppf, scipy.stats.lomax.support, scipy.stats.lomax.fit, scipy.stats.lomax.rvs)
maxwell = PreFitParametricContinuousUnivariate('maxwell', scipy.stats.maxwell.pdf, scipy.stats.maxwell.cdf, scipy.stats.maxwell.ppf, scipy.stats.maxwell.support, scipy.stats.maxwell.fit, scipy.stats.maxwell.rvs)
mielke = PreFitParametricContinuousUnivariate('mielke', scipy.stats.mielke.pdf, scipy.stats.mielke.cdf, scipy.stats.mielke.ppf, scipy.stats.mielke.support, scipy.stats.mielke.fit, scipy.stats.mielke.rvs)
moyal = PreFitParametricContinuousUnivariate('moyal', scipy.stats.moyal.pdf, scipy.stats.moyal.cdf, scipy.stats.moyal.ppf, scipy.stats.moyal.support, scipy.stats.moyal.fit, scipy.stats.moyal.rvs)
nakagami = PreFitParametricContinuousUnivariate('nakagami', scipy.stats.nakagami.pdf, scipy.stats.nakagami.cdf, scipy.stats.nakagami.ppf, scipy.stats.nakagami.support, scipy.stats.nakagami.fit, scipy.stats.nakagami.rvs)
ncf = PreFitParametricContinuousUnivariate('ncf', scipy.stats.ncf.pdf, scipy.stats.ncf.cdf, scipy.stats.ncf.ppf, scipy.stats.ncf.support, scipy.stats.ncf.fit, scipy.stats.ncf.rvs)
nct = PreFitParametricContinuousUnivariate('nct', scipy.stats.nct.pdf, scipy.stats.nct.cdf, scipy.stats.nct.ppf, scipy.stats.nct.support, scipy.stats.nct.fit, scipy.stats.nct.rvs)
ncx2 = PreFitParametricContinuousUnivariate('ncx2', scipy.stats.ncx2.pdf, scipy.stats.ncx2.cdf, scipy.stats.ncx2.ppf, scipy.stats.ncx2.support, scipy.stats.ncx2.fit, scipy.stats.ncx2.rvs)
normal = PreFitParametricContinuousUnivariate('normal', scipy.stats.norm.pdf, scipy.stats.norm.cdf, scipy.stats.norm.ppf, scipy.stats.norm.support, scipy.stats.norm.fit, scipy.stats.norm.rvs)
norminvgauss = PreFitParametricContinuousUnivariate('norminvgauss', scipy.stats.norminvgauss.pdf, scipy.stats.norminvgauss.cdf, scipy.stats.norminvgauss.ppf, scipy.stats.norminvgauss.support, scipy.stats.norminvgauss.fit, scipy.stats.norminvgauss.rvs)
pareto = PreFitParametricContinuousUnivariate('pareto', scipy.stats.pareto.pdf, scipy.stats.pareto.cdf, scipy.stats.pareto.ppf, scipy.stats.pareto.support, scipy.stats.pareto.fit, scipy.stats.pareto.rvs)
pearson3 = PreFitParametricContinuousUnivariate('pearson3', scipy.stats.pearson3.pdf, scipy.stats.pearson3.cdf, scipy.stats.pearson3.ppf, scipy.stats.pearson3.support, scipy.stats.pearson3.fit, scipy.stats.pearson3.rvs)
powerlaw = PreFitParametricContinuousUnivariate('powerlaw', scipy.stats.powerlaw.pdf, scipy.stats.powerlaw.cdf, scipy.stats.powerlaw.ppf, scipy.stats.powerlaw.support, scipy.stats.powerlaw.fit, scipy.stats.powerlaw.rvs)
powerlognorm = PreFitParametricContinuousUnivariate('powerlognorm', scipy.stats.powerlognorm.pdf, scipy.stats.powerlognorm.cdf, scipy.stats.powerlognorm.ppf, scipy.stats.powerlognorm.support, scipy.stats.powerlognorm.fit, scipy.stats.powerlognorm.rvs)
powernorm = PreFitParametricContinuousUnivariate('powernorm', scipy.stats.powernorm.pdf, scipy.stats.powernorm.cdf, scipy.stats.powernorm.ppf, scipy.stats.powernorm.support, scipy.stats.powernorm.fit, scipy.stats.powernorm.rvs)
rayleigh = PreFitParametricContinuousUnivariate('rayleigh', scipy.stats.rayleigh.pdf, scipy.stats.rayleigh.cdf, scipy.stats.rayleigh.ppf, scipy.stats.rayleigh.support, scipy.stats.rayleigh.fit, scipy.stats.rayleigh.rvs)
rdist = PreFitParametricContinuousUnivariate('rdist', scipy.stats.rdist.pdf, scipy.stats.rdist.cdf, scipy.stats.rdist.ppf, scipy.stats.rdist.support, scipy.stats.rdist.fit, scipy.stats.rdist.rvs)
recipinvgauss = PreFitParametricContinuousUnivariate('recipinvgauss', scipy.stats.recipinvgauss.pdf, scipy.stats.recipinvgauss.cdf, scipy.stats.recipinvgauss.ppf, scipy.stats.recipinvgauss.support, scipy.stats.recipinvgauss.fit, scipy.stats.recipinvgauss.rvs)
reciprocal = PreFitParametricContinuousUnivariate('reciprocal', scipy.stats.reciprocal.pdf, scipy.stats.reciprocal.cdf, scipy.stats.reciprocal.ppf, scipy.stats.reciprocal.support, scipy.stats.reciprocal.fit, scipy.stats.reciprocal.rvs)
rice = PreFitParametricContinuousUnivariate('rice', scipy.stats.rice.pdf, scipy.stats.rice.cdf, scipy.stats.rice.ppf, scipy.stats.rice.support, scipy.stats.rice.fit, scipy.stats.rice.rvs)
semicircular = PreFitParametricContinuousUnivariate('semicircular', scipy.stats.semicircular.pdf, scipy.stats.semicircular.cdf, scipy.stats.semicircular.ppf, scipy.stats.semicircular.support, scipy.stats.semicircular.fit, scipy.stats.semicircular.rvs)
skewcauchy = PreFitParametricContinuousUnivariate('skewcauchy', scipy.stats.skewcauchy.pdf, scipy.stats.skewcauchy.cdf, scipy.stats.skewcauchy.ppf, scipy.stats.skewcauchy.support, scipy.stats.skewcauchy.fit, scipy.stats.skewcauchy.rvs)
skewnorm = PreFitParametricContinuousUnivariate('skewnorm', scipy.stats.skewnorm.pdf, scipy.stats.skewnorm.cdf, scipy.stats.skewnorm.ppf, scipy.stats.skewnorm.support, scipy.stats.skewnorm.fit, scipy.stats.skewnorm.rvs)
# studentized_range = PreFitParametricContinuousUnivariate('studentized_range', scipy.stats.studentized_range.pdf, scipy.stats.studentized_range.cdf, scipy.stats.studentized_range.ppf, scipy.stats.studentized_range.support, scipy.stats.studentized_range.fit, scipy.stats.studentized_range.rvs)
t = PreFitParametricContinuousUnivariate('t', scipy.stats.t.pdf, scipy.stats.t.cdf, scipy.stats.t.ppf, scipy.stats.t.support, scipy.stats.t.fit, scipy.stats.t.rvs)
trapezoid = PreFitParametricContinuousUnivariate('trapezoid', scipy.stats.trapezoid.pdf, scipy.stats.trapezoid.cdf, scipy.stats.trapezoid.ppf, scipy.stats.trapezoid.support, scipy.stats.trapezoid.fit, scipy.stats.trapezoid.rvs)
trapz = PreFitParametricContinuousUnivariate('trapz', scipy.stats.trapz.pdf, scipy.stats.trapz.cdf, scipy.stats.trapz.ppf, scipy.stats.trapz.support, scipy.stats.trapz.fit, scipy.stats.trapz.rvs)
triang = PreFitParametricContinuousUnivariate('triang', scipy.stats.triang.pdf, scipy.stats.triang.cdf, scipy.stats.triang.ppf, scipy.stats.triang.support, scipy.stats.triang.fit, scipy.stats.triang.rvs)
truncexpon = PreFitParametricContinuousUnivariate('truncexpon', scipy.stats.truncexpon.pdf, scipy.stats.truncexpon.cdf, scipy.stats.truncexpon.ppf, scipy.stats.truncexpon.support, scipy.stats.truncexpon.fit, scipy.stats.truncexpon.rvs)
truncnorm = PreFitParametricContinuousUnivariate('truncnorm', scipy.stats.truncnorm.pdf, scipy.stats.truncnorm.cdf, scipy.stats.truncnorm.ppf, scipy.stats.truncnorm.support, scipy.stats.truncnorm.fit, scipy.stats.truncnorm.rvs)
tukeylambda = PreFitParametricContinuousUnivariate('tukeylambda', scipy.stats.tukeylambda.pdf, scipy.stats.tukeylambda.cdf, scipy.stats.tukeylambda.ppf, scipy.stats.tukeylambda.support, scipy.stats.tukeylambda.fit, scipy.stats.tukeylambda.rvs)
uniform = PreFitParametricContinuousUnivariate('uniform', scipy.stats.uniform.pdf, scipy.stats.uniform.cdf, scipy.stats.uniform.ppf, scipy.stats.uniform.support, scipy.stats.uniform.fit, scipy.stats.uniform.rvs)
vonmises = PreFitParametricContinuousUnivariate('vonmises', scipy.stats.vonmises.pdf, scipy.stats.vonmises.cdf, scipy.stats.vonmises.ppf, scipy.stats.vonmises.support, scipy.stats.vonmises.fit, scipy.stats.vonmises.rvs)
vonmises_line = PreFitParametricContinuousUnivariate('vonmises_line', scipy.stats.vonmises_line.pdf, scipy.stats.vonmises_line.cdf, scipy.stats.vonmises_line.ppf, scipy.stats.vonmises_line.support, scipy.stats.vonmises_line.fit, scipy.stats.vonmises_line.rvs)
wald = PreFitParametricContinuousUnivariate('wald', scipy.stats.wald.pdf, scipy.stats.wald.cdf, scipy.stats.wald.ppf, scipy.stats.wald.support, scipy.stats.wald.fit, scipy.stats.wald.rvs)
weibull_max = PreFitParametricContinuousUnivariate('weibull_max', scipy.stats.weibull_max.pdf, scipy.stats.weibull_max.cdf, scipy.stats.weibull_max.ppf, scipy.stats.weibull_max.support, scipy.stats.weibull_max.fit, scipy.stats.weibull_max.rvs)
weibull_min = PreFitParametricContinuousUnivariate('weibull_min', scipy.stats.weibull_min.pdf, scipy.stats.weibull_min.cdf, scipy.stats.weibull_min.ppf, scipy.stats.weibull_min.support, scipy.stats.weibull_min.fit, scipy.stats.weibull_min.rvs)
wrapcauchy = PreFitParametricContinuousUnivariate('wrapcauchy', scipy.stats.wrapcauchy.pdf, scipy.stats.wrapcauchy.cdf, scipy.stats.wrapcauchy.ppf, scipy.stats.wrapcauchy.support, scipy.stats.wrapcauchy.fit, scipy.stats.wrapcauchy.rvs)

# normal = PreFitContinuousUnivariate('normal', scipy.stats.norm.pdf, scipy.stats.norm.cdf, scipy.stats.norm.ppf, scipy.stats.norm.support, scipy.stats.norm.fit, scipy.stats.norm.rvs)
# all_continuous: list = scipy.stats._continuous_distns._distn_names
# all_continuous.remove('norm')
# required: tuple = ('pdf', 'cdf', 'ppf', 'support', 'fit')
# optional: tuple = ('rvs', )
# for name in all_continuous:
#     dist = eval(f"scipy.stats.{name}")
#     dist_dir = eval(f"dir(dist)")
#     has_req: bool = True
#     for req in required:
#         if req not in dist_dir:
#             has_req = False
#     if has_req:
#         s: str = f"{name} = PreFitContinuousUnivariate('{name}', scipy.stats.{name}.pdf, scipy.stats.{name}.cdf, scipy.stats.{name}.ppf, scipy.stats.{name}.support, scipy.stats.{name}.fit"
#         for opt in optional:
#             if opt in dist_dir:
#                 s += f", scipy.stats.{name}.{opt}"
#         exec(f"{s})")
#         __all__ += [name]

########################################################################################################################
# Discrete (Parametric)
########################################################################################################################
discrete_parametric_names: tuple = ('discrete_laplace', 'discrete_uniform', 'geometric', 'planck', 'poisson')
common_discrete_parametric_names: tuple = ('discrete_laplace', 'discrete_uniform', 'geometric', 'poisson')
discrete_multimodal_parametric_names: tuple = ()

discrete_laplace = PreFitParametricDiscreteUnivariate('discrete-laplace', scipy.stats.dlaplace.pmf, scipy.stats.dlaplace.cdf, scipy.stats.dlaplace.ppf, scipy.stats.dlaplace.support, dlaplace_fit, scipy.stats.dlaplace.rvs)
discrete_uniform = PreFitParametricDiscreteUnivariate('discrete-uniform', scipy.stats.randint.pmf, scipy.stats.randint.cdf, scipy.stats.randint.ppf, scipy.stats.randint.support, duniform_fit, scipy.stats.randint.rvs)
geometric = PreFitParametricDiscreteUnivariate('geometric', scipy.stats.geom.pmf, scipy.stats.geom.cdf, scipy.stats.geom.ppf, scipy.stats.geom.support, geometric_fit, scipy.stats.geom.rvs)
planck = PreFitParametricDiscreteUnivariate('planck', scipy.stats.planck.pmf, scipy.stats.planck.cdf, scipy.stats.planck.ppf, scipy.stats.planck.support, planck_fit, scipy.stats.planck.rvs)
poisson = PreFitParametricDiscreteUnivariate('poisson', scipy.stats.poisson.pmf, scipy.stats.poisson.cdf, scipy.stats.poisson.ppf, scipy.stats.poisson.support, poisson_fit, scipy.stats.poisson.rvs)


########################################################################################################################
# Numerical/Non-Parametric
########################################################################################################################
continuous_numerical_names: tuple = ('gaussian_kde', 'empirical')
discrete_numerical_names: tuple = ('discrete_empirical',)

gaussian_kde = PreFitNumericalContinuousUnivariate('gaussian-kde', kde_fit)
empirical = PreFitNumericalContinuousUnivariate('empirical', continuous_empirical_fit)
discrete_empirical = PreFitNumericalDiscreteUnivariate('discrete-empirical', discrete_empirical_fit)

########################################################################################################################
all_continuous_names: tuple = (*continuous_parametric_names, *continuous_numerical_names)
all_discrete_names: tuple = (*discrete_parametric_names, *discrete_numerical_names)
all_common_names: tuple = (*common_continuous_parametric_names, *common_discrete_parametric_names)
all_multimodal_names: tuple = (*continuous_multimodal_parametric_names, *discrete_multimodal_parametric_names)
all_parametric_names: tuple = (*continuous_parametric_names, *discrete_parametric_names)
all_numerical_names: tuple = (*continuous_numerical_names, *discrete_numerical_names)
all_distributions: tuple = (*all_continuous_names, *all_discrete_names)

distributions_map: dict = {
    'all': all_distributions,
    'all continuous': all_continuous_names,
    'all discrete': all_discrete_names,
    'all common': all_common_names,
    'all multimodal': all_multimodal_names,
    'all parametric': all_parametric_names,
    'all numerical': all_numerical_names,
    'all continuous parametric': continuous_parametric_names,
    'all discrete parametric': discrete_parametric_names,
    'all continuous numerical': continuous_numerical_names,
    'all discrete numerical': discrete_numerical_names,
    'common continuous': common_continuous_parametric_names,
    'common discrete': common_discrete_parametric_names,
    'continuous multimodal': continuous_multimodal_parametric_names,
    'discrete multimodal': discrete_multimodal_parametric_names,
}

__all__ = [*all_distributions]
