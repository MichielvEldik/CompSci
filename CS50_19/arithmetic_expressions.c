#include <stdio.h>

int main()
{
		int radius;
		printf("Please enter a radius: ");
		scanf("%i", &radius);
		
		double area = 3.14159 * (radius * radius);
		printf("The area of a circle wiht %i radius is %f\n", radius, area);
		return 0;
}
