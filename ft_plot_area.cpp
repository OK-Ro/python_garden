#include <iostream>

void ft_plot_area()
{
	int length = 0;
	int width = 0;

	std::cout << "Enter length: ";
	std::cin >> length;
	std::cout << "Enter width: ";
	std::cin >> width;
	int result = (length * width);
	std::cout << "Plot area: " << result << std::endl;
}

int main(void)
{
	ft_plot_area();
	return (0);
}