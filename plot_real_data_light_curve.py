import lightkurve as lk
import matplotlib.pyplot as plt

def fetch_and_plot_real_light_curve(kepler_id, quarter):
    """
    Searches for, downloads, and plots a real Kepler light curve for a given star.
    The data is sourced from the MAST archive using the lightkurve package.
    """
    print(f"Searching for light curve for KIC {kepler_id}, Quarter {quarter}...")
    
    # Search for the light curve file using the Kepler ID and quarter
    search_result = lk.search_lightcurve(f'KIC {kepler_id}', author='Kepler', quarter=quarter)
    
    # Check if data was found
    if not search_result:
        print(f"No data found for KIC {kepler_id}, Quarter {quarter}.")
        return

    print("Data found. Downloading...")
    # Download the first found light curve file collection
    lc_collection = search_result.download_all()
    
    # Stitch the collection of light curves for the quarter together
    lc = lc_collection.stitch()

    print("Processing and cleaning data...")
    # Normalize the flux, remove outliers and NaN values for a cleaner plot
    lc = lc.remove_nans().normalize().remove_outliers()

    # Create the plot
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(15, 5))
    
    ax.plot(lc.time.value, lc.flux.value, '.', markersize=1, color='midnightblue', alpha=0.6)
    
    ax.set_title(f'Real Kepler Light Curve for KIC {kepler_id} (Quarter {quarter})', fontsize=16)
    ax.set_xlabel(f'Time - {lc.time.format.upper()}', fontsize=12)
    ax.set_ylabel('Normalized Flux', fontsize=12)
    
    # Save the plot to a file
    output_filename = f'real_light_curve_{kepler_id}_Q{quarter}.png'
    plt.savefig(output_filename)
    
    print(f"\nPlot successfully saved to: {output_filename}")
    # This line can be commented out if you don't want the plot window to pop up
    # plt.show()


if __name__ == "__main__":
    # KIC 8462852, "Tabby's Star," is famous for its unusual dimming events.
    # An excellent and credible choice for a real-data script.
    KEPLER_ID = 8462852
    OBSERVATION_QUARTER = 16
    
    fetch_and_plot_real_light_curve(KEPLER_ID, OBSERVATION_QUARTER)
