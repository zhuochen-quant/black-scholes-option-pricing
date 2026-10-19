# Black-Scholes Option Pricing Model

A Python implementation of the Black-Scholes model for pricing European call and put options.

This project demonstrates the application of financial mathematics and Python programming to derivative pricing and provides a foundation for further quantitative risk analysis.

## 1. Project Overview

The Black-Scholes model is a widely used mathematical framework for pricing European-style options.

The objectives of this project are to:

- Implement the Black-Scholes analytical pricing formulas in Python.
- Calculate theoretical prices for European call and put options.
- Validate input parameters and produce reproducible pricing results.
- Establish a foundation for future option Greeks and risk sensitivity analysis.

## 2. Mathematical Framework

For a non-dividend-paying underlying asset, the European call option price is:

**C = S × N(d₁) − K × e⁻ʳᵀ × N(d₂)**

The European put option price is:

**P = K × e⁻ʳᵀ × N(−d₂) − S × N(−d₁)**

Where:

**d₁ = [ln(S/K) + (r + σ²/2)T] / (σ√T)**

**d₂ = d₁ − σ√T**

Definitions:

| Symbol | Description |
|---|---|
| S | Current underlying asset price |
| K | Option strike price |
| T | Time to maturity in years |
| r | Continuously compounded risk-free interest rate |
| σ | Annualized volatility |
| N(x) | Standard normal cumulative distribution function |

## 3. Implementation

The model is implemented in Python using only standard-library modules:

- `math`: logarithmic, exponential, and square-root calculations.
- `statistics.NormalDist`: standard normal cumulative distribution function.

The program supports both European call and put options and validates key input parameters.

No external Python packages are required for the current version.

## 4. Example Results

The following parameters are used:

| Parameter | Value |
|---|---|
| Stock Price (S) | $100 |
| Strike Price (K) | $100 |
| Time to Maturity (T) | 1 year |
| Risk-Free Rate (r) | 5% |
| Volatility (σ) | 20% |

Model output:

```text
Black-Scholes Option Pricing
----------------------------
Call Price: $10.4506
Put Price:  $5.5735
```

The results provide a numerical example of European option valuation under the Black-Scholes assumptions.

## 5. How to Run

**Requirements**

- Python 3.10 or later
- No third-party dependencies

Clone the repository:

```bash
git clone https://github.com/zhuochen-quant/black-scholes-option-pricing.git
```

Navigate to the project directory:

```bash
cd black-scholes-option-pricing
```

Run the Python script:

```bash
python black_scholes.py
```

## 6. Model Assumptions and Limitations

The current implementation relies on the standard Black-Scholes assumptions, including:

- European-style exercise.
- No dividends.
- Constant volatility and risk-free interest rate.
- Lognormal asset prices under the model.
- Frictionless markets.

The current model does not account for volatility smiles, stochastic volatility, transaction costs, or early exercise.

## 7. Future Development

Planned improvements include:

- Greeks: Delta, Gamma, Vega, Theta, and Rho.
- Sensitivity analysis and visualization.
- Monte Carlo option pricing.
- Put-call parity and numerical validation tests.
- Comparison of analytical and simulation-based pricing approaches.

## 8. Author

Zhuo Chen

Master's Student in Computational Finance & Risk Management  
University of Washington

GitHub: [zhuochen-quant](https://github.com/zhuochen-quant)
