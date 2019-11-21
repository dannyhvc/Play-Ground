#include "CsvParser.hpp"
using namespace std;

CsvParser::~CsvParser()
{
}

/*
*/
void CsvParser::read(string const& file_name)
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
	//names_.resize(1);
	//values_.resize(1);
	//values_[0].resize(1);
	string row;
	size_t carriageReturn = 0, carriageTemp = 0;
	while (!SS_.eof())
	{
		row.clear();
		std::getline(SS_, row); //gets the titles for each column of the graph.
		size_t start = 0, end = 0, temp = 0, pos = 0;

		//string row = "Dan,Lili,asdhflkasjdhflkjashf,asldhflaskjhdfljkashdf,sadf,\n";

		for (auto ch : row)
		{
			switch (ch)
			{
			case '\r':
			case '\n':
				//new row of data row.substr(end, (carriageTemp)-end)
					/*carriageTemp = pos + 1;
					values_[values_.size() - 1].push_back(
						row.substr(end, (carriageTemp)-end)
					);
					++carriageReturn;*/
				break;

				// checking if the character is comma
			case ',':
				temp = end;
				start = temp;
				end = pos + 1;
				switch (carriageReturn) // sets the titles for each column
				{
				case 0:
					switch (end)
					{
					case 0:
						names_.push_back(
							row.substr(start, (end)-start)
						);
						break;

					default:
						names_.push_back(
							row.substr(start, (end - 1) - start)
						);
						break;
					} break;
				default: // for inputting data for the columns
					switch (end)
					{
					case 0:
						for (auto sub_list : values_)
							sub_list.push_back(
								string(row.substr(start, (end)-start))
							);
						break;

					default:
						for (auto sub_list : values_)
							sub_list.push_back(
								string(row.substr(start, (end)-start))
							);
						break;
					} break;
					break;
					++pos;
				}
			}
		}
	}
}//end-parse

// ===================== boost testing ===================== //