# Highest demand regions analysis
# Create grid for pickup locations
lat_bins = np.linspace(df['pickup_latitude'].min(), df['pickup_latitude'].max(), 20)
lon_bins = np.linspace(df['pickup_longitude'].min(), df['pickup_longitude'].max(), 20)

df['lat_bin'] = pd.cut(df['pickup_latitude'], lat_bins)
df['lon_bin'] = pd.cut(df['pickup_longitude'], lon_bins)

# Count rides by region
region_demand = df.groupby(['lat_bin', 'lon_bin']).size().reset_index(name='ride_count')
top_regions = region_demand.nlargest(5, 'ride_count')

plt.figure(figsize=(10, 8))
plt.scatter(df['pickup_longitude'], df['pickup_latitude'], alpha=0.1, s=1)
plt.title('Pickup Locations Heatmap')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

print("Top 5 demand regions:")
print(top_regions)