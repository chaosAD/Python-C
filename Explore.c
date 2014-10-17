#include <stdio.h>

typedef struct Point Point;
struct Point {
  int x;
  int y;
};

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

void __declspec(dllexport) set_point(Point *point, int x, int y) {
  point->x = x;
  point->y = y;
}