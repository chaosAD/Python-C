# The following generates the Add.dll from Add.c file
gcc -shared -o Add.dll Add.c -Wl,--out-implib,libadd_dll.a