# Peak ride hours analysis
hourly_rides = df.groupby('hour').size()
plt.figure(figsize=(12, 6))
plt.bar(hourly_rides.index, hourly_rides.values)
plt.title('Peak Ride Hours - Total Rides by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Rides')
plt.xticks(range(0, 24))
plt.grid(axis='y', alpha=0.3)
plt.show()

print("Peak hours (top 5):")
peak_hours = hourly_rides.sort_values(ascending=False).head()
print(peak_hours)