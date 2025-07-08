import lightkurve as lk
import matplotlib.pyplot as plt

def fetch_and_plot_quarter_light_curve(kepler_id, quarter, target_name):
    """
    Searches for and plots the light curve for a specific quarter for a given KIC ID.
    """
    print(f"Searching for light curve for {target_name} (KIC {kepler_id}), Quarter {quarter}...")
    
    search_result = lk.search_lightcurve(f'KIC {kepler_id}', author='Kepler', quarter=quarter)
    
    if not search_result:
        print(f"No data found for KIC {kepler_id}, Quarter {quarter}.")
        return

    print("Data found. Downloading...")
    lc = search_result.download()

    print("Processing and cleaning data...")
    lc = lc.remove_nans().normalize().remove_outliers()

    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(15, 5))
    
    ax.plot(lc.time.value, lc.flux.value, '.', markersize=2, color='firebrick', alpha=0.7)
    
    ax.set_title(f'Kepler Light Curve for {target_name} (Quarter {quarter})', fontsize=16)
    ax.set_xlabel(f'Time - {lc.time.format.upper()}', fontsize=12)
    ax.set_ylabel('Normalized Flux', fontsize=12)
    ax.grid(True)
    
    clean_name = "".join(x for x in target_name if x.isalnum())
    output_filename = f'light_curve_{clean_name}_{kepler_id}_Q{quarter}.png'
    plt.savefig(output_filename)
    
    print(f"\nPlot successfully saved to: {output_filename}")


if __name__ == "__main__":
    # --- Parameters for Quick Analysis ---
    # --- Просто измените эти значения для анализа другой звезды/квартала ---
    KEPLER_ID = 8462852
    STAR_NAME = "Tabby's Star"
    QUARTER = 16
    
    fetch_and_plot_quarter_light_curve(KEPLER_ID, QUARTER, STAR_NAME)
