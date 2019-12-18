#include"lists.h"

/**
 *is_palindrome - this function evaluates if singly linked list is palindrome
 *@head:head of the singly linked list
 *Return: 0 if it is not palidrome or 1 if it is palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int len = 0, i, j;
	int buf[9999];

	if (*head == NULL)
		return (1);
	len = len_list(temp);
	temp = *head;
	for (i = 0; i < len; i++)
	{
		buf[i] = temp->n;
		temp = temp->next;
	}
	temp = *head;
	for (j = 0; j < len; j++)
	{
		if (temp->n != buf[len - 1 - j])
			return (0);
		temp = temp->next;
	}
	return (1);
}

/**
 *len_list - calculate the size of a linked list
 *@temp:head of the singly linked list
 *Return: the size of the list
 */
int len_list(listint_t *temp)
{
	int len = 0;

	while (temp)
	{
		len++;
		temp = temp->next;
	}
	return (len);
}
