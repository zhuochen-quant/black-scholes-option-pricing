
from math import log, sqrt, exp
from statistics import NormalDist


def black_scholes(S, K, T, r, sigma, option_type="call"):
    """
    Calculate the price of a European option.

    Parameters:
        S: Current stock price
        K: Strike price
        T: Time to maturity (years)
        r: Risk-free interest rate
        sigma: Annualized volatility
        option_type: "call" or "put"
    """

    if S <= 0 or K <= 0 or T <= 0 or sigma <= 0:
        raise ValueError("S, K, T, and sigma must be positive.")

    if option_type not in ("call", "put"):
        raise ValueError("Option type must be 'call' or 'put'.")

    # Standard normal cumulative distribution
    N = NormalDist().cdf

    # Calculate d1 and d2
    d1 = (log(S / K) + (r + 0.5 * sigma ** 2) * T) / (
        sigma * sqrt(T)
    )

    d2 = d1 - sigma * sqrt(T)

    # European call option
    if option_type == "call":
        price = S * N(d1) - K * exp(-r * T) * N(d2)

    # European put option
    else:
        price = K * exp(-r * T) * N(-d2) - S * N(-d1)

    return price


if __name__ == "__main__":

    S = 100
    K = 100
    T = 1
    r = 0.05
    sigma = 0.20

    call_price = black_scholes(S, K, T, r, sigma, "call")
    put_price = black_scholes(S, K, T, r, sigma, "put")

    print("Black-Scholes Option Pricing")
    print("----------------------------")
    print(f"Call Price: ${call_price:.4f}")
    print(f"Put Price:  ${put_price:.4f}")
