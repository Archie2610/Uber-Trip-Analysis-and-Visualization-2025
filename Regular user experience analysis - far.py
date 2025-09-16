# Regular user experience analysis - fare patterns and passenger counts
plt.figure(figsize=(15, 5))

# Fare distribution
plt.subplot(1, 3, 1)
plt.hist(df['fare_amount'], bins=50, alpha=0.7, edgecolor='black')
plt.title('Fare Amount Distribution')
plt.xlabel('Fare Amount ($)')
plt.ylabel('Frequency')
plt.xlim(0, 50)

# Passenger count distribution
plt.subplot(1, 3, 2)
passenger_counts = df['passenger_count'].value_counts().sort_index()
plt.bar(passenger_counts.index, passenger_counts.values)
plt.title('Passenger Count Distribution')
plt.xlabel('Number of Passengers')
plt.ylabel('Number of Rides')

# Average fare by hour
plt.subplot(1, 3, 3)
hourly_avg_fare = df.groupby('hour')['fare_amount'].mean()
plt.plot(hourly_avg_fare.index, hourly_avg_fare.values, marker='o')
plt.title('Average Fare by Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Average Fare ($)')
plt.xticks(range(0, 24, 2))
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()

print("User Experience Summary:")
print(f"Average fare: ${df['fare_amount'].mean():.2f}")
print(f"Median fare: ${df['fare_amount'].median():.2f}")
print(f"Most common passenger count: {df['passenger_count'].mode()[0]}")
print(f"Average trip distance (estimated): {((df['pickup_latitude'] - df['dropoff_latitude'])**2 + (df['pickup_longitude'] - df['dropoff_longitude'])**2)**0.5 * 69:.2f} miles")