TARGET=system_health_check
SRC=$(wildcard *.c)

CC=gcc
CFLAGS=-m32 -no-pie -fno-pie -fno-stack-protector

.PHONY: all clean

all: $(TARGET)

clean: 
	rm -r $(TARGET)

$(TARGET) : $(SRC)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC)
