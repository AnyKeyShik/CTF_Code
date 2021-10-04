TARGET=password
SRC=$(wildcard *.c)

CC=gcc
CFLAGS=-O0 -m32

.PHONY: all clean

all: $(TARGET)

clean: 
	rm -r $(TARGET)

$(TARGET) : $(SRC)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC)
	strip -s $(TARGET)
