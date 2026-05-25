import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.set_page_config(page_title="FM Lock-in Signal Explorer", layout="wide")
st.title("FM Lock-in Signal Explorer")
st.caption("Interactive ODMR + lock-in discriminator visualization")


def lorentzian(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + 4.0 * x**2)


def gaussian(x: np.ndarray) -> np.ndarray:
    return np.exp(-4.0 * np.log(2.0) * x**2)


def calculate_signals(
    freq_arr: np.ndarray,
    nu_0: float,
    delta_nu: float,
    nu_dev: float,
    shape: str,
    contrast: float = 0.1,
    rate: float = 1.0,
) -> tuple[np.ndarray, np.ndarray]:
    if shape == "Lorentzian":
        static_i = rate * (1 - contrast * lorentzian((freq_arr - nu_0) / delta_nu))
    else:
        static_i = rate * (1 - contrast * gaussian((freq_arr - nu_0) / delta_nu))

    theta = np.linspace(0, 2 * np.pi, 128, endpoint=False)
    s_e = np.zeros_like(freq_arr)
    for i, nc in enumerate(freq_arr):
        nu_m = nc + nu_dev * np.sin(theta)
        if shape == "Lorentzian":
            i_t = rate * (1 - contrast * lorentzian((nu_m - nu_0) / delta_nu))
        else:
            i_t = rate * (1 - contrast * gaussian((nu_m - nu_0) / delta_nu))
        s_e[i] = (1.0 / np.pi) * np.trapzoid(i_t * np.sin(theta), theta)

    return static_i, s_e


with st.sidebar:
    st.header("Parameters")
    nu_0 = st.slider("Resonant Freq nu_0 (MHz)", 2860.0, 2880.0, 2870.0, 0.1)
    nu_dev = st.slider("Modulation Depth nu_dev (MHz)", 0.01, 10.0, 1.0, 0.01)
    delta_nu = st.slider("Linewidth Delta_nu (MHz)", 0.5, 5.0, 2.0, 0.01)
    contrast = st.slider("Contrast C", 0.01, 0.1, 0.05, 0.001)
    shape = st.selectbox("Line Shape", ["Lorentzian", "Gaussian"], index=0)

freq_arr = np.linspace(2860, 2880, 1000)
static_i, s_e = calculate_signals(
    freq_arr, nu_0, delta_nu, nu_dev, shape, contrast=contrast
)

center_idx = np.argmin(np.abs(freq_arr - nu_0))
# Guard against indexing at boundaries.
if 0 < center_idx < len(freq_arr) - 1:
    slope = (s_e[center_idx + 1] - s_e[center_idx - 1]) / (
        freq_arr[center_idx + 1] - freq_arr[center_idx - 1]
    )
else:
    slope = 0.0

tangent_nu = np.linspace(nu_0 - 3, nu_0 + 3, 20)
tangent_se = slope * (tangent_nu - nu_0)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.plot(freq_arr, static_i, "k-", linewidth=2, label="Static ODMR Profile")
ax1.axvspan(
    nu_0 - nu_dev,
    nu_0 + nu_dev,
    color="green",
    alpha=0.2,
    label="Modulation Sweep Region",
)
ax1.axvline(nu_0, color="green", linestyle=":", label="Resonant Center nu_0")
ax1.set_title("Static ODMR Dip & Modulation Region")
ax1.set_xlabel("Microwave Frequency (MHz)")
ax1.set_ylabel("Fluorescence Intensity (arb. units)")
ax1.set_xlim(np.min(freq_arr), np.max(freq_arr))
ax1.grid(True, linestyle=":", alpha=0.7)
ax1.legend(loc="lower right")

ax2.plot(freq_arr, s_e, "b-", linewidth=2, label="Error Signal S_E")
ax2.axvline(nu_0, color="gray", linestyle="--", label="Zero-Crossing Target")
ax2.axhline(0, color="gray", linestyle="--")
ax2.plot(
    tangent_nu,
    tangent_se,
    color="orange",
    linestyle="--",
    linewidth=2,
    label=f"Slope |D| = {abs(slope):.5f}",
)
ax2.set_title("Lock-In Error Signal (S_E)")
ax2.set_xlabel("Tracking Frequency nu_c (MHz)")
ax2.set_ylabel("Demodulated Amplitude")
ax2.set_xlim(np.min(freq_arr), np.max(freq_arr))
ax2.set_ylim(-0.06, 0.06)
ax2.grid(True, linestyle=":", alpha=0.7)
ax2.legend(loc="upper right")

fig.tight_layout()
st.pyplot(fig)

st.markdown("---")
st.write(
    "Tip: Deploy this app and embed the public URL in Confluence using an iframe macro."
)
