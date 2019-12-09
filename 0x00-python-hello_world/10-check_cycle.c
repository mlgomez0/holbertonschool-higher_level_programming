#include "lists.h"
#include <stdio.h>
#include <string.h>

/**
 *check_cycle - checks if a given list has a loop
 *@list: head of the singly linked list
 *Return: 0 if there is not cycle or 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *hare;
	listint_t *tortuise;

	hare = list;
	tortuise = list;
	while (1)
	{
		if (hare == NULL || hare->next == NULL)
			return (0);
		hare = hare->next->next;
		tortuise = tortuise->next;
		if (tortuise == hare)
			return (1);

	}
}
