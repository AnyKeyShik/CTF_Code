#include <iostream>
#include <fstream>
#include <ctime>
#include <cstdlib>

int main()
{
    std::fstream in("flag.enc", std::fstream::in);
    std::fstream out("out", std::fstream::out);

 	std::string flag;
 	std::string wtf;
 	time_t start_time;

    in >> flag;
    std::cin >> start_time;

 	while(start_time > 0)
 	{
  		srand(start_time);
  		for(int i = 0; i < flag.size(); i++)
 	 	{
            char ch = flag[i] ^ rand() % 255;
            if (!isprint(ch)) {
                break;
            }
    		
            wtf.push_back(ch);
  		} 
  	
        wtf.push_back('\n');
		out << wtf;
  		start_time -= 1;
 	} 
}
