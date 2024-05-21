import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
 
def six_sigma_poisson_chart(avg_defect_rate):
    # Calculate Six Sigma quality level (defects per million opportunities)
    six_sigma_defects_per_million = 3.4
    million_opportunities = 1e6
    six_sigma_defects = six_sigma_defects_per_million / million_opportunities
    # Set the range of defects to consider
    max_defects = 10  # Adjust based on expected maximum defects
    defects_range = np.arange(0, max_defects + 1)
    # Calculate Poisson probabilities for the given average defect rate (λ)
    poisson_probs = poisson.pmf(defects_range, avg_defect_rate)
    # Create the Poisson chart
    plt.figure(figsize=(10, 6))
    plt.bar(defects_range, poisson_probs, alpha=0.7, label=f'λ = {avg_defect_rate}')
    # Plot Six Sigma quality limits
    plt.axvline(x=six_sigma_defects * million_opportunities, color='red', linestyle='--', label='Six Sigma Quality')
    # Add labels and title
    plt.xlabel('Number of Defects')
    plt.ylabel('Probability')
    plt.title('Six Sigma Poisson Chart')
    plt.legend()
    plt.grid(True)
    # Show the plot
    plt.show()
 
# Example usage
average_defect_rate = 0.1  # Adjust based on your process
six_sigma_poisson_chart(average_defect_rate)