//abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-=
#include <bits/stdc++.h>
using namespace std;
int t(int k)
{
    int r = rand() % k + 1;
    for (int i = 0; i < r; i++)
    {
        if (char(k) == 'a')
        {
            k = 122;
            continue;
        }
        k--;
    }
    for (int i = r - 1; i >= 0; i--)
    {
        if (char(k) == 'z')
        {
            k = 97;
            continue;
        }
        k++;
    }
    return char(k);
}
int l(int k)
{
    int e = k;
    for (int i = 0; i < rand() % 1000 + 2; i++)
    {
        e = (e % 2) ? (((e + 1) / 2) * e) : ((e / 2) * (e + 1));
    }
    return e;
}

string b(int k)
{
    vector<char> a;
    a.clear();

    int temp;

    for (int i = 0; k > 0; i++)
    {
        temp = k % 16;

        if (k % 16 < 10)
        {
            a.push_back(temp + 48);
        }
        else
        {
            a.push_back(temp + 87);
        }
        k /= 16;
    }

    string o = "";

    for (int i = a.size() - 1; i >= 0; i--)
    {
        o += a[i];
    }
    o += " ";
    return o;
}

int c(int k, int b)
{
    int z;
    for (int j = 1; j <= 4; j++)
    {
        for (int i = 0; i < 50; i++)
        {
            if (j % 2 != 0)
            {
                k += b;
            }
            else
            {
                k -= b;
            }
        }
    }
    return char(k);
}
int found(int x)
{
    int found = 0;
    int ans = -1;
    for (int i = 33; i <= 122; i++)
    {
        if (found)
        {
            break;
        }
        int e = i;
        for (int j = 0; j < 2 + 999; j++)
        {
            e = (e % 2) ? (((e + 1) / 2) * e) : ((e / 2) * (e + 1));
            if (e == x)
            {
                ans = i;
                found = 1;
                break;
            }
        }
    }
    return ans;
}
int main()
{
    vector<string> a = {"bafa1d", "1318e7c", "1318e7c", "9ead68", "b754d", "1537969", "9ead68", "17823eb", "d6cb9", "147deba", "19fb307", "9ead68", "bafa1d", "a8f6c", "a8f6c", "1085d81"};
    vector<int> b;
    for (auto i : a)
    {
        b.push_back(stoll(i, 0, 16));
    }
    for (auto i : b)
    {
        cout << char(found(i)) << "";
    }
    cout<<endl;

}