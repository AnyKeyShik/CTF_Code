TARGET=wizards
SRC=$(wildcard *.c)

CC=gcc
CFLAGS=-fno-stack-protector

.PHONY: all clean

all: $(TARGET)

clean: 
	rm -r $(TARGET)

$(TARGET) : $(SRC)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC)
