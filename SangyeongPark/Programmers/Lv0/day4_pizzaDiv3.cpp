#include <string>
#include <vector>

using namespace std;

int solution(int slice, int n) 
{
    int pizza;
    int i =1;

    while(true)
    {
        pizza = slice * i;

        if(i*slice >= n) break;

        i++;
    }

    return i;
}