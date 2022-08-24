#include <iostream>
using namespace std;

void swap(int a, int b)
{
    int tmp = a;
    a = b;
    b = tmp;
}

void reverseArrayUsingPrint(int arr[], int length)
{
    // this way not change value of array
    /*
        example:
           original array: {2,5,4,1,3,3,4}
           affter call function: {2,5,4,1,3,3,4}
    */
    for (int i = length - 1; length >= 0; i--)
    {
        cout << arr[i] << " ";
    }
}

void reverseArrayWithSwap(int arr[], int length)
{
    // this way change value of array
    /*
        example:
           original array: {2,5,4,1,3,3,4}
           affter call function: {4,3,3,1,4,5,2}
    */
    int start = 0;
    int end = length - 1;
    while (start <= end)
    {
        swap(arr[start], arr[end]);
        start++;
        end--;
    }

    cout << "After reverse" << endl;
    for (int i = 0; i < length; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main()
{

    int n;
    cin >> n;

    int a[n];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }

    reverseArrayUsingPrint(a, n);
    reverseArrayWithSwap(a, n);

    return 0;
}