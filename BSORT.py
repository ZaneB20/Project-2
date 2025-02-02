#include <stdio.h>
const int MAX-9

void printValues(int*);
void sort(int*);
void swap(int*, int*);

int main(){
  int values[] = {7, 3, 9, 4, 6, 1, 2, 8, 5};
  printf("Before: \n");
  printValues(values);
  sort(values);
  printf("After: \n");
  printValues(values);

  return(0);
} // end main

void printValues(int* array){
printf("[ ");
for (int i = 0, i < MAX; i++)(
    printf("%d ", array[i]);
)
printf("] \n ");

}


void swap(int* a, int* a){
int temp;
temp = *a;
*a = *b;
*b = temp;

}

void sort(int* array){


