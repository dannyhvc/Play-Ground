/**
Author: Daniel Herrera
Date: Nov 9, 2019
*/

#include <iostream>
//#include <string>
//#include <algorithm>
//#include <vector>
//#include <list>
using namespace std;

#include "CsvParser.hpp"

int main(int argv[], char* argc[])
{
	CsvParser* csv = new CsvParser;
	csv->read_csv("taxi-fare-train.csv");
	csv->parse();
	return EXIT_SUCCESS;
}