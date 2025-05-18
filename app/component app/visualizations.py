import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

class SolarVisualizer:
    """Handles all visualization components"""
    
    def __init__(self, palette="muted"):
        self.palette = palette
        sns.set_theme(style="whitegrid", palette=palette)
    
    def plot_boxplot(self, df, metric, countries):
        """Generate boxplot visualization"""
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(x='country', y=metric, data=df, ax=ax)
        ax.set_title(f"{metric} Distribution by Country")
        st.pyplot(fig)
    
    def plot_histogram(self, df, metric, countries):
        """Generate histogram visualization"""
        fig, ax = plt.subplots(figsize=(10, 6))
        for country in countries:
            sns.histplot(
                df[df['country'] == country][metric],
                label=country,
                kde=True,
                alpha=0.5,
                ax=ax
            )
        ax.legend()
        ax.set_title(f"{metric} Distribution")
        st.pyplot(fig)
    
    def plot_scatter(self, df, x_metric, y_metric, countries):
        """Generate scatter plot visualization"""
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.scatterplot(
            x=x_metric,
            y=y_metric,
            hue='country',
            data=df,
            palette=self.palette,
            ax=ax
        )
        ax.set_title(f"{x_metric} vs {y_metric}")
        st.pyplot(fig)