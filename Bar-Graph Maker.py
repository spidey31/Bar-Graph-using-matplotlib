import matplotlib.pyplot as plt

try:

    x_input = input("Enter x-axis values (e.g., 1,2,3,4): ")

    y_input = input("Enter y-axis values (e.g., 10,20,25,40): ")

    x_values = [float(item.strip()) for item in x_input.split(',')]
    y_values = [float(item.strip()) for item in y_input.split(',')]

    if len(x_values) != len(y_values):
        print("Error: The number of x-values must match the number of y-values.")
    else:
        plt.figure(figsize=(8, 6))

        plt.plot(x_values, y_values, marker='o', linestyle='-', color='purple')

        # Add a title and labels for clarity.
        plt.title('Custom Plot from User Input')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')

        # Add a grid for easier readability.
        plt.grid(True)

        # Display the plot.
        plt.show()

except ValueError:
    print("Error: Please enter a comma-separated list of valid numbers.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")