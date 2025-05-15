import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# App title
st.title("Aliasing Visualizer")

# Sidebar inputs
st.sidebar.header("Settings")

# Frequency settings
signal_freq = st.sidebar.slider("Original Signal Frequency (Hz)", min_value=1, max_value=100, value=10)
sample_rate = st.sidebar.slider("Sampling Rate (Hz)", min_value=1, max_value=200, value=20)
duration = st.sidebar.slider("Duration (s)", min_value=1, max_value=5, value=1)

# Time values
continuous_time = np.linspace(0, duration, 1000)
sampled_time = np.arange(0, duration, 1/sample_rate)

# Signal definition
original_signal = np.sin(2 * np.pi * signal_freq * continuous_time)
sampled_signal = np.sin(2 * np.pi * signal_freq * sampled_time)

# Aliasing detection
nyquist_rate = sample_rate / 2
is_aliasing = signal_freq > nyquist_rate

# Warning display
if is_aliasing:
    st.sidebar.error(f"⚠️ Aliasing detected! Nyquist rate is {nyquist_rate:.1f} Hz.")
else:
    st.sidebar.success(f"✅ No aliasing. Nyquist rate is {nyquist_rate:.1f} Hz.")

# Plotting
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(continuous_time, original_signal, label="Original Signal", linewidth=2)
ax.stem(sampled_time, sampled_signal, linefmt='r-', markerfmt='ro', basefmt=" ", label="Sampled Points")
ax.set_title("Signal and Sampled Points")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Amplitude")
ax.legend()
ax.grid(True)

# Display the plot
st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("Developed with ❤️ using Streamlit")
