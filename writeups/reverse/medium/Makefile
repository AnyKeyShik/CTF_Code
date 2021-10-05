TARGET=bcw
SRC=$(wildcard *.cpp)

CC=g++

.PHONY: all clean

all: $(TARGET)

clean: 
	rm -r $(TARGET)

$(TARGET) : $(SRC)
	$(CC) -o $(TARGET) $(SRC)
	strip -s $(TARGET)
