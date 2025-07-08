# Astro Data Visualization

Simple Python scripts for visualizing astronomical data. This repository is for personal educational projects and explorations.

---

## 1. `plot_light_curve.py` (Primary)

A script to search, download, and plot a **real** light curve for a star from the NASA Kepler mission archive. It uses the `lightkurve` package to interact with real scientific data.

### Features
- Searches for real data on the MAST archive for a given Kepler ID.
- Downloads the FITS file.
- Processes and cleans the data (normalizes flux, removes outliers).
- Plots the light curve using `Matplotlib` and saves it as a PNG file.

### Usage
To run the script, you need Python and the following libraries installed:

```bash
pip install lightkurve matplotlib
```

Then, run the script from your terminal:

```bash
python plot_light_curve.py
```

This will download data and generate a plot named `real_light_curve_8462852_Q16.png`.

---

## 2. `synthetic_plot_light_curve.py` (Test/Demo)

A script to generate and plot a sample light curve with synthetic data. Useful for quick tests without network access.

### Features
- Generates synthetic data mimicking a stellar light curve with a planetary transit.
- Uses NumPy and Matplotlib.

### Usage
Install dependencies:

```bash
pip install numpy matplotlib
```

Run the script:

```bash
python synthetic_plot_light_curve.py
```

This will generate a plot named `light_curve_8462852.png`.
