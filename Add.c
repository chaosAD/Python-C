#include <stdio.h>

int __declspec(dllexport) sum(int a, int b) {
  return a + b;
}

void __declspec(dllexport) print_hi(char *msg) {
  printf("Hello %s\n", msg);
}

void __declspec(dllexport) get_age(int *agePtr) {
  printf("Please type your age: ");
  scanf("%d", agePtr);
}

void __declspec(dllexport) get_name(char *name) {
  printf("Please type your name: ");
  scanf("%s", name);
}