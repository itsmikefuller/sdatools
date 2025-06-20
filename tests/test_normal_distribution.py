from sdatools.distributions.continuous.normal import NormalDistribution


# Create two normal distributions
dist1 = NormalDistribution(mu=5, sigma=2)
dist2 = NormalDistribution(mu=3, sigma=4)

# Print the distributions
print("Distribution 1:", dist1)
print("Distribution 2:", dist2)

# Add the two distributions
dist_sum = dist1 + dist2
print("Distribution 1 + Distribution 2:", dist_sum)

# Subtract the two distributions
dist_diff = dist1 - dist2
print("Distribution 1 - Distribution 2:", dist_diff)

# Multiply a distribution by a scalar
dist_scaled = 3 * dist1
print("3 * Distribution 1:", dist_scaled)
dist_scaled = dist1 * 3
print("Distribution 1 * 3:", dist_scaled)

# Divide a distribution by a scalar
dist_divided = dist1 / 2
print("Distribution 1 / 2:", dist_divided)

# Check equality and inequality
print("Distribution 1 == Distribution 2:", dist1 == dist2)
print("Distribution 1 != Distribution 2:", dist1 != dist2)
