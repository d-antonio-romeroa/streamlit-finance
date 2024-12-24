
import yfinance as yf

import plotly.graph_objects as go

def plot_stock(data, ticker):
    fig = go.Figure()

    # Candlestick chart
    fig.add_trace(go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name='Candlestick'
    ))

    # Moving averages
    fig.add_trace(go.Scatter(
        x=data.index, y=data['Short_MA'],
        mode='lines', name='10-day MA'
    ))
    fig.add_trace(go.Scatter(
        x=data.index, y=data['Long_MA'],
        mode='lines', name='50-day MA'
    ))

    # Add titles and labels
    fig.update_layout(
        title=f"Stock Analysis for {ticker}",
        xaxis_title="Date",
        yaxis_title="Price",
        template="plotly_dark"
    )
    return fig


def generate_signals(data):
    data['Short_MA'] = data['Close'].rolling(window=10).mean()
    data['Long_MA'] = data['Close'].rolling(window=50).mean()
    data['Signal'] = 0
    data.loc[data['Short_MA'] > data['Long_MA'], 'Signal'] = 1
    data.loc[data['Short_MA'] <= data['Long_MA'], 'Signal'] = -1
    return data


def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="6mo")  # Fetch last 6 months of data
    return data