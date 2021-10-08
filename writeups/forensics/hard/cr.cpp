#include <iostream>
#include <fstream>
#include <ctime>
#include <cstdlib>

int main()
{
    srand(time(NULL));

    std::fstream out("flag.enc", std::fstream::out);

    std::string flag = "oren_ctf_goto_fail!";
    std::string wtf;

    std::cout << time(NULL) << std::endl;

    for(int i = 0; i < flag.size(); i++)
    {
        wtf.push_back(flag[i] ^ rand() % 255);
    }

    out << wtf;
}
