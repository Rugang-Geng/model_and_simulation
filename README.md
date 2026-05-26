# FM Lock-in Signal Streamlit App

This folder contains a small Streamlit app for exploring a frequency-modulated lock-in ODMR signal in the browser.

## Files

- `FM lock-in signal.ipynb`: notebook version of the interactive model
- `streamlit_app.py`: browser-based Streamlit version of the app

## What The App Does

The app visualizes two linked outputs:

1. The static ODMR dip and modulation sweep region
2. The lock-in discriminator error signal and its local slope

You can interactively adjust:

- Resonant frequency `nu_0`
- Modulation depth `nu_dev`
- Linewidth `Delta_nu`
- Contrast `C`
- Line shape: Lorentzian or Gaussian

## Python Dependencies

The app uses:

- `streamlit`
- `numpy`
- `matplotlib`

These are listed in the repository root `requirements.txt`.


## Share it

After deployment, copy the public app URL.

You can share it by:

- pasting the URL as a link or Smart Link
- embedding it with an iframe/embed macro if your instance allows that

For public Streamlit apps, viewers usually do not need their own Streamlit account.

## Notes

- The app is intended for interactive exploration and communication.
- If you want to extend it, add more metrics, export figures, or switch to Plotly for web-native interaction.
