
from rabin_miller_primality import rabin_miller_primality
from fermat_primality import fermat_primality

def composite_primality(strong_pseudoprime):
    if (fermat_primality(strong_pseudoprime)):
      if (rabin_miller_primality(strong_pseudoprime)):
        return strong_pseudoprime
      else:
        return 0
