# Fix the distance calculation
avg_distance = ((df['pickup_latitude'] - df['dropoff_latitude'])**2 + (df['pickup_longitude'] - df['dropoff_longitude'])**2)**0.5 * 69
print(f"Average trip distance (estimated): {avg_distance.mean():.2f} miles")