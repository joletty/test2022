import pandas as pd
from lightweight_charts.widgets import StreamlitChart

def calculate_sma(df, period: int = 50):
    sma = df['Close'].rolling(window=period).mean()
    return pd.DataFrame({'time': df['Date'], f'SMA {period}': sma}).dropna()

def calculate_vwap(df):
    vwap = df['VWAP']
    return pd.DataFrame({'time': df['Date'], 'vwap': vwap}).dropna()

def main():
    df = pd.read_csv('2022_europe.csv')
    df_v = pd.read_csv('2022_vwap.csv')
    chart = StreamlitChart(width=950, height=600)
    chart.legend(visible=True)
    
    chart.set(df)    
    vwap_data = calculate_vwap(df_v)
    line = chart.create_line('vwap')
    line.set(vwap_data)

    # sma_data = calculate_sma(df)
    # sma_line = chart.create_line('SMA')
    # sma_line.set(sma_data)

    chart.load()
    
if __name__ == '__main__':
    main()
