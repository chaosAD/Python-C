# The following generates the Add.dll from Add.c file
gcc -shared -o Explore.dll Explore.c -Wl,--out-implib,libexplore_dll.a