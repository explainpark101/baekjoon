#include <iostream>

using namespace std; 
  
// function check whether a number is prime or not 
bool isPrime(int n) 
{ 
    // Corner case 
    if (n <= 1) 
        return false; 
    if (n==2) return true;
    // Check from 2 to n-1 
    if (!(n & 1)) return false;
    for (int i = 3; i < n; i+=2) 
        if (n % i == 0) 
            return false; 
  
    return true; 
} 
  
// Function to print primes 
void printPrime(long long n) 
{ 
    for (long long i = 2; i <= n; i++) 
        if (isPrime(i)) 
            cout << i*i << ", "; 
} 
  
// Driver Code 
int main() 
{ 
    long long n = 1000002; 
    cout << '{';
    printPrime(n); 
    cout << '}';
} 