import streamlit as st
import math

st.title("Transformer Short Circuit Test Calculator")

st.markdown('''
This tool calculates the winding resistance and reactance of a transformer based on short circuit test measurements (Vsc, Isc, Wsc).
''')

vsc = st.number_input('Enter the short circuit voltage (Vsc) in volts:', min_value=0.0)
isc = st.number_input('Enter the short circuit current (Isc) in amperes:', min_value=0.0)
wsc = st.number_input('Enter the short circuit power (Wsc) in watts:', min_value=0.0)

if st.button('Calculate'):
    if isc > 0:
        winding_resistance = wsc / (isc ** 2)
        impedance = vsc / isc
        winding_reactance = math.sqrt(impedance ** 2 - winding_resistance ** 2)
        st.write(f'Winding Resistance (R): {winding_resistance:.4f} Ω')
        st.write(f'Winding Reactance (X): {winding_reactance:.4f} Ω')
    else:
        st.write('The short circuit current (Isc) must be greater than 0.')

