#include "ll.h"
#include <stdio.h>

int JNum(int n){
  return n;
}

bool JBool(bool b){
  return b;
}

char JPrim(char * p){
  return *p;
}

int main(){
  printf("%d\n", JNum(5));
  printf("%d\n", JBool(true));
  return 0;
}
