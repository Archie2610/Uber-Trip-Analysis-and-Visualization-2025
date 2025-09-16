# Weekly pattern analysis
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekly_pattern = df.groupby('day_of_week').size()

plt.figure(figsize=(10, 6))
plt.bar(range(7), weekly_pattern.values)
plt.title('Weekly Ride Pattern')
plt.xlabel('Day of Week')
plt.ylabel('Number of Rides')
plt.xticks(range(7), days, rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.show()

print("Weekly pattern:")
for i, day in enumerate(days):
    print(f"{day}: {weekly_pattern[i]:,} rides")