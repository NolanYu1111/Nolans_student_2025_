import csv

# Open and read the CSV file
with open("Spotify_2024_Global_Streaming_Data.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    
    # Prepare to store filtered rows
    filtered_songs = []

    for row in reader:
        # Convert the stream count to float and check the condition
        try:
            streams = float(row["Total Streams (Millions)"])
            if streams > 10:
                filtered_songs.append(row)
        except ValueError:
            continue  # Skip rows with invalid number formats

# Print the filtered results
print("Songs with over 10 million streams:\n")
for song in filtered_songs:
    print(f"{song['Artist']} - {song['Album']} ({song['Total Streams (Millions)']} million streams)")

