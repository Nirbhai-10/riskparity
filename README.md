### README

## Portfolio Optimization with Risk Parity and Minimum Variance

### Introduction

This project focuses on portfolio optimization using two primary methods: Risk Parity and Minimum Variance. Additionally, it compares these methods with a Market Capitalization weighting approach. The goal is to understand how different weighting strategies impact the expected return and risk (variance) of a portfolio.

### Theory

#### Risk Parity

Risk Parity is an investment strategy that aims to balance the risk contributions of each asset in a portfolio. Instead of focusing on allocating equal amounts of capital, Risk Parity allocates risk equally. The idea is to ensure that each asset contributes the same amount of risk to the overall portfolio, leading to a more balanced and potentially more stable portfolio.

**Equation for Risk Parity:**

\[ \text{MCR}_i = \frac{(\mathbf{C} \mathbf{w})_i}{\sqrt{\mathbf{w}^T \mathbf{C} \mathbf{w}}} \]

Where:
- \( \text{MCR}_i \) is the Marginal Contribution to Risk of asset \(i\).
- \( \mathbf{C} \) is the covariance matrix of asset returns.
- \( \mathbf{w} \) is the weight vector of the portfolio.

The objective is to minimize the squared differences in the risk contributions of all assets:

\[ \text{Objective Function} = \sum_{i=1}^{n} \sum_{j=1}^{n} (w_i \text{MCR}_i - w_j \text{MCR}_j)^2 \]

#### Minimum Variance

The Minimum Variance strategy focuses on minimizing the overall risk of the portfolio. This is achieved by finding the optimal combination of asset weights that results in the lowest possible variance (a measure of risk) for the portfolio. This approach is ideal for risk-averse investors looking to reduce potential volatility.

**Equation for Minimum Variance:**

\[ \text{Objective Function} = \sqrt{\mathbf{w}^T \mathbf{C} \mathbf{w}} \]

Where:
- \( \mathbf{w} \) is the weight vector of the portfolio.
- \( \mathbf{C} \) is the covariance matrix of asset returns.

#### Market Capitalization Weighting

Market Capitalization weighting allocates weights to assets based on their market capitalization. Larger companies get a higher weight in the portfolio. This method assumes that the market cap reflects the company's size, stability, and importance, making it a popular approach for index funds.

### Project Steps

1. **Data Collection**: We selected six diversified stocks from the Indian stock market:
   - Reliance Industries (Energy)
   - TCS (Technology)
   - HDFC Bank (Finance)
   - ITC (Consumer Goods)
   - Bharti Airtel (Telecommunications)
   - Dr. Reddy's Laboratories (Pharmaceuticals)

2. **Historical Data**: We downloaded the historical price data for the last 5 months using Yahoo Finance.

3. **Returns Calculation**: Daily returns for each stock were calculated based on the adjusted close prices.

4. **Variance-Covariance Matrix**: This matrix, representing the variance and covariance between the stocks, was computed from the returns.

5. **Risk Parity Weights Calculation**: 
   - A function was created to balance the risk contributions of each asset.
   - Optimization was performed using the `scipy.optimize.minimize` function to find the optimal weights.

6. **Minimum Variance Weights Calculation**: 
   - A function was designed to minimize the portfolio's variance.
   - Optimization was performed to determine the weights that minimize risk.

7. **Performance Calculation**: 
   - The expected return and variance for the Risk Parity and Minimum Variance portfolios were computed.
   - The same calculations were performed for a Market Capitalization weighted portfolio for comparison.

8. **Results**:
   - Risk Parity provided balanced weights with moderate returns and risk.
   - Minimum Variance achieved the lowest risk but with slightly lower returns.
   - Market Capitalization yielded the highest returns but also the highest risk.


      
