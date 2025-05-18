import pandas as pd
import streamlit as st
from pathlib import Path

class DataLoader:
    """Handles loading and caching of solar data"""
    
    def __init__(self, data_dir="../data"):
        self.data_dir = Path(data_dir)
        self.available_countries = ["Benin", "Sierra Leone", "Togo"]
    
    @st.cache_data(show_spinner="Loading solar data...")
    def load_country_data(_self, country):
        """Load and cache data for a single country"""
        file_path = _self.data_dir / f"{country.lower().replace(' ', '_')}_clean.csv"
        if not file_path.exists():
            raise FileNotFoundError(f"Data file not found: {file_path}")
        df = pd.read_csv(file_path)
        df['country'] = country  # Add country label
        return df
    
    def load_multiple_countries(self, countries):
        """Load and combine data for multiple countries"""
        if not countries:
            raise ValueError("No countries selected")
        
        dfs = []
        for country in countries:
            try:
                df = self.load_country_data(country)
                dfs.append(df)
            except FileNotFoundError as e:
                st.warning(str(e))
                continue
        
        if not dfs:
            raise ValueError("No valid data loaded")
        
        return pd.concat(dfs, ignore_index=True)