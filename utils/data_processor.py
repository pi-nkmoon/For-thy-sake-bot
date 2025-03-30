# utils/data_processor.py

import pandas as pd

def process_spot_trades(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        print("No spot trades to process.")
        return df
    df['time'] = pd.to_datetime(df['time'], unit='ms')
    numeric_columns = ['price', 'qty', 'commission', 'quoteQty']
    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    df['side'] = df['isBuyer'].apply(lambda x: 'BUY' if x else 'SELL')
    df['trade_id'] = df['id']
    print(f"Processed {len(df)} spot trades.")
    return df


def process_futures_trades(df: pd.DataFrame) -> pd.DataFrame:
    '''
    if df.empty:
        print("No futures trades to process.")
        return df
    df['time'] = pd.to_datetime(df['time'], unit='ms')
    numeric_columns = ['price', 'qty', 'realizedPnl', 'commission']
    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Convert 'side' to 'LONG' or 'SHORT' based on position side
    # Assume that 'side' in futures trades indicates the trade side ('BUY' or 'SELL')
    # and 'positionSide' indicates 'LONG' or 'SHORT' position
    if 'positionSide' in df.columns:
        df['side'] = df['positionSide']
    else:
        # Fallback if 'positionSide' is not available
        df['side'] = df['side'].apply(lambda x: 'LONG' if x == 'BUY' else 'SHORT')

    df['trade_id'] = df['id']
    print(f"Processed {len(df)} futures trades.")
    return df'''

    if df.empty:
        print("No futures trades to process.")
        return df
    df['time'] = pd.to_datetime(df['time'], unit='ms')
    numeric_columns = ['price', 'qty', 'realizedPnl', 'commission']
    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Determine 'side' based on 'positionSide' and 'side'
    def determine_side(row):
        if row.get('positionSide') == 'BOTH' or not row.get('positionSide'):
            # One-way Mode
            if row['side'] == 'BUY':
                return 'LONG'
            else:
                return 'SHORT'
        else:
            # Hedge Mode
            return row['positionSide']

    df['side'] = df.apply(determine_side, axis=1)

    df['trade_id'] = df['id']
    print(f"Processed {len(df)} futures trades.")
    return df