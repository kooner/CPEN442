all: crcbrute3.cpp crcbrute4.cpp
	gcc -c crc.c -o crc.o
	g++ -c crcbrute3.cpp -o crcbrute3.o -std=c++11
	g++ -o crcbrute3.out crc.o crcbrute3.o
	g++ -c crcbrute4.cpp -o crcbrute4.o -std=c++11
	g++ -o crcbrute4.out crc.o crcbrute4.o

clean:
	$(RM) *.out *.o

