#ifndef WALLET_HPP
#define WALLET_HPP

#include <iostream>
#include <cstring>
#include <vector>
#include <iterator>
#include <fstream>

#define USAGE_ERROR 0x101
#define FILE_OPEN_ERROR 0x102
#define LOGIN_SET_ERROR 0x103
#define PASSWORD_SET_ERROR 0x104
#define INVALID_LOGIN_OR_PASSWORD 0x105
#define NORMAL_EXIT 0x106
#define NO_OPTION 0x107

#define BALANCE_XOR_KEY 0xdeadbeef

typedef unsigned char BYTE;
typedef unsigned int DWORD;

std::vector<BYTE> 
ReadFile(std::string);

unsigned long 
GetRandomValue(unsigned long);

std::vector<int>
GenGamma(int, int);

class Wallet {
	private:
		std::string Name;
		int balance;
		std::string Info;
		std::vector<std::string> last_operations;

		std::string Username;
		std::string Passsword;

		std::vector<BYTE> RawData;

	public:
		Wallet(std::string Filename);

		void ViewBasicInfo(void);
		bool Decrypt(void);
		void ViewLastOperations(void);
		int GetBalance(void);
		std::string GetInfo(void);
		std::vector<BYTE> GetRawData(void);

		bool SetUsername(std::string);
		bool SetPassword(std::string);
};

#endif
