# Clean and prepare the data
# Drop the unnamed index column and convert datetime
df = df.drop('Unnamed: 0', axis=1)
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])

# Basic data cleaning - remove invalid coordinates and negative fares
df = df[(df['pickup_longitude'] != 0) & (df['pickup_latitude'] != 0)]
df = df[(df['dropoff_longitude'] != 0) & (df['dropoff_latitude'] != 0)]
df = df[df['fare_amount'] > 0]
df = df[df['passenger_count'] > 0]

# Remove outliers (coordinates should be around NYC)
df = df[(df['pickup_longitude'] >= -74.3) & (df['pickup_longitude'] <= -73.7)]
df = df[(df['pickup_latitude'] >= 40.5) & (df['pickup_latitude'] <= 40.9)]
df = df[(df['dropoff_longitude'] >= -74.3) & (df['dropoff_longitude'] <= -73.7)]
df = df[(df['dropoff_latitude'] >= 40.5) & (df['dropoff_latitude'] <= 40.9)]

# Extract time features
df['hour'] = df['pickup_datetime'].dt.hour
df['day_of_week'] = df['pickup_datetime'].dt.dayofweek
df['month'] = df['pickup_datetime'].dt.month
df['year'] = df['pickup_datetime'].dt.year

print("Cleaned dataset shape:", df.shape)
print("\
Data info:")
print(df.info())