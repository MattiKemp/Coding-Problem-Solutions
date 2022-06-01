#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'primeCount' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts LONG_INTEGER n as parameter.
 */

int primeCount(long n) {
    // see python solution for notes, the below solution did not work
    // even though it is a near copy of the python solution. I am guessing
    // it is some kind of overflow error for large values, but my attempts
    // to amend the solution did not work and I don't have hackrank premium to see
    // what inputs are causing the error.
    int primes[] = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53};
    long primorial = 1;
    int spot = 0;
    while(primorial <= n){
        primorial *= primes[spot];
        spot++;
    }
    return spot - 1;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string q_temp;
    getline(cin, q_temp);

    int q = stoi(ltrim(rtrim(q_temp)));

    for (int q_itr = 0; q_itr < q; q_itr++) {
        string n_temp;
        getline(cin, n_temp);

        long n = stol(ltrim(rtrim(n_temp)));

        int result = primeCount(n);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

