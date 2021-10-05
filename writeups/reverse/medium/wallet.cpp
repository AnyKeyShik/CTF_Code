#include "wallet.hpp"

Wallet::Wallet(std::string Filename)
{
	Name = Filename;
	RawData = ReadFile(Filename);
}

std::vector<BYTE>
Wallet::GetRawData(void)
{
	return RawData;
}

std::vector<BYTE>
ReadFile(std::string Filename)
{
	std::ifstream InputFile (Filename, std::ios::binary | std::ios::ate);

	// Check file is exist and opened
	if (!InputFile.is_open()) {
		std::cout << "[-] Error in file <" << Filename << "> open!";
		std::cout << std::endl;

		exit(FILE_OPEN_ERROR);
	}

	// Get file size
	std::streamsize FileSize = InputFile.tellg();

    // Make buffer for file data
    char* TempFileDataBuffer = new char[FileSize];

    // Set position to start and read in tmp-buffer
    InputFile.seekg(0, std::ios::beg);
	InputFile.read(TempFileDataBuffer, FileSize);

	InputFile.close();

	std::vector<BYTE> FileData;

	for (int i = 0; i < FileSize; i++) {
		FileData.push_back(TempFileDataBuffer[i]);
	}

	delete[] TempFileDataBuffer;

	return FileData;
}

bool
Wallet::SetUsername(std::string InpUsername)
{
	if (InpUsername.size() > 32) {
		return false;
	}

	Username = InpUsername;

	return true;
}

bool
Wallet::SetPassword(std::string InpPassword)
{
	if (InpPassword.size() > 64) {
		return false;
	}

	Passsword = InpPassword;

	return true;
}

bool
Wallet::Decrypt(void)
{
	int file_offset = 0;

	int OriginalUsernameSize = (int) RawData[file_offset];
	file_offset += 1;

	// Check username
	if (OriginalUsernameSize != Username.size()) {
		return false;
	}

	std::vector<int> UsernameGamma = GenGamma(OriginalUsernameSize, OriginalUsernameSize);

	for (int i = 0; i < OriginalUsernameSize; i++) {
		if ( (RawData[file_offset + i] ^ UsernameGamma[i]) != Username[i] ) {
			return false;
		}
	}

	file_offset += OriginalUsernameSize;

	// Check password
	int OriginalPasswordSize = (int) RawData[file_offset];
	file_offset += 1;

	if (OriginalPasswordSize != Passsword.size()) {
		return false;
	}

	std::vector<int> PasswordGamma = GenGamma(OriginalPasswordSize, OriginalPasswordSize);

	for (int i = 0; i < OriginalPasswordSize; i++) {
		if ( (RawData[file_offset + i] ^ PasswordGamma[i] ) != Passsword[i] ) {
			return false;
		}
	}

	file_offset += OriginalPasswordSize;

	// Get balance
	char tmp_buffer[4];
	tmp_buffer[0] = RawData[file_offset + 3];
	tmp_buffer[1] = RawData[file_offset + 2];
	tmp_buffer[2] = RawData[file_offset + 1];
	tmp_buffer[3] = RawData[file_offset];
	file_offset += 4;

	memcpy(&balance, tmp_buffer, 4);
	balance ^= BALANCE_XOR_KEY;

	// Get operations
	int OperationsSize = (int) RawData[file_offset];
	file_offset += 1;

	for (int i = 0; i < OperationsSize; i++) {
		int EntrySize = (int) RawData[file_offset];
		file_offset += 1;

		std::string Operation(EntrySize, ' ');

        for (int j = 0; j < EntrySize; j++) {
			Operation[j] = RawData[file_offset + j] ^ EntrySize;
        }
		
		file_offset += EntrySize;
		last_operations.push_back(Operation);
	}

	// Get info
	int InfoSize = (int) RawData[file_offset];
	file_offset += 1;

	std::string XorKey = Username + Passsword;
	std::string DecodedInfo(InfoSize, ' ');

	for (int i = 0; i < InfoSize; i++) {
		DecodedInfo[i] = RawData[file_offset + i] ^ XorKey[i % XorKey.size()];
	}

	Info = DecodedInfo;

	return true;
}

int
Wallet::GetBalance(void)
{
	return balance;
}

std::string 
Wallet::GetInfo(void)
{
	return Info;
}

void 
Wallet::ViewLastOperations(void)
{
	std::cout << "--- Last Operations ---" << std::endl;

	for (int i = 0; i < last_operations.size(); i++) {
		std::cout << i << ". " << last_operations[i] << std::endl;
	}
}

unsigned long 
GetRandomValue(unsigned long seed)
{
  return (seed >> 1) & 0xff;
}

std::vector<int>
GenGamma(int seed, int sz)
{
	std::vector<int> gamma;

	int value = seed;

	for (int i = 0; i < sz; i++) {
		value = GetRandomValue(seed);
		seed += value;
		gamma.push_back(value);
	}

	return gamma;
}

