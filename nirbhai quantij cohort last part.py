import pandas as pd
import numpy as np
import yfinance as yf
from scipy.optimize import minimize

tickers = ['RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'ITC.NS', 'BHARTIARTL.NS', 'DRREDDY.NS']
data = yf.download(tickers=tickers, period='5mo')

returns = data['Adj Close'].pct_change().dropna()
C = returns.cov()

def risk_parity_obj_function(w, C):
    P = C @ w
    MCR = P / np.sqrt(w.T @ C @ w)
    f = 0.0
    for i in range(len(w)):
        for j in range(len(w)):
            f += (w[i] * MCR[i] - w[j] * MCR[j]) ** 2
    return f

def risk_parity_weights(C):
    n = C.shape[0]
    w = np.ones(n) / n
    constraints = (
        {'type': 'eq', 'fun': lambda w: np.sum(w) - 1},
        {'type': 'ineq', 'fun': lambda w: w}
    )
    bounds = [(0, 1) for _ in range(n)]
    result = minimize(lambda w: risk_parity_obj_function(w, C), w, method='SLSQP', constraints=constraints, bounds=bounds)
    return result.x

def min_variance_obj_function(w, C):
    return np.sqrt(w.T @ C @ w)

def min_variance_weights(C):
    n = C.shape[0]
    w = np.ones(n) / n
    constraints = (
        {'type': 'eq', 'fun': lambda w: np.sum(w) - 1},
        {'type': 'ineq', 'fun': lambda w: w}
    )
    bounds = [(0, 1) for _ in range(n)]
    result = minimize(lambda w: min_variance_obj_function(w, C), w, method='SLSQP', constraints=constraints, bounds=bounds)
    return result.x

weights_risk_parity = risk_parity_weights(C)
weights_min_variance = min_variance_weights(C)

def portfolio_performance(weights, returns):
    portfolio_return = np.sum(returns.mean() * weights) * 252
    portfolio_variance = np.dot(weights.T, np.dot(C, weights)) * 252
    return portfolio_return, portfolio_variance

expected_return_rp, variance_rp = portfolio_performance(weights_risk_parity, returns)
expected_return_mv, variance_mv = portfolio_performance(weights_min_variance, returns)

market_caps = {'RELIANCE.NS': 1542990, 'TCS.NS': 1339262, 'HDFCBANK.NS': 862053, 'ITC.NS': 335125, 'BHARTIARTL.NS': 421144, 'DRREDDY.NS': 76842}
total_market_cap = sum(market_caps.values())
market_cap_weights = np.array([market_caps[ticker] for ticker in tickers]) / total_market_cap

expected_return_mc, variance_mc = portfolio_performance(market_cap_weights, returns)

print("Risk Parity Weights:", weights_risk_parity)
print("Minimum Variance Weights:", weights_min_variance)
print("\nExpected Return (Risk Parity):", expected_return_rp)
print("Variance (Risk Parity):", variance_rp)
print("\nExpected Return (Minimum Variance):", expected_return_mv)
print("Variance (Minimum Variance):", variance_mv)
print("\nExpected Return (Market Cap):", expected_return_mc)
print("Variance (Market Cap):", variance_mc)

'''
We analyzed a portfolio using three different weighting methods: Risk Parity, Minimum Variance, and Market Capitalization.


Risk Parity: This method allocated equal weights to each stock, resulting in an expected annual return of 29.59% with a variance of 1.59%. 
It offers a balanced approach with moderate risk and return.

Minimum Variance: This approach minimized risk by varying the weights, leading to a lower expected return of 23.73% but also the lowest variance at 1.44%. 
Its ideal for risk-averse investors.

Market Capitalization: This method weighted stocks based on their market cap, yielding the highest expected return of 40.67% but with the highest risk (variance of 1.97%). 
It suits those willing to accept more risk for higher returns.

'''