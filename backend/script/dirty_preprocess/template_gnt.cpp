#include <iostream>
#include <fstream>
#include <vector>
#include<string>
#include <sstream>
using namespace std;
int main()
{
	vector<vector<string>> v;
	ifstream in("d:\\data.txt");
	ofstream out("d:\\template.txt");
	string s,s1;
	int i = 0;
	while (getline(in,s))
	{
		v.push_back(vector<string>());
		stringstream ss(s);
		while (ss >> s1)
			v[i].push_back(s1);
		i++;
	}
	for (int j = 0; j < v.size(); j++)
	{
		out << "\t<category>\n" << "\t\t<pattern>" << '#' << v[j][0] << '#' << v[j][1] << '#' << v[j][2] << '#' << "</pattern>\n" << "\t\t<template>\n\t\t\ttask_" << v[j][3] << "\n\t\t</template>\n\t</category>\n";
		out << "\t<category>\n" << "\t\t<pattern>" << '#' << v[j][0] << '#' << v[j][2] << '#' << v[j][1] << '#' << "</pattern>\n" << "\t\t<template>\n\t\t\ttask_" << v[j][3] << "\n\t\t</template>\n\t</category>\n";
		out << "\t<category>\n" << "\t\t<pattern>" << '#' << v[j][1] << '#' << v[j][0] << '#' << v[j][2] << '#' << "</pattern>\n" << "\t\t<template>\n\t\t\ttask_" << v[j][3] << "\n\t\t</template>\n\t</category>\n";
		out << "\t<category>\n" << "\t\t<pattern>" << '#' << v[j][1] << '#' << v[j][2] << '#' << v[j][0] << '#' << "</pattern>\n" << "\t\t<template>\n\t\t\ttask_" << v[j][3] << "\n\t\t</template>\n\t</category>\n";
		//out << "\t<category>\n" << "\t\t<pattern>" << '#' << v[j][2] << '#' << v[j][1] << '#' << v[j][0] << '#' << "</pattern>\n" << "\t\t<template>\n\t\t\ttask_" << v[j][3] << "\n\t\t</template>\n\t</category>\n";
		//out << "\t<category>\n" << "\t\t<pattern>" << '#' << v[j][2] << '#' << v[j][0] << '#' << v[j][1] << '#' << "</pattern>\n" << "\t\t<template>\n\t\t\ttask_" << v[j][3] << "\n\t\t</template>\n\t</category>\n";
		
	}		
	in.close();
	out.close();
	system("pause");
}
