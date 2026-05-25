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

## Run Locally

From the repository root:

```bash
streamlit run "notebooks/canberra/Rugang-dev/NV sensing and lock-in detection/streamlit_app.py"
```

Or from this folder:

```bash
cd "notebooks/canberra/Rugang-dev/NV sensing and lock-in detection"
streamlit run streamlit_app.py
```

## Python Dependencies

The app uses:

- `streamlit`
- `numpy`
- `matplotlib`

These are listed in the repository root `requirements.txt`.

## Deploy To Streamlit Community Cloud

1. Push the repository to GitHub.
2. Make sure these files are committed:
   - `requirements.txt`
   - `notebooks/canberra/Rugang-dev/NV sensing and lock-in detection/streamlit_app.py`
3. Sign in to Streamlit Community Cloud.
4. Create a new app.
5. Select the repository and branch.
6. Set the app file path to:

```text
notebooks/canberra/Rugang-dev/NV sensing and lock-in detection/streamlit_app.py
```

7. Deploy the app.

## Share In Confluence

After deployment, copy the public app URL.

You can share it in Confluence by:

- pasting the URL as a link or Smart Link
- embedding it with an iframe/embed macro if your Confluence instance allows that

For public Streamlit apps, viewers usually do not need their own Streamlit account.

## Notes

- The app is intended for interactive exploration and communication.
- If you want to extend it, add more metrics, export figures, or switch to Plotly for web-native interaction.
