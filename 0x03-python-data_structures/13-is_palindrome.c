#include"lists.h"

/**
 *is_palindrome - this function evaluates if singly linked list is palindrome
 *@head:head of the singly linked list
 *Return: 0 if it is not palidrome or 1 if it is palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head, *temp2;
	int len = 0, i, j;

	if (*head == NULL || head == NULL || (*head)->next == NULL)
		return (1);
	while (temp)
	{
		len++;
		temp = temp->next;
	}
	temp = *head;
	for (i = 0; i < len / 2; i++)
	{
		temp2 = *head;
		for (j = 1; j < (len - i); j++)
		{
			temp2 = temp2->next;
		}
		if (temp2->n != temp->n)
			return (0);
		temp = temp->next;
	}
	return (1);
}
