/*
 * Echo_Server.c
 *
 *  Created on: Sep 3, 2019
 *      Author: Sean
 */

/*Required Headers*/

#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <stdio.h>
#include<string.h>

#define MAX 100

char* Capitalize(char* str)
{
	int i;

	//capitalize first character of words
	for(i=0; str[i]!='\0'; i++)
	{
		//check first character is lowercase alphabet
		if(i==0)
		{
			if((str[i]>='a' && str[i]<='z'))
				str[i]=str[i]-32; //subtract 32 to make it capital
			continue; //continue to the loop
		}
		if(str[i]==' ')//check space
		{
			//if space is found, check next character
			++i;
			//check next character is lowercase alphabet
			if(str[i]>='a' && str[i]<='z')
			{
				str[i]=str[i]-32; //subtract 32 to make it capital
				continue; //continue to the loop
			}
		}
		else
		{
			//all other uppercase characters should be in lowercase
			if(str[i]>='A' && str[i]<='Z')
				str[i]=str[i]+32; //subtract 32 to make it small/lowercase
		}
	}


	return str;
}

int main()
{

    char str[100];
    int listen_fd, comm_fd;

    struct sockaddr_in servaddr;

    listen_fd = socket(AF_INET, SOCK_STREAM, 0);

    bzero( &servaddr, sizeof(servaddr));

    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = htons(INADDR_ANY);
    servaddr.sin_port = htons(22000);

    bind(listen_fd, (struct sockaddr *) &servaddr, sizeof(servaddr));

    listen(listen_fd, 10);

    comm_fd = accept(listen_fd, (struct sosckaddr*) NULL, NULL);

    while(1)
    {

        bzero( str, 100);

        read(comm_fd,str,100);

        printf("Echoing back - %s",str);

        write(comm_fd, str, strlen(str)+1);

    }
}


