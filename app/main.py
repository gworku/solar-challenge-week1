import streamlit as st
from app.services.data_loader import DataLoader
from app.services.data_processor import DataProcessor
from app.components.sidebar import SidebarControls
from app.components.visualizations import SolarVisualizer

def main():
    st.title("Solar Potential Dashboard")
    
    # Initialize components
    data_loader = DataLoader()
    data_processor = DataProcessor()
    sidebar = SidebarControls()
    visualizer = SolarVisualizer()
    
    # Get user inputs
    inputs = sidebar.render()
    
    try:
        # Load and process data
        df = data_loader.load_multiple_countries(inputs["countries"])
        
        # Show data summary
        st.header("Summary Statistics")
        summary_stats = data_processor.get_summary_stats(df, inputs["primary_metric"])
        st.dataframe(
            summary_stats.style.background_gradient(cmap="Blues")
        )
        
        # Render visualization
        st.header(f"{inputs['chart_type']} of {inputs['primary_metric']}")
        
        if inputs["chart_type"] == "Boxplot":
            visualizer.plot_boxplot(df, inputs["primary_metric"], inputs["countries"])
        
        elif inputs["chart_type"] == "Histogram":
            visualizer.plot_histogram(df, inputs["primary_metric"], inputs["countries"])
        
        elif inputs["chart_type"] == "Scatter Plot":
            visualizer.plot_scatter(
                df,
                inputs["primary_metric"],
                inputs["secondary_metric"],
                inputs["countries"]
            )
    
    except ValueError as e:
        st.error(str(e))
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()