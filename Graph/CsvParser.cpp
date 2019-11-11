#include "CsvParser.hpp"
#include <iostream>
using namespace std;

/*
*/
void CsvParser::read_csv(string const& file_name)
{
	csvFile_.open(file_name, ios::binary); // OPEN >>>>
	if (!csvFile_)
	{
		cerr << "Unable to open file" << endl;
		exit(EXIT_FAILURE);   // call system to stop
	}
	SS_ << csvFile_.rdbuf();
	csvFile_.close();// CLOSE <<<<
}//end-read_csv

/*

*/
void CsvParser::parse()
{
	structure_ = new vector<mapper<>>; // init the structure_ member
	string rows;
	while (!SS_.eof())
	{
		size_t pos = 0, start = 0, end = 0, i = 0; //for flagging and iterating through the string
		vector<size_t> endPosArr; // for keeping track of end points
		rows.clear();
		getline(SS_, rows); //gets the titles for each column of the graph.

		for (char ch : rows)
		{
			if (ch == ',')
			{
				end = pos;
				endPosArr.push_back(pos);
				if (endPosArr.size() <= 1);
				else
				{
					start = endPosArr[i]; // the start position is always going to be at the flag before the end.
					++i; //move it over for the next session.
				}//end if;-else
			}
			else if (ch == '\n')
			{
			}
			++pos;
		}//end-while
	}
}//end-parse