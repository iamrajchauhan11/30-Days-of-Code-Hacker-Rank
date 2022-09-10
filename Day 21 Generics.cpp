/* Hello Guys Welocme Back ...
Day 21 Generics....
So, In this video we will use C++. Because in Hacker Rank there are no option for pyhton for this problem to solve... So bacically i have not the c++ complier thats why the program should be highlighted red please ignore it...

So come to the point.. Below code is already given in the terminal when you select C++ (Note: Please Select C++ only.)

Let's start coding....


*/


#include <iostream>
#include <vector>
#include <string>

using namespace std;

/**
*    Name: printArray
*    Print each element of the generic vector on a new line. Do not return anything.
*    @param A generic vector
**/

// Write your code here
// We have to write our code here...
template <class T>
void printArray(vector<T> vec){
    for (int i=0; i<vec.size(); i++)
    cout<<vec[i]<<endl;
}
//This is the 5 line code you have to write and then Just Run and submit your code..
// Thankyou for your support.... i will see you on next day...
//KEEP CODING AND KEEP LEARNING..


int main() {
	int n;
	
	cin >> n;
	vector<int> int_vector(n);
	for (int i = 0; i < n; i++) {
		int value;
		cin >> value;
		int_vector[i] = value;
	}
	
	cin >> n;
	vector<string> string_vector(n);
	for (int i = 0; i < n; i++) {
		string value;
		cin >> value;
		string_vector[i] = value;
	}

	printArray<int>(int_vector);
	printArray<string>(string_vector);

	return 0;
}