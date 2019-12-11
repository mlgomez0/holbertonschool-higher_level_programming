#include<stdio.h>
#include<stdlib.h>
#include "lists.h"

/**
 *insert_node - inserts a node according to sorting
 *@head: head of the linked list
 *@number:number to be added to the node
 *Return: The address of the new node or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp1 = NULL;
	listint_t *tmp2 = NULL;
	listint_t *new_node = NULL;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	tmp1 = *head;
	if (*head == NULL || tmp1->n > number)
	{
		*head = new_node;
		new_node->next = tmp1;
		return (*head);
	}
	while (tmp1->next)
	{
		if (tmp1->n < number && tmp1->next->n < number)
			tmp1 = tmp1->next;
		else
		{
			tmp2 = tmp1->next;
			tmp1->next = new_node;
			new_node->next = tmp2;
			return (*head);
		}
	}
	tmp1->next = new_node;
	return (*head);
}
