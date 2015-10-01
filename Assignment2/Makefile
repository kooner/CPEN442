all: q3crcbrute.cpp q4crcbrute.cpp
	gcc -c crc.c -o crc.o
	g++ -c q3crcbrute.cpp -o q3crcbrute.o -std=c++11
	g++ -o q3crcbrute.out crc.o q3crcbrute.o
	g++ -c q4crcbrute.cpp -o q4crcbrute.o -std=c++11
	g++ -o q4crcbrute.out crc.o q4crcbrute.o

clean:
	$(RM) *.out *.o

