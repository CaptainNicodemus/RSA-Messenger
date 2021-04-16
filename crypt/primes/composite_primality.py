
import rabin_miller_primality as rmp
import fermat_primality as fp

def composite_primality(strong_pseudoprime):
    #rint("In composite_primality")
    if fp.fermat_primality(strong_pseudoprime):
      if rmp.rabin_miller_primality(strong_pseudoprime):
        return True
    else:
      return False
