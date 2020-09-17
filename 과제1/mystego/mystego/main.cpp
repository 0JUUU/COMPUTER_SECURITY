#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

/*
	[24비트 비트맵]
	비트맵 파일 헤더(14) + 비트맵 정보 헤더(40) + 픽셀 데이터(가변적)
*/

// 경로 고정
const string INPUT_NAME = "origin.bmp";
const string OUTPUT_NAME = "stego.bmp";

// file I/O
ifstream in;
ofstream out;

// 문자열 구분 마크
const int mark = -1;

string msg;

// 비트맵 관련 배열
char* buf;

void encoding()
{
	// binary 형식으로 'origin.bmp' 읽기
	in.open(INPUT_NAME, ios::binary);

	// 파일 읽기 오류
	if (!in.is_open())
	{
		cout << "WRONG : FILE ERROR\n";
		return;
	}

	// 파일 마지막으로 포인터를 옮겨 전체 크기 구하기
	in.seekg(0, ios::end);
	int size = in.tellg();

	// 포인터 위치 처음으로 조정
	in.seekg(0, ios::beg);

	buf = new char[size];
	in.read(buf, size);

	// message (이하 msg) 입력
	cout << "INPUT MESSAGE : ";
	getline(cin, msg);

	out.open(OUTPUT_NAME, ios::binary);

	// stego.bmp에 쓰기
	out.write(buf,size);

	// 입력 문자열을 구분해줄 mark(-1) 쓰기
	out.write((char*)&mark, sizeof(int));
	out << msg;

	cout << "HIDDEN COMPLETE!\n";
	in.close();
	out.close();
}

void decoding()
{
	in.open(OUTPUT_NAME, ios::binary);

	// 파일 읽기 오류
	if (!in.is_open())
	{
		cout << "WRONG : FILE ERROR\n";
		return;
	}

	in.seekg(0, ios::end);
	int sz = in.tellg();

	in.seekg(0, ios::beg);

	buf = new char[sz];
	in.read(buf, sz);

	int i = 1;
	vector<char> v;
	char ch;

	while (true) 
	{
		ch = buf[sz - i];
		v.push_back(ch);
		
		// mark를 발견하면 해당 반복문을 끝냄
		if (ch == -1)
			break;
		i++;
	}

	// 뒤에서부터 저장된 것을 뒤집어줌
	reverse(v.begin(), v.end());
	// -1값 제거
	v.erase(v.begin() + 0);

	for (int i = 0; i < v.size(); i++)
		cout << v[i];

	in.close();
	out.close();
}

int main(int argc, char* argv[])
{

	switch (argv[1][0])
	{
	case 'e':
		encoding();
		break;

	case 'd':
		decoding();
		break;

	default:
		break;
	}
	return 0;
}