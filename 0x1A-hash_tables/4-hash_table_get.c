#include "hash_tables.h"

/**
 *hash_table_set- Adds a key-value to a hash table
 *@ht: hash table to add the new node
 *@key: to value to add in the table
 *@value: value to add to the table
 *Return: 1 on success and 0 on failute
 */

int hash_table_set(hash_table_t *ht, const char *key, const char *value)
{
	hash_node_t *r;
	hash_node_t *node_head;
	unsigned long int _idx;
	char *empty_str = "\0";

	if (key == NULL || strcmp(key, empty_str) == 0)
		return (0);
	_idx = key_index((unsigned char *)key, ht->size);
	node_head = ht->array[_idx];
	r = add_node(&node_head, key, value);
	ht->array[_idx] = node_head;
	if (r == NULL)
		return (0);
	return (1);
}

/**
 *add_node - adds a new node to the begging of a given linked list
 *@head: head of the linked list
 *@key: key to be placed in the new node
 *@value: value to be placed in new node
 *Return: a pointer to the new head
 */

hash_node_t *add_node(hash_node_t **head, const char *key, const char *value)
{
	hash_node_t *new_node;

	new_node = malloc(sizeof(hash_node_t));
	if (new_node == NULL)
		return (NULL);
	new_node->key = strdup(key);
	new_node->value = strdup(value);
	new_node->next = *head;
	*head = new_node;
	return (*head);
}
