#!/bin/sh

echo "Start encryption..."
echo "Alice encrypt..."
openssl rsautl -encrypt -raw -inkey alice.pub -pubin -in flag -out flag.enc.alice
echo "Bob encrypt..."
openssl rsautl -encrypt -raw -inkey bob.pub -pubin -in flag -out flag.enc.bob
echo "Eve encrypt..."
openssl rsautl -encrypt -raw -inkey eve.pub -pubin -in flag -out flag.enc.eve
echo "Encrypted successfully!"

echo -en "Let's test...\nAlice:\t"
openssl rsautl -decrypt -raw -inkey alice -in flag.enc.alice
echo -en "Bob:\t"
openssl rsautl -decrypt -raw -inkey bob -in flag.enc.bob
echo -en "Eve:\t"
openssl rsautl -decrypt -raw -inkey eve -in flag.enc.eve
echo "All done"
