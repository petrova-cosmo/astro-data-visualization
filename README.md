# Astro Data Visualization

A collection of Python scripts for visualizing astronomical data from the Kepler mission, showcasing different analysis approaches.

---

### 1. `plot_full_light_curve.py` (Full Survey)

A universal script to search, download, and plot the **complete** Kepler light curve for any star. Ideal for finding long-period transits or analyzing long-term stellar variability. This is the primary tool of the repository.

**Usage:**
This script is run from the command line with parameters.

```bash
# Install dependencies
pip install lightkurve matplotlib

# Run for a specific star (KIC ID and Name)
python plot_full_light_curve.py 8311864 "Kepler-452"
```
### 2. quick_analyze_quarter.py (Quick Analysis)
A script to download and plot data for a single observation quarter. Perfect for a quick, detailed look at a specific event. To analyze a different star or quarter, simply edit the parameters at the bottom of the script file.

**Usage:**
```bash

# Dependencies are the same
pip install lightkurve matplotlib

# Run the script
python quick_analyze_quarter.py
```
### 3. `synthetic_plot_light_curve.py` (Synthetic Data)
A simple script that generates and plots a synthetic light curve. It does not require an internet connection and is useful for quick tests or demonstrating the concept of a planetary transit.

**Usage:**
```bash

# Install dependencies
pip install numpy matplotlib

# Run the script
python synthetic_plot_light_curve.py
```
