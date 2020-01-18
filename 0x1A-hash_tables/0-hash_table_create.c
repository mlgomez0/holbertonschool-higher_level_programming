#include "hash_tables.h"

/**
 *hash_table_create- creates a hash table
 *@size: size of the table
 *Return: a hash table
 */

hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *newh_table;
	hash_node_t **new_array;
	unsigned long int i;

	if (size <= 0)
		return (NULL);
	newh_table = malloc(sizeof(hash_table_t));
	if (newh_table == NULL)
		return (NULL);
	new_array = malloc(sizeof(hash_node_t *) * size);
	if (new_array == NULL)
		return (NULL);
	for (i = 0; i < size; i++)
	{
		new_array[i] = NULL;
	}
	newh_table->size = size;
	newh_table->array = new_array;
	return (newh_table);
}
