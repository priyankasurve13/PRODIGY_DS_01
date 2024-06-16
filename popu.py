import csv
import turtle
import glob

# Function to read CSV files and return combined data for the year 2020
def read_csv_files(file_pattern):
    combined_data = {}
    for filename in glob.glob(file_pattern):
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Read the header
            for row in reader:
                country = row[0]
                try:
                    population = float(row[-1])  # Adjust index if the year column is different
                except ValueError:
                    population = 0  # Handle missing or non-numeric values
                if country in combined_data:
                    combined_data[country] += population  # Aggregate population
                else:
                    combined_data[country] = population
    return list(combined_data.items())

# Function to plot the bar chart using turtle
def plot_data(data):
    data.sort(key=lambda x: x[1], reverse=True)  # Sort by population
    top_10 = data[:10]  # Get the top 10 entries

    screen = turtle.Screen()
    screen.title('Top 10 Countries by Population in 2020 (Combined Data)')

    t = turtle.Turtle()
    t.speed(0)  # Max speed
    t.hideturtle()

    # Draw axes
    t.penup()
    t.goto(-300, -200)
    t.pendown()
    t.forward(500)
    t.penup()
    t.goto(-300, -200)
    t.left(90)
    t.pendown()
    t.forward(300)

    # Draw bars
    x = -290
    y = -200
    bar_width = 30
    max_height = 250

    for i, (country, population) in enumerate(top_10):
        # Normalize height for the visualization
        height = (population / top_10[0][1]) * max_height  # Scale based on max population
        t.penup()
        t.goto(x + i * bar_width * 2, y)
        t.setheading(90)
        t.pendown()
        t.forward(height)
        t.right(90)
        t.forward(bar_width)
        t.right(90)
        t.forward(height)
        t.right(90)
        t.forward(bar_width)
        t.penup()
        t.goto(x + i * bar_width * 2 + bar_width / 2, y - 20)
        t.write(country[:10], align="center")  # Display country name
        t.goto(x + i * bar_width * 2 + bar_width / 2, y + height + 10)
        t.write(f"{population:.0f}", align="center")  # Display population
        t.goto(x + i * bar_width * 2, y)

    screen.mainloop()

# Main function
def main():
    file_pattern = 'population_data.csv'  # Use a pattern that matches your CSV files
    data = read_csv_files(file_pattern)
    plot_data(data)

if __name__ == '__main__':
    main()
