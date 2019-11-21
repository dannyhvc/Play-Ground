/**
Author: Daniel Herrera
Date: Nov 9, 2019
*/

//boost libs
#define BOOST_TEST_MODULE __CSV_PARSER__
#include <boost/test/unit_test.hpp>

//std libs
#include <iostream>
using namespace std;

// my headers
#include "CsvParser.hpp"

int main()
{
	return EXIT_SUCCESS;
}

BOOST_AUTO_TEST_CASE(MAIN)
{
#if true
#endif

#if false
	CsvParser* csv = new CsvParser;
	csv->read("tester.csv");
	csv->parse();
	cout << csv->to_string();
	delete csv;
#endif

	//trail 1
#if false
	string row =
		"A,B\n";
	string subs;
	size_t start = 0, end = 0, temp = 0, pos = 0;
	for (auto ch : row)
	{
		if (ch == ',')
		{
			temp = end;
			start = temp;
			end = pos + 1;
			if (end == 0)
				subs = row.substr(start, (end)-start);
			else
				subs = row.substr(start, (end - 1) - start);
			cout << subs << endl;
		}
		if (ch == '\n' || ch == '\r')
		{
			end = pos + 1;
			subs = row.substr(start, (end)-start);
		}
		++pos;
	}
#endif
}