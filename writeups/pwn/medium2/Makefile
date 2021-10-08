TARGET=MAL
SRC=$(wildcard *.c)

CC=gcc
CFLAGS=-Wall

.PNONY: all clean

all: $(TARGET)

clean:
	rm -r $(TARGET)

$(TARGET) : $(SRC)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC)
