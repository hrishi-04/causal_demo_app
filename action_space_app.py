
import streamlit as st
import pandas as pd

raw_data = pd.read_csv('raw_data.csv')
data_propensity = pd.read_csv('data_propensity.csv')

def main():
    st.title("Propensity Generator")
    st.subheader("A simple web app to display propensity scores and feature coefficients")

    if 'page' not in st.session_state:
        st.session_state.page = 'main'

    if 'show_propensity_group1' not in st.session_state:
        st.session_state.show_propensity_group1 = False
    if 'show_propensity_group2' not in st.session_state:
        st.session_state.show_propensity_group2 = False
    if 'show_propensity_group3' not in st.session_state:
        st.session_state.show_propensity_group3 = False

    if st.session_state.page == 'main':
        show_main()
    elif st.session_state.page == 'raw_data':
        show_raw_data()
    elif st.session_state.page == 'propensities':
        show_propensities()
    elif st.session_state.page == 'images':
        show_images()
    elif st.session_state.page == 'causal_inference':
        causal_inference()

def show_main():
    if st.button("Show Raw Data"):
        st.session_state.page = 'raw_data'
        st.rerun()
    if st.button("Data with Propensities"):
        st.session_state.page = 'propensities'
        st.rerun()
    if st.button("Propensity Insights"):
        st.session_state.page = 'images'
        st.rerun()
    if st.button("Causal Inference for PTP"):
        st.session_state.page = 'causal_inference'
        st.rerun()

def show_raw_data():
    st.header("Raw Data")
    st.dataframe(raw_data)
    if st.button("Back"):
        st.session_state.page = 'main'
        st.rerun()

def show_propensities():
    st.header("Data Propensity")
    st.dataframe(data_propensity)
    if st.button("Back"):
        st.session_state.page = 'main'
        st.rerun()

def show_images():
    st.header("Propensity Insights")
    show_image('propensity_score_distribution.jpg', "Propensity Score Distribution")
    show_image('propensity_features.jpg', "Feature Coefficients")
    if st.button("Back"):
        st.session_state.page = 'main'
        st.rerun()

def show_image(image_path, title):
    st.header(title)
    st.image(image_path)

def causal_inference():
    if st.button('(No-Risk Customers)'):
        st.session_state.show_propensity_group1 = True
        st.rerun()
    if st.session_state.show_propensity_group1:
        st.write('statistically signigicant effect of PTP on Re-payment \U0001F7E2')
        st.write('----------------------------------------------')
        st.write('A ptp made sugggests that a customer in this category is 27% more likely to miss a payment \U0001F53A')
        st.write('----------------------------------------------')
    


    if st.button('(Medium-Risk Customers)'):
        st.session_state.show_propensity_group2 = True
        st.rerun()
    if st.session_state.show_propensity_group2:
        st.write('statistically signigicant effect of PTP on Re-payment \U0001F7E2')
        st.write('----------------------------------------------')
        st.write('A ptp made sugggests that a customer in this category is 46% more likely to miss a payment \U0001F53A')
        st.write('----------------------------------------------')
    


    if st.button('(High-Risk Customers)'):
        st.session_state.show_propensity_group3 = True
        st.rerun()
    if st.session_state.show_propensity_group3:
        st.write('statistically insignigicant effect of PTP on Re-payment \U0001F534')
        st.write('----------------------------------------------')
        st.write('For a customer in this category ptp is not the most significant driving factor to miss a payment \U0000274C')
        st.write('----------------------------------------------')

    if st.button("Back"):
        st.session_state.page = 'main'
        st.session_state.show_propensity_group1 = False
        st.session_state.show_propensity_group2 = False
        st.session_state.show_propensity_group3 = False
        st.rerun()
    

if __name__ == "__main__":
    main()