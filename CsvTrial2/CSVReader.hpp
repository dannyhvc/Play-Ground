#pragma once
#include <string>
#include <vector>
#include <iostream>

/*
 * A class to read data from a csv file.
 */
class CSVReader
{
public:
	//constructors
	CSVReader(std::string filename, std::string delm = ",") :
		fileName_(filename), delimeter_(delm) {	}

	// Function to fetch data from a CSV File
	std::vector<std::vector<std::string>> getData() const { return this->data_; }
	std::vector<std::vector<std::string>> readCSV(void);
	std::vector<std::vector<std::string>> readCSV_str(std::string const& data);
	std::string to_string(void);

	//opertors
	inline friend std::ostream& operator << (std::ostream& os, CSVReader& data) { return os << data.to_string(); }

private:
	std::string fileName_;
	std::string delimeter_;
	std::vector<std::vector<std::string>> data_;
};