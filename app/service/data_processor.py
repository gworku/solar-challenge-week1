import pandas as pd

class DataProcessor:
    """Handles data processing and statistics"""
    
    def get_summary_stats(self, df, metric):
        """Calculate summary statistics for a given metric"""
        return df.groupby('country')[metric].describe()
    
    def filter_by_date_range(self, df, date_col, start_date, end_date):
        """Filter dataframe by date range"""
        if not pd.api.types.is_datetime64_any_dtype(df[date_col]):
            df[date_col] = pd.to_datetime(df[date_col])
        mask = (df[date_col] >= start_date) & (df[date_col] <= end_date)
        return df.loc[mask]
    
    def detect_outliers(self, df, columns, z_threshold=3):
        """Detect outliers using Z-score method"""
        z_scores = df[columns].apply(
            lambda x: (x - x.mean()) / x.std()
        ).abs()
        return z_scores > z_threshold