from .kyber import Kyber

DEFAULT_PARAMETERS = {
    "anadil_kyber_1": {
        "k": 3,
        "n": 256,
        "q": 3329,
        "eta_1": 2,
        "eta_2": 2,
        "eta_3": 1,
        "eta_4": 1,
    },
    "anadil_kyber_2": {
        "k": 4,
        "n": 256,
        "q": 3329,
        "eta_1": 2,
        "eta_2": 2,
        "eta_3": 1,
        "eta_4": 1,
    },
    "anadil_kyber_3": {
        "k": 5,
        "n": 256,
        "q": 3329,
        "eta_1": 1,
        "eta_2": 2,
        "eta_3": 1,
        "eta_4": 1,
    },
}
"""
Lattice parameters for the Kyber key exchange.

To be used for initialisation of :py:obj:`.Kyber` objects.
"""

# Initialise with default parameters for easy import
AnaDil_Kyber1 = Kyber(DEFAULT_PARAMETERS["anadil_kyber_1"])

AnaDil_Kyber2 = Kyber(DEFAULT_PARAMETERS["anadil_kyber_2"])

AnaDil_Kyber3 = Kyber(DEFAULT_PARAMETERS["anadil_kyber_3"])

