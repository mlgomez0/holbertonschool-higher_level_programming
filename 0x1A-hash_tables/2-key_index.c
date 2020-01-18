#include "hash_tables.h"

/**
 *key_index - determines the index to allocate or retrieve a key-value
 *@size: size of the hash table
 *@key: key of hash table
 *Return: and unsigned long int with the index of the key-value
 */

unsigned long int key_index(const unsigned char *key, unsigned long int size)
{
	unsigned long int my_index;

	my_index = (hash_djb2(key)) % size;
	return (my_index);
}
