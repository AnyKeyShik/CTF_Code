TARGET=shop
SRC=$(wildcard *.c)

CC=gcc
CFLAGS=-static -fstack-protector

.PHONY: all clean

all: $(TARGET)

clean:
	rm -r $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC)
